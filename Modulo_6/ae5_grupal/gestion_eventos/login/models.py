from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ('ver_eventos', 'Puede ver los eventos'),
            ('editar_eventos', 'Puede editar los eventos'),
            ('eliminar_eventos', 'Puede eliminar los eventos'),
            ('crear_eventos', 'Puede crear eventos'),
        ]
