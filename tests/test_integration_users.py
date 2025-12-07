import os
import tempfile
from core.file_singleton import FileManager


def test_integration_user_list_route(client):
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write("id,name,email\n")
            f.write("1,Amina,amina@test.com\n")

        fm = FileManager()
        fm.file_path = path
        response = client.get('/users/')
        assert response.status_code == 200
        assert b"Amina" in response.data
    finally:
        try:
            os.remove(path)
        except OSError:
            pass
