import pytest
# pip install pytest

def add(a, b):
    return a + b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def test_add():
    assert add(1, 2) == 3


def square_list(l):
    return [x**2 for x in l]


def greet():
    name = input("Enter your name: ")
    return f"Hello, {name}!"

def save_to_file(filepath, content):
    with open(filepath, "w") as f:
        f.write(content)


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (-1, 1, 0)])
def test_add_2(a, b, expected):
    assert add(a, b) == expected


def test_div_raise_value_error_when_b_is_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        div(1, 0)


@pytest.fixture
def data():
    return [1, 2, 3]

def test_square_list(data):
    assert square_list(data) == [1, 4, 9]
    assert square_list([-1, 1]) == [1, 1]


def test_greet(mocker):
    mocker.patch("builtins.input", return_value="John")
    assert greet() == "Hello, John!"


def test_save_to_file(tmp_path):
    filepath = tmp_path / "test.txt"
    save_to_file(filepath, "Hello, World!")
    assert filepath.read_text() == "Hello, World!"

    with open(filepath, "r") as f:
        assert f.read() == "Hello, World!"

