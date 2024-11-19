from datetime import datetime, timedelta

import pytest
from django.urls import reverse

from finance_config.tracker.models import Category


@pytest.mark.django_db
def test_total_values_appear_on_list_page(user_transactions, client):
    user = user_transactions[0].user
    client.force_login(user)

    income_total = sum(t.amount for t in user_transactions if t.type == "income")
    expense_total = sum(t.amount for t in user_transactions if t.type == "expense")
    net = income_total - expense_total

    response = client.get(reverse("tracker:transactions-list"))
    assert response.context["total_income"] == income_total
    assert response.context["total_expenses"] == expense_total
    assert response.context["net_income"] == net


@pytest.mark.django_db
def test_transaction_type_filter(user_transactions, client):
    user = user_transactions[0].user
    client.force_login(user)

    GET_params = {"transaction_type": "income"}
    response = client.get(reverse("tracker:transactions-list"), GET_params)

    qs = response.context["filter"].qs

    for transaction in qs:
        assert transaction.type == "income"

    GET_params = {"transaction_type": "expense"}
    response = client.get(reverse("tracker:transactions-list"), GET_params)

    qs = response.context["filter"].qs

    for transaction in qs:
        assert transaction.type == "expense"


@pytest.mark.django_db
def test_start_end_date_filter(user_transactions, client):
    user = user_transactions[0].user
    client.force_login(user)

    start_date_cutoff = datetime.now().date() - timedelta(days=120)
    GET_params = {"start_date": start_date_cutoff}
    response = client.get(reverse("tracker:transactions-list"), GET_params)

    qs = response.context["filter"].qs

    for transaction in qs:
        assert transaction.date >= start_date_cutoff

    end_date_cutoff = datetime.now().date() - timedelta(days=20)
    GET_params = {"end_date": end_date_cutoff}
    response = client.get(reverse("tracker:transactions-list"), GET_params)

    qs = response.context["filter"].qs

    for transaction in qs:
        assert transaction.date <= end_date_cutoff


@pytest.mark.django_db
def teat_category_filter(user_transactions, client):
    user = user_transactions[0].user
    client.force_login(user)

    category_pks = Category.objects.all()[:2].values_list("pk", flat=True)
    GET_params = {"category": category_pks}
    response = client.get(reverse("tracker:transactions-list"), GET_params)

    qs = response.context["filter"].qs

    for transaction in qs:
        assert transaction.category.pk in category_pks
