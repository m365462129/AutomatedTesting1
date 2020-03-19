import pytest
import conftest


@click.command
@click.option("-m",default=None,help="输入运行模式：run或debug")
def run(m):
    if m is None or m == "run":
        pass
    elif m == "debug":
        pass


# if __name__ == '__main__':
#     #
#     pytest.main(['-s', './test_case/test_baidu.py'])

