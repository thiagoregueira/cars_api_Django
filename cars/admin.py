from django.contrib import admin

from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    """
    Classe de administração para a entidade Brand.

    Atributos:
        list_display (list): Campos a serem exibidos na lista de registros.
        search_fields (list): Campos que podem ser utilizados para busca.
    """

    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']


class CarAdmin(admin.ModelAdmin):
    """
    Classe de administração para a entidade Car.

    Atributos:
        list_display (list): Campos a serem exibidos na lista de registros.
        search_fields (list): Campos que podem ser utilizados para busca.
        list_filter (list): Campos que podem ser utilizados para filtragem.
    """

    list_display = [
        'id',
        'model',
        'brand__name',
        'color',
        'factory_year',
        'model_year',
        'created_at',
    ]
    search_fields = ['model']
    list_filter = ['brand']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
