from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from finance_config.tracker.models import Category, Transaction


class TransactionResource(resources.ModelResource):
    category = fields.Field(
        attribute="category",
        column_name="category",
        widget=ForeignKeyWidget(Category, field="name"),
    )

    class Meta:
        model = Transaction
        fields = ("amount", "type", "date", "category")
