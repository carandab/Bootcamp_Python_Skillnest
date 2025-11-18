from django.contrib import admin
from .models import Task, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    ordering = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ['title', 'user', 'priority', 'status', 'category', 'due_date', 'created_at']
    list_filter = ['status', 'priority', 'category', 'created_at', 'due_date']
    search_fields = ['title', 'description', 'user__username']
    list_editable = ['status', 'priority']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'user')
        }),
        ('Clasificación', {
            'fields': ('priority', 'status', 'category')
        }),
        ('Fechas', {
            'fields': ('due_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        
        # Query Set
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        
        return qs.filter(user=request.user)