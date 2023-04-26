from os.path import exists

from setuptools import find_packages
from setuptools import setup

setup(
    name="django-tenants-schemas",
    author="Adam Birds",
    author_email="adam.birds@adbwebdesigns.co.uk",
    packages=find_packages(),
    scripts=[],
    url="https://github.com/adambirds/django-tenants-schemas",
    license="MIT",
    description="Tenant support for Django using PostgreSQL schemas.",
    long_description=open("README.rst").read() if exists("README.rst") else "",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=["Django>=2.2", "ordered-set", "psycopg2-binary", "six"],
    setup_requires=["setuptools-scm"],
    version="1.0.0",
    zip_safe=False,
)
