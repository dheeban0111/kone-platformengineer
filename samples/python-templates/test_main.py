from main import greet

def test_greet():
    assert greet("Kone") == "Hello, Kone!"
    assert greet() == "Hello, Platform Engineer!"
