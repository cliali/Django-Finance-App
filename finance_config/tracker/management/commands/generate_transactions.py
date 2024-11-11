import random
from typing import Any
from faker import Faker
from flask.config import T
from finance_config.tracker.models import Category, Transaction
from finance_config.core.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generate transactions for testing"

    def handle(self, *args: Any, **options: Any) -> str | None:
        fake = Faker()

        categories = [
            "Bills",
            "Groceries",
            "Restaurants",
            "Clothing",
            "Entertainment",
            "Travel",
            "Healthcare",
            "Other",
        ]

        for category in categories:
            Category.objects.get_or_create(name=category)

        user = User.objects.filter(username="admin").first()
        if not user:
            User.objects.create_superuser(
                username="admin",
                password="admin",
                email="admin@admin.com",
            )

        categories = Category.objects.all()
        types = list(Transaction.Type)
        for i in range(20):
            Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=random.uniform(1, 2500),
                date=fake.date_between(start_date="-1y", end_date="today"),
                type=random.choice(types),
            )
