"""
URL configuration for afra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from users import views
from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('course/', include('course.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404='users.views.view404'

# Custom 404 page
def handler_404(request, exception=None):
    return render(request, '404page.html', status=404)

# URL pattern to handle unmatched URLs
urlpatterns += [
    re_path(r'^.*$', handler_404),
]