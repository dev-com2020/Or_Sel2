def myapp():
    print("Aplikacja została uruchomiona")


def test_capsys(capsys):
    myapp()
    out, err = capsys.readouterr()
    assert out == "Aplikacja została uruchomiona\n"

