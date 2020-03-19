
print("-----------------------01")
def multiply(a,b):
    return a * b

def setup_module(module):
    print("--setup_module")

def teardown_module(module):
    print("--teardown_module")

def setup_function(function):
    print("--setUp_function")

def teardown_function(function):
    print("--teardown_function")

def setup():
    print("--setup")

def teardown():
    print("--teardown")


def test_mutiply_3_4():
    print("--test_mutiply_3_4")
    assert multiply(3,4) == 12

def test_mutiply_a_3():
    print("--test_mutiply_a_3")
    assert multiply("a",3) == "aaa"