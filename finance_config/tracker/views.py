from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django_htmx.http import retarget

from finance_config.tracker.filters import TransactionFilter
from finance_config.tracker.forms import TransactionForm
from finance_config.tracker.models import Transaction


# Create your views here.
def index(request):
    return render(request, "tracker/index.html")


@login_required
def transactions_list(request):
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related(
            "category"
        ),
    )

    total_income = transaction_filter.qs.get_total_income()
    total_expenses = transaction_filter.qs.get_total_expenses()
    context = {
        "filter": transaction_filter,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_income": total_income - total_expenses,
    }
    if request.htmx:
        return render(request, "tracker/partials/transactions-container.html", context)
    return render(request, "tracker/transactions-list.html", context)


@login_required
def create_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            context = {"message": "transaction was added successfully"}
            return render(request, "tracker/partials/transaction-success.html", context)
        else:
            context = {"form": form}
            response = render(
                request, "tracker/partials/create-transaction.html", context
            )
            return retarget(response, "#transaction-block")

    context = {"form": TransactionForm()}
    return render(request, "tracker/partials/create-transaction.html", context)


@login_required
def update_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            context = {"message": "transaction was updated successfully!"}
            return render(request, "tracker/partials/transaction-success.html", context)
        else:
            context = {"form": form, "transaction": transaction}
            response = render(
                request, "tracker/partials/update-transaction.html", context
            )
            return retarget(response, "#transaction-block")

    context = {
        "form": TransactionForm(instance=transaction),
        "transaction": transaction,
    }
    return render(request, "tracker/partials/update-transaction.html", context)


@login_required
@require_http_methods(["DELETE"])
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    transaction.delete()
    context = {
        "message": f"Transaction of {transaction.amount} on {transaction.date} was deleted successfully!"
    }
    return render(request, "tracker/partials/transaction-delete.html", context)
