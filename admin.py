from django.contrib import admin
from .models import Builds, Inks, Follows


admin.site.register(Builds)
admin.site.register(Inks)
admin.site.register(Follows)
