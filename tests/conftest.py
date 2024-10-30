import pytest
from faker import Faker

faker = Faker()

def pytest_addoption(parser):
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of test records"
    )

@pytest.fixture
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture
def generate_test_data(num_records):
    test_data = []
    for _ in range(num_records):
        a = faker.random_number(digits=2)
        b = faker.random_number(digits=2)
        operation = faker.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
        test_data.append((a, b, operation))
    return test_data