from setuptools import setup, find_packages  # type: ignore

setup(
    name="metodosord",
    version="0.1.0",
    author="Sherlin y julian",
    author_email="28145az@gmail.com",
    description="Contiene varios métodos de ordenamiento",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sherlinwiii/metodosord",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

