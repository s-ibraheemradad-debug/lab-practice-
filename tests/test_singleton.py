from core.file_singleton import FileManager


def test_singleton_file_manager():
    f1 = FileManager()
    f2 = FileManager()
    assert f1 is f2
