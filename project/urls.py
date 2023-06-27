from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('', include("home.urls")),
    path('jobs/', include("job.urls", namespace="jobs")),
    # path('accounts/', include("accounts.urls")),
    # path('blog', include("blog.urls")),
    # path('contact', include("contact.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
