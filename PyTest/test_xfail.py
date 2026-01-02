import pytest
import func as f

@pytest.mark.xfail(reason="devide by 0 not handled",strict=True)
@pytest.mark.parametrize("a,b,res",[(2,0,0)])
def test_div(a,b,res):
    assert f.div(a,b) == res, "Not correct"