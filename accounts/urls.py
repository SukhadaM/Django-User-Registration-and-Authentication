from django.urls import path
from  . import views

app_name='accounts'

urlpatterns = [
    path('',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    path('dashboardprofile/',views.dashboardprofile,name="dashboard-profile"),
    # path('editprofile/',views.editprofile,name="edit-profile"),
    path('changeemail/',views.changeemail,name="change-email"),
    path('changeusername/',views.changeusername,name="change-username"),
    path('changeaddress/',views.changeaddress,name="change-address"),
    path('deleteprofile/',views.deleteprofile,name="delete-profile"),
    
]