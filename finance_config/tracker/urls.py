from django.urls import path

from . import views

app_name = "tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("transactions/", views.transactions_list, name="transactions-list"),
    path("transactions/create/", views.create_transaction, name="create-transaction"),
    path("transactions/charts/", views.transactions_charts, name="transactions-charts"),
    path("transactions/export/", views.export, name="export"),
    path(
        "transactions/<int:pk>/update/",
        views.update_transaction,
        name="update-transaction",
    ),
    path(
        "transactions/<int:pk>/delete/",
        views.delete_transaction,
        name="delete-transaction",
    ),
    path("get_transactions/", views.get_transaction, name="get-transaction"),
]
