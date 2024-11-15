import django_filters
from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.ChoiceFilter(
        choices=Transaction.Type,
        field_name="type",
        lookup_expr="iexact",
        empty_label="Any",
    )

    class Meta:
        model = Transaction
        fields = ("transaction_type",)