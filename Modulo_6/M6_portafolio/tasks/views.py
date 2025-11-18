from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Category
from .forms import TaskForm, CategoryForm
from django.db.models import Q

# Vista de inicio/home
def home(request):
    return render(request, 'tasks/home.html')

# Lista de tareas

@login_required
def task_list(request):

    # Query de busqueda, filtrar por estado y filtrar por prioridad

    search_query = request.GET.get('search', '')
    filter_status = request.GET.get('status', '')
    filter_priority = request.GET.get('priority', '')
    
    # Obtener las tareas del usuario

    tasks = Task.objects.filter(user=request.user)
    
    # Uso de queries de busqueda

    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    if filter_status:
        tasks = tasks.filter(status=filter_status)
    
    if filter_priority:
        tasks = tasks.filter(priority=filter_priority)
    
    # Contexto para la vista

    context = {
        'tasks': tasks,
        'search_query': search_query,
        'filter_status': filter_status,
        'filter_priority': filter_priority,
    }

    return render(request, 'tasks/task_list.html', context)

# Detalle de tarea

@login_required
def task_detail(request, pk):

    # Obtener tarea por Primary Key
    task = get_object_or_404(Task, pk=pk, user=request.user)

    return render(request, 'tasks/task_detail.html', {'task': task})

# Crear tarea
@login_required
def task_create(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Tarea creada exitosamente.')
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Crear Tarea'})

# Editar tarea

@login_required
def task_update(request, pk):

    # Obtener tarea por Primary Key
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada con éxito.')
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Editar Tarea', 'task': task})


# Eliminar tarea

@login_required
def task_delete(request, pk):

    # Obtener tarea por Primary Key
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarea eliminada con éxito.')
        return redirect('task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})



# Lista de categorías

@login_required
def category_list(request):

    # Obtener todas las categorías
    categories = Category.objects.all()

    return render(request, 'tasks/category_list.html', {'categories': categories})



# Crear categoría


@login_required
def category_create(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada con éxito')
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'tasks/category_form.html', {'form': form, 'title': 'Crear Categoría'})


# Eliminar categoría

@login_required
def category_delete(request, pk):

    # Obtener categoría por Primary Key
    category = get_object_or_404(Category, pk=pk)
    
    # Contar cuántas tareas usan esta categoría
    tasks_count = Task.objects.filter(category=category).count()
    
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Categoría eliminada exitosamente!')
        return redirect('category_list')
    

    # Contexto para la vista

    context = {
        'category': category,
        'tasks_count': tasks_count,
    }
    
    return render(request, 'tasks/category_confirm_delete.html', context)