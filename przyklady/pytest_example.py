def save_to_file(filepath, content):
    with open(filepath, "w") as f:
        f.write(content)

def test_save_to_file(tmp_path):
    filepath = tmp_path / "test.txt"
    save_to_file(filepath, "Hello, World!")

    with open(filepath, "r") as f:
        assert f.read() == "Hello, World!"