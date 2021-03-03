import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="py-ccloud",
    version="0.0.1",
    scripts=["pyccloud"],
    author="Pawel Dudzinski",
    author_email="pawel.dudzinski@saucelabs.com",
    description="Simple Python library wrapping the Confluent Cloud CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saucelabs/py-ccloud",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
    install_requires=[
        "executor==23.2"
    ]
 )
