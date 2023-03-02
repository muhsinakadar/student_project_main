from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from StudentManagementSystem import views, admin_views, faculty_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name='base'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)