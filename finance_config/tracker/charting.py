import plotly.express as px
from django.db.models import Sum

from finance_config.tracker.models import Category


def plot_income_expenses_chart(qs):
    x_vals = ["Income", "Expenditure"]

    total_income = qs.get_total_income()
    total_expenses = qs.get_total_expenses()

    fig = px.bar(x=x_vals, y=[total_income, total_expenses])
    return fig


def plot_category_pie_chart(qs):
    count_per_category = (
        qs.order_by("category").values("category").annotate(total=Sum("amount"))
    )

    category_pks = count_per_category.values_list("category", flat=True).order_by(
        "category"
    )
    categories = (
        Category.objects.filter(pk__in=category_pks)
        .order_by("pk")
        .values_list("name", flat=True)
    )
    total_amount = count_per_category.order_by("category").values_list(
        "total", flat=True
    )

    fig = px.pie(values=total_amount, names=categories)
    fig.update_layout(title_text="Total Amount per Category")
    return fig
