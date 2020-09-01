import pytest
from colornamer import get_color_from_rgb

def test_black():
    results = get_color_from_rgb([0, 0, 0])
    assert results['xkcd_color'] == 'black'
    assert results['design_color'] == 'black'
    assert results['common_color'] == 'black'
    assert results['color_family'] == 'black'
    assert results['color_type'] == 'dark neutral'
    assert results['color_or_neutral'] == 'neutral'

def test_blue():
    results = get_color_from_rgb([0, 0, 255])
    assert results['xkcd_color'] == 'primary blue'
    assert results['design_color'] == 'ultramarine blue'
    assert results['common_color'] == 'cobalt blue'
    assert results['color_family'] == 'blue'
    assert results['color_type'] == 'saturated color'
    assert results['color_or_neutral'] == 'color'

def test_errors():
    with pytest.raises(AssertionError):
        get_color_from_rgb('fooo')
    with pytest.raises(AssertionError):
        get_color_from_rgb(123)
