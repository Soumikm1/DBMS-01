from django.contrib import admin
from django.urls import path, include
from fest import views

admin.site.site_header = "FEsT Admin"
admin.site.site_title = "FEsT Admin Portal"
admin.site.index_title = "Welcome to FEsT Portal"

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('', include('festapp.urls')),
]
