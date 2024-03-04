"""
URL configuration for anp project.

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/', admin.site.urls),
    path('translation/', include('rosetta.urls')),
    path('account/', include('account.urls')),
    path("", include("main.urls")),
    path("", include("etc.urls")),
    path("shop/", include("shop.urls")),
    path("blog/", include("blog.urls")),
    path("project/", include("project.urls")),
    path("service/", include("service.urls")),
    path('tinymce/', include('tinymce.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'etc.views.error_404_view'