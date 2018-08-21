from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_panel, name="landing-panel"),
    path('user-panel/', views.user_panel, name="user-panel"),
    path('items-panel/', views.items_panel, name="items-panel"),
    path('actions-panel/', views.actions_panel, name="actions-panel"),
    path('actions-panel/modify', views.modify_reservations, name="modify_reservations"),
    path('items-panel/create', views.create_item, name="create_item"),
    path('items-panel/delete', views.delete_item, name="delete_item"),
    path('actions-panel/changeloans', views.changeloans, name="change_loans")
]
