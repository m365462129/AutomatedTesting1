


def multiply(a,b):
    return a+b

def setUp_module(module):
    print("setUp_module")

def teardown_module(module):
    print("teardown_module")

def setUp_function(module):
    print("setUp_function")

def teardown_function(module):
    print("teardown_function")

def setUp(module):
    print("setUp")

def teardown(module):
    print("teardown")


def test_mutiply_3_4():
    assert multiply(3,4)==12