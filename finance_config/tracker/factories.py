from datetime import datetime

import factory

from finance_config.core.models import User
from finance_config.tracker.models import Category, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Faker("email")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("name",)

    name = factory.Iterator(
        [
            "Bills",
            "Groceries",
            "Restaurants",
            "Clothing",
            "Entertainment",
            "Travel",
            "Healthcare",
            "Other",
        ]
    )


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    amount = 5
    date = factory.Faker(
        "date_between",
        start_date=datetime(year=2023, month=1, day=1).date(),
        end_date=datetime.now().date(),
    )
    type = factory.Iterator([x[0] for x in Transaction.Type.choices])
