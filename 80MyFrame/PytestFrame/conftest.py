import pytest

run_list = [
    "./test_case/test_baidu.py",
    "./test_case/test_51job.py",
]



# 设置测试钩子
@pytest.fixture()
def test_url():
    return "http://www.baidu.com"




