import setuptools


setuptools.setup(
    name="py-ccloud",
    version="0.1.1",
    author="Pawel Dudzinski",
    author_email="pawel.dudzinski@saucelabs.com",
    description="Simple Python library wrapping the Confluent Cloud CLI",
    long_description="Simple Python library wrapping the Confluent Cloud CLI",
    long_description_content_type="text/markdown",
    url="https://github.com/saucelabs/py-ccloud",
    py_modules=["ccloud"],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
    install_requires=[
        "executor==23.2"
    ]
 )
