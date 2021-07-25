from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import mimetypes
mimetypes.add_type("text/css", ".css", True)

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('admin/', admin.site.urls),
    path('',include('Netwok_automation.urls')),
]

urlpatterns += staticfiles_urlpatterns()




