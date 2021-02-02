import pytest

from calculator.calculator import Calculator


@pytest.fixture()
def calc(a, b):
    print("==========开始测试============")
    cal: Calculator = Calculator(a, b)
    yield cal
    print("!!!!!!!!!!!!!结束测试!!!!!!!!!!!!!")


def pytest_generate_tests(metafunc: "Metafunc") -> None:
    """Generate (multiple) parametrized calls to a test function."""
    if "add" in metafunc.fixturenames:
        metafunc.parametrize("add",
                             metafunc.module.adddatas,
                             ids=metafunc.module.addids,
                             scope='function')
    elif "sub" in metafunc.fixturenames:
        metafunc.parametrize("sub",
                             metafunc.module.subdatas,
                             ids=metafunc.module.subids,
                             scope='function')
    elif "mul" in metafunc.fixturenames:
        metafunc.parametrize("mul",
                             metafunc.module.muldatas,
                             ids=metafunc.module.mulids,
                             scope='function')
    elif "div" in metafunc.fixturenames:
        metafunc.parametrize("div",
                             metafunc.module.divdatas,
                             ids=metafunc.module.divids,
                             scope='function')


def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    """Register argparse-style options and ini-style config values,
    called once at the beginning of a test run.

    .. note::

        This function should be implemented only in plugins or ``conftest.py``
        files situated at the tests root directory due to how pytest
        :ref:`discovers plugins during startup <pluginorder>`.

    :param _pytest.config.argparsing.Parser parser:
        To add command line options, call
        :py:func:`parser.addoption(...) <_pytest.config.argparsing.Parser.addoption>`.
        To add ini-file values call :py:func:`parser.addini(...)
        <_pytest.config.argparsing.Parser.addini>`.

    :param _pytest.config.PytestPluginManager pluginmanager:
        pytest plugin manager, which can be used to install :py:func:`hookspec`'s
        or :py:func:`hookimpl`'s and allow one plugin to call another plugin's hooks
        to change how command line options are added.

    Options can later be accessed through the
    :py:class:`config <_pytest.config.Config>` object, respectively:

    - :py:func:`config.getoption(name) <_pytest.config.Config.getoption>` to
      retrieve the value of a command line option.

    - :py:func:`config.getini(name) <_pytest.config.Config.getini>` to retrieve
      a value read from an ini-style file.

    The config object is passed around on many internal objects via the ``.config``
    attribute or can be retrieved as the ``pytestconfig`` fixture.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')
