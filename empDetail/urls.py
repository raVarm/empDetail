from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addData/', views.addEmployeeData, name='addData'),
    path('empLists/', views.empLists, name='empLists'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update , name="update"),
    # path('update/<int:pk>', views.EmployeeUpdateView.as_view() , name="update"),

    # path('register/', views.registration, name='register'),
]
