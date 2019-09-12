import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='kayqrl',
    version='0.1',
    author="Amr Kayid",
    author_email="amrkayid2027@gmail.com",
    description="Quantum Deep Reinforcement Learning Library 🕸🤖",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amrmkayid/kayqrl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
