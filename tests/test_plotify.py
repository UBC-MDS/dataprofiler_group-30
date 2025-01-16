from dataprofiler.dataprofiler import plotify
import pytest

def test_wrong_input():
    with pytest.raises(TypeError):
        plotify(123)
        plotify('abcd')
        
