from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from AIwebApp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("AIsite.urls")),
] + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     pass
# else:
#     urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)

