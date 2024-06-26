from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from recipes.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('recipes/', include('recipes.urls')),
    path('profile/', include('users.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)