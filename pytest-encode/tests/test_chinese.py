import pytest


@pytest.mark.parametrize("name", ['有才', '唐伯虎'])
def test(name):
    print(name)