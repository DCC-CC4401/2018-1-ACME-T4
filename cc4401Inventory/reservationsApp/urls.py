from django.urls import path
from . import views

urlpatterns = [
    path('<int:reservation_id>', views.reservation_data, name='reservation_data'),
    path('delete/', views.delete, name='delete_reservation'),
    path('cancel/', views.cancel, name='cancel_reservation'),
]
