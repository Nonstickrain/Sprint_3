import pytest
import random

@pytest.fixture()
def valid_registration():
    correct_data = ['Alabama', 'artyomtimonin'+str(random.randint(0, 999))+'@mail.ru', str(random.randint(1000000, 999999999))]

    return correct_data
@pytest.fixture()
def invalid_registration_due_to_password():
    invalid_password_data = ['Alabama', 'artyomtimonin'+str(random.randint(0, 999))+'@mail.com', str(random.randint(0, 99999))]

    return invalid_password_data
@pytest.fixture()
def account():
    test_account = ['artyomtimonin200@mail.ru', 'At0987654321']

    return test_account


