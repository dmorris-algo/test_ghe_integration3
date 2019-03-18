from . import test_ghe_integration3

def test_test_ghe_integration3():
    assert test_ghe_integration3.apply("Jane") == "hello Jane"
