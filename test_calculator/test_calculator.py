import json

import pytest
import yaml


def get_datas(name):
    with open("../data/test_calculator_data.yml", 'r', encoding='utf-8') as f:
        all_data = yaml.safe_load(f)
        datas = all_data[name].values()
        ids = all_data[name].keys()
        return (datas, ids)


class TestCalculator:
    @pytest.mark.parametrize('a,b,result', get_datas('add')[0],
                             ids=get_datas('add')[1])
    def test_add(self, a, b, result, calc):
        assert result == calc.add()

    @pytest.mark.parametrize('a,b,result', get_datas('sub')[0],
                             ids=get_datas('sub')[1])
    def test_sub(self, a, b, result, calc):
        assert result == calc.sub()

    @pytest.mark.parametrize('a,b,result', get_datas('mul')[0],
                             ids=get_datas('mul')[1])
    def test_mul(self, a, b, result, calc):
        assert result == calc.mul()

    @pytest.mark.parametrize('a,b,result', get_datas('div')[0],
                             ids=get_datas('div')[1])
    def test_div(self, a, b, result, calc):
        assert result == calc.div()
