from django.urls import path

from . import views

app_name = "tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("transactions", views.transactions_list, name="transactions-list"),
    path("transactions/create", views.create_transaction, name="create-transaction"),
]
