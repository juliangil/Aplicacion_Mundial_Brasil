from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mundial_brasil.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Va a la vista que muestra los partidos ordenados por fecha.
    url(r'^$', 'partidos.views.ver_partidos', name='ver_partidos'),
    # Rutas del administrador de Django
    url(r'^admin/', include(admin.site.urls)),
]
