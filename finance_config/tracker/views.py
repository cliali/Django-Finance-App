from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from finance_config.tracker.filters import TransactionFilter
from finance_config.tracker.models import Transaction


# Create your views here.
def index(request):
    return render(request, "tracker/index.html")


@login_required
def transactions_list(request):
    transaction_filter = TransactionFilter(
        request.GET, queryset=Transaction.objects.filter(user=request.user)
    )

    context = {"filter": transaction_filter}
    if request.htmx:
        print("hi")
        return render(request, "tracker/partials/transactions-container.html", context)
    return render(request, "tracker/transactions-list.html", context)
