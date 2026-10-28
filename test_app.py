import app

def test_celsius_to_fahrenheit():
    assert app.celsius_to_fahrenheit(0) == 32
    assert app.celsius_to_fahrenheit(100) == 212