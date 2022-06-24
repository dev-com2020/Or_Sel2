import pytest


@pytest.fixture(scope="class")
def provide_current_time(request):
    import datetime
    request.cls.now = datetime.datetime.now()
    print("\nWejście do klasy...")
    yield
    print("\nWyjście z klasy...")


def test_mnozenie(random_number_gen):
    a = random_number_gen()
    print("\nliczba wylosowania:", a)
    b = 10
    assert a * b >= 10


@pytest.mark.usefixtures("provide_current_time")
class TestMultiple:

    # @pytest.mark.usefixtures("greetings")
    def test_dodawanie(self):
        print("Data rozpoczęcia: ", self.now)
        a = 5
        b = 10
        assert a + b == 11

    def test_odejmowanie(self):
        print("Data rozpoczęcia: ", self.now)
        a = 10
        b = 1
        assert a - b == 9
