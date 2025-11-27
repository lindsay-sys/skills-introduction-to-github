from django.urls import path
from . import views 

urlpatterns = [
  path("", views.index, name='index'),


  path("tenders/", views.tender_list, name="tender_list"),
  path("tenders/create/", views.create_tender, name="create_tender"),
  path("tenders/<int:tender_id>/edit/", views.edit_tender, name="edit_tender"),



  path("contact/", views.contact,  name="contact"),
  path("reports/", views.reports, name="reports"),

  
  path("suppliers/", views.suppliers, name="suppliers"),


  path("login/", views.login_view, name="login"),
  path("register/", views.register_view, name="register"),
  path("logout/", views.logout_view, name="logout"),
]