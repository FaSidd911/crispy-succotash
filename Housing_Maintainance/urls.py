
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "HSMA Portal"
admin.site.site_title = "HSMA Admin Portal"
admin.site.index_title = "Welcome to HSMA App Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
]
