import pytest
import func as f

@pytest.mark.parametrize('a,b,expected_value',
                         [
                             (1,2,3),(2,3,6),(1,7,8)
                         ]
                         )
def test_add(a,b,expected_value):
    assert f.add_num(a,b) == expected_value, "Addition is wrong"
