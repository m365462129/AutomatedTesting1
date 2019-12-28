import pytest

def intc(x):
    return x+1

def test_answer():
    assert intc(3) == 5

if __name__ == "__main__":
    pass
    # pytest.main()
#  if __name__ == "__main__":
#     pytest.main()