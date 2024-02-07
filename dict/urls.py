
from django.urls import path
from .views import home, c3d2, epmd, tmd, projectClick, insert_data,add_data_ojt_form,edit_data_ojt,view_data_ojt

urlpatterns = [
    path('', home, name='home'),      # URL for the home view
    path('c3d2/', c3d2, name='c3d2'),  # URL for the c3d2 view
    path('epmd/', epmd, name='epmd'),  # URL for the epmd view
    path('tmd/', tmd, name='tmd'),     # URL for the tmd view
    path('projectClick/', projectClick, name='projectClick'),  # URL for the projectClick view
    path('insert_data/', insert_data, name='insert_data'),
    path('add_data_ojt_form/', add_data_ojt_form, name='add_data_ojt_form'),
    path('edit_data_ojt/<int:application_id>/',edit_data_ojt, name='edit_data_ojt'),
    path('view_data_ojt/<int:application_id>/',view_data_ojt, name='view_data_ojt'),

 ]
