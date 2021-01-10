from setuptools import setup, find_packages

setup(
    name="modulo_instalavel",
    version="0.1.0",
    description="Delivery app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
)