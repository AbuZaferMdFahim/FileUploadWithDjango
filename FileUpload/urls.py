from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from home.views import HandleFileUploadView, home, download
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),  
    path('download/<uid>/', download, name='download'),  
    path('admin/', admin.site.urls),
    path('handle/', HandleFileUploadView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
