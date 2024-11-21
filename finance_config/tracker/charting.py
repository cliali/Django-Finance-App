import plotly.express as px


def plot_income_expenses_chart(qs):
    x_vals = ["Income", "Expenditure"]

    total_income = qs.get_total_income()
    total_expenses = qs.get_total_expenses()

    fig = px.bar(x=x_vals, y=[total_income, total_expenses])
    return fig
