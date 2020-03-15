import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='appl',
    version='0.1',
    scripts=['appl-init'],
    author="Ergin Soysal",
    author_email="esoysal@gmail.com",
    description="Application framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soysal/appl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)