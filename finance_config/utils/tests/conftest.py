import pytest

from finance_config.tracker.factories import TransactionFactory


@pytest.fixture
def transactions():
    return TransactionFactory.create_batch(20)
