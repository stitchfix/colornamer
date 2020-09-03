from setuptools import setup, find_packages

setup(
    name="colornamer",
    version="0.1.3",
    description="Given a color, return a hierarchy of names.",
    long_description="Turns an RGB or LAB point into a hierarchical list of "
        "names: color family, common color, design color, and xkcd color, as "
        " well as color type and color-or-neutral. See "
        "https://github.com/stitchfix/colornamer/ or "
        "https://multithreaded.stitchfix.com/blog/2020/09/02/what-color-is-this/ "
        "for more details.",
    url="https://github.com/stitchfix/colornamer",
    packages=find_packages(),
    package_data={"static": ["color_hierarchy.json", "color_hierarchy.csv"],},
    install_requires=["importlib_resources", "numpy", "scikit-image",],
    python_requires=">=3.6",
    author="Dan Tasse",
    author_email="dan.tasse@stitchfix.com"
)
