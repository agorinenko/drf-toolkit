import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drf_toolkit",
    version="0.0.14",
    author="Gorinenko Anton",
    author_email="anton.gorinenko@gmail.com",
    description="Django rest framework toolkit",
    long_description=long_description,
    keywords='python, drf, django rest framework, toolkit, utils',
    long_description_content_type="text/markdown",
    url="https://github.com/agorinenko/drf-toolkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2'
    ],
    install_requires=[
        'try-parse',
        'power-dict',
        'djangorestframework',
        "django>=2.2"
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.7',
)
