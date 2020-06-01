from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_profile/', views.new_profile, name='new_profile'),
    path('user_profile/<int:profile_id>', views.user_profile, name='user_profile'),
    path('upload_image/', views.upload_image, name='upload'),
    path('search/', views.search_by_username, name='search_results'),
    path('posts/user_profile/<int:profile_id>', views.all_images, name='posts'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)