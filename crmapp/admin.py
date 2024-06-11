from django.contrib import admin
#step 2
#step 3 make migrations and migrate command run karo isse table create hogi 
from . models import Enquiry,Customer,Login
# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Customer)
admin.site.register(Login)


