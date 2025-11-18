from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Mixin personalizado para requerir autenticación"""
    login_url = '/login/'
    redirect_field_name = 'next'


class CustomPermissionRequiredMixin(PermissionRequiredMixin):
    """Mixin personalizado para requerir permisos específicos"""
    login_url = '/login/'
    redirect_field_name = 'next'
    raise_exception = True  # Lanza excepción para que Django use el handler403 personalizado


class ProtectedTemplateView(CustomLoginRequiredMixin, TemplateView):
    """Vista base protegida que requiere autenticación"""
    pass


class PermissionProtectedTemplateView(CustomLoginRequiredMixin, CustomPermissionRequiredMixin, TemplateView):
    """Vista base protegida que requiere autenticación y permisos específicos"""
    pass
