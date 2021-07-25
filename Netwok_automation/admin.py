from django.contrib import admin
from .models import Device
import mimetypes
mimetypes.add_type("text/css", ".css", True)

admin.site.register(Device)
