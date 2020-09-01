from typing import List, Dict
from functools import lru_cache

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources
import numpy as np, json
from skimage.color import rgb2lab, deltaE_ciede2000

MAX_RGB = 255.0
HIERARCHY_JSON_FILE = "color_hierarchy.json"


@lru_cache(maxsize=1)
def _get_color_data():
    hierarchy_txt = pkg_resources.read_text("static", HIERARCHY_JSON_FILE)
    color_json = json.loads(hierarchy_txt)
    rgb_values = np.array(
        [
            [c["xkcd_r"] / MAX_RGB, c["xkcd_g"] / MAX_RGB, c["xkcd_b"] / MAX_RGB]
            for c in color_json
        ]
    )
    return {
        "lab_values": rgb2lab([rgb_values]),
        "xkcd_names": [c["xkcd_color"] for c in color_json],
        "color_hierarchy": {c["xkcd_color"]: c for c in color_json},
    }


def get_color_from_rgb(rgb_color: List[float]) -> Dict:
    """ Given an array of 3 values representing an RGB color, return an object
    representing the closest color to that RGB value. Values should be numbers
    between 0-255.

    The returned value has the following keys:
    xkcd_color, xkcd_color_hex, xkcd_r, xkcd_g, xkcd_b,
    design_color, design_color_hex, design_r, design_g, design_b,
    common_color, common_color_hex, common_r, common_g, common_b,
    color_family, color_type, color_or_neutral.
    """
    assert (
        hasattr(rgb_color, "__len__") and len(rgb_color) == 3
    ), "rgb_color must be a list of 3 floats."
    assert all(
        [rgb_color[i] >= 0 and rgb_color[i] <= 255.0 for i in range(3)]
    ), "R, G, and B values must be between 0 and 255."

    rgb_color = [x / MAX_RGB for x in rgb_color]
    # scikit-image's rgb2lab wants m*n*3 arrays.
    lab = rgb2lab([[rgb_color]])[0][0]
    return get_color_from_lab(lab)


def get_color_from_lab(lab_color: List[float]) -> Dict:
    """ Given an array of 3 values representing an LAB color, return an object
    representing the closest color to that LAB value. L values should be
    between 0 and 100; A and B between -128 and 127.

    The returned value has the following keys:
    xkcd_color, xkcd_color_hex, xkcd_r, xkcd_g, xkcd_b,
    design_color, design_color_hex, design_r, design_g, design_b,
    common_color, common_color_hex, common_r, common_g, common_b,
    color_family, color_type, color_or_neutral.
    """
    color_data = _get_color_data()
    assert (
        hasattr(lab_color, "__len__") and len(lab_color) == 3
    ), "lab_color must be a list of 3 floats."
    assert lab_color[0] >= 0 and lab_color[0] <= 100, "L should be between 0 and 100."
    assert (
        lab_color[1] >= -128 and lab_color[1] <= 127
    ), "A should be between -128 and 127."
    assert (
        lab_color[2] >= -128 and lab_color[2] <= 127
    ), "B should be between -128 and 127."

    dists = np.array(
        [deltaE_ciede2000(lab_color, item) for item in color_data["lab_values"]]
    )
    xkcd_name = color_data["xkcd_names"][dists.argmin()]
    return color_data["color_hierarchy"][xkcd_name]
