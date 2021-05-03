from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    # Tiene que tener el mismo nombre que el atributo de arriba!
    def full_name(self, obj):
        # print(obj) # Todos los registros del modelo empleado
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',) # Campo de busqueda. En base a que se realiza la busqueda. En este caso nombre.
    list_filter = ('job', 'habilidades')
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)