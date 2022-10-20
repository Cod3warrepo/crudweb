from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('std_db', views.std_db, name='std_db'),
    path('std_db_add', views.std_db_add, name='std_db_add'),
    path('std_db_add_func', views.std_db_add_func, name='std_db_add_func'),
    path('std_db_edit/<int:id>', views.std_db_edit, name='std_db_edit'),
    path('std_db_edit_func/<int:id>', views.std_db_edit_func, name='std_db_edit_func'),
    path('std_db_delete/<int:id>', views.std_db_delete, name='std_db_delete'),
    
]
