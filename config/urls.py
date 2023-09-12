
from django.contrib import admin
from django.urls import path, include


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configurations for API documentation

schema_view = get_schema_view( # new
openapi.Info(
title="Person API",
default_version="v1",
description="HNGx second stage task",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="jpcwork081@gmail.com"),
license=openapi.License(name="BSD License"),
),
public=True,
# permission_classes=(permissions.AllowAny,),
)


# Projects urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),

    # path for interactive documentation
    path('swagger/', schema_view.with_ui( 'swagger', 
            cache_timeout=0), name='schema-swagger-ui'),
]


handler404 = 'api.views.endpoint_error_handler'