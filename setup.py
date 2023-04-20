import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    setuptools.setup(
        name="labeler",
        version="0.0.1",
        author="",
        author_email="",
        description="Anthropomophization labeler",
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        python_requires=">=3.10",
    )
