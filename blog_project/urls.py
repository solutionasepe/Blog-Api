"""
URL configuration for blog_project project.

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
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


API_DESCRIPTION = 'A web Api for creating and editing blog post'
schema_view = get_schema_view(title='Blog API')
swagger_view = get_swagger_view(title="Blog API")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('', RedirectView.as_view(url='api/v1/', permanent = True)),
    path('api-auth/', include('rest_framework.urls')),
    path("api/v1/dj-rest-auth/", include('dj_rest_auth.urls')),
    path("api/v1/dj-rest-auth/registration/", include('dj_rest_auth.registration.urls')),
    path("docs/", include_docs_urls(title="Blog Api", description=API_DESCRIPTION)),
    path('schema/', schema_view),
    path('swagger-docs/', swagger_view),
]
