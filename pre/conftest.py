import pytest

@pytest.fixture(scope="session", autouse=True)
def greetings():
    print("Witaj")
    yield
    print("Żegnaj")

@pytest.fixture
def random_number_gen():
    import random
    def _number_provider():
        return random.choice(range(10))
    yield _number_provider


def test_temp(tmp_path):
    f = tmp_path / "file.txt"
    print("PLIK: ", f)

    f.write_text("Witaj świecie!")
    fread = tmp_path / "file.txt"
    assert fread.read_text() == "Witaj świecie!"


