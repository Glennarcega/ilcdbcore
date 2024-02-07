
from django.urls import path
from .views import home, c3d2, epmd, tmd, projectClick, insert_data

urlpatterns = [
    path('', home, name='home'),      # URL for the home view
    path('c3d2/', c3d2, name='c3d2'),  # URL for the c3d2 view
    path('epmd/', epmd, name='epmd'),  # URL for the epmd view
    path('tmd/', tmd, name='tmd'),     # URL for the tmd view
    path('projectClick/', projectClick, name='projectClick'),  # URL for the projectClick view
    path('insert_data/', insert_data, name='insert_data'),
 
]
