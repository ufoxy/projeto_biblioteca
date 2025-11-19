from database.connection import get_db

def test_connection():
    db = get_db()
    assert db is not None
