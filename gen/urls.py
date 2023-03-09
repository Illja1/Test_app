from django.urls import path
from . import views

urlpatterns = [
    path('schemas/',views.main,name='main'),
    path('mymodel/<int:pk>/delete/', views.MyModelDeleteView.as_view(), name='mymodel_delete'),
    path('',views.user_login,name='login'),
    path('csvdata/<int:pk>/edit/',views.edit_csvdata, name='edit_csvdata'),
    path('log',views.user_logout,name='logout'),
    path('generate-csv/', views.generate_csv, name='generate_csv'),
]