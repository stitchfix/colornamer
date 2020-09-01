from setuptools import setup, find_packages

setup(
    name="colornamer",
    version="0.1.2",
    description="Given a color, return a hierarchy of names.",
    url="https://github.com/stitchfix/colornamer",
    packages=find_packages(),
    package_data={"static": ["color_hierarchy.json", "color_hierarchy.csv"],},
    install_requires=["importlib_resources", "numpy", "scikit-image",],
    python_requires=">=3.6",
)
