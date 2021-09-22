from setuptools import setup, find_packages

setup(
    name="ciphertool",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "ciphertool = ciphertool:cli",
        ],
    },
)
