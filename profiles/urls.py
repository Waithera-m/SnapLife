from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'profiles'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)