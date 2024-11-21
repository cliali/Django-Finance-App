from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from finance_config.tracker.models import Category, Transaction


class TransactionResource(resources.ModelResource):
    category = fields.Field(
        attribute="category",
        column_name="category",
        widget=ForeignKeyWidget(Category, field="name"),
    )

    def after_init_instance(self, instance, new, row, **kwargs):
        instance.user = kwargs.get("user")

    class Meta:
        model = Transaction
        fields = ("amount", "type", "date", "category")
        import_id_fields = ("amount", "type", "date", "category")
