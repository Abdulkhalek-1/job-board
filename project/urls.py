from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path('jobs/', include("job.urls")),
    # path('accounts/', include("accounts.urls")),
    # path('blog', include("blog.urls")),
    # path('contact', include("contact.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
