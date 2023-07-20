from django.urls import path
from .views import ItemView, OrderView, CustomerView, BillView

urlpatterns = [
    path('items/', ItemView.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<int:customer_id>/', OrderView.as_view()),
    path('orders/<int:customer_id>/<int:item_id>/', OrderView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('customer/<int:pk>/', CustomerView.as_view()),
    path('bill/<int:customer_id>/', BillView.as_view()),
]