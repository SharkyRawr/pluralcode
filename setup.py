import setuptools

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="pluralcode", # Replace with your own username
    version="0.0.1",
    author="Sophie Luna Schumann",
    author_email="me@sophie.lgbt",
    description="WIP Pluralcode library",
#   long_description=long_description,
#   long_description_content_type="text/markdown",
    url="https://git.catgirl.biz/pluralcode/pypluralcode",
    project_urls={
        "Bug Tracker": "https://git.catgirl.biz/pluralcode/pypluralcode/-/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Religion",
        "Topic :: Sociology",
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)