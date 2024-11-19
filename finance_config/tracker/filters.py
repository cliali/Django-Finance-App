import django_filters
from django import forms

from .models import Category, Transaction


class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.ChoiceFilter(
        choices=Transaction.Type,
        field_name="type",
        lookup_expr="iexact",
        empty_label="Any",
    )

    start_date = django_filters.DateFilter(
        field_name="date",
        lookup_expr="gte",
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date From",
    )

    end_date = django_filters.DateFilter(
        field_name="date",
        lookup_expr="lte",
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date To",
    )

    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Transaction
        fields = ("transaction_type", "start_date", "end_date", "category")
