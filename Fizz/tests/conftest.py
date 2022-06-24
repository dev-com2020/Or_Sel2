import pytest

pytest_plugins = ["Fizz.testing.fixtures"]


def pytest_runtest_setup(item):
    print("Zaczep announce", item)


@pytest.fixture(scope="function", autouse=True)
def enterexit():
    print("POCZĄTEK TESTÓW")
    yield
    print("KONIEC TESTÓW")


def pytest_addoption(parser):
    parser.addoption(
        "--upper", action="store_true",
        help="sprawdzenie użycia wielkich liter"
    )

