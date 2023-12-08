from django.contrib import admin
from myapp.models import product2,sadman,orders



admin.site.register(product2)
admin.site.register(orders)

# Register your models here.




class sadmanadmin(admin.ModelAdmin):
    list_display=('username','city','thana','area','images')
admin.site.register(sadman,sadmanadmin)
