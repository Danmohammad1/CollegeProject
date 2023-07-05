from django.contrib import admin

# Register your models here.
from .models import User
from .models import hiringForm
from .models import Contact

admin.site.register(User)
admin.site.register(hiringForm)
admin.site.register(Contact)
