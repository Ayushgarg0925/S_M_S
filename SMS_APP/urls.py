from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('log/',log_in),
    path('edit/<int:a>/',edit_page),
    path('delete/<int:a>/',delete_data),
    path('edit1/<int:a>/',showall_edit_page),
    path('delete1/<int:a>/',delete_data_allpage),
]           
