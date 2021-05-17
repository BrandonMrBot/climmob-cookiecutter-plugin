import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = ["climmob"]

tests_require = [
	"WebTest >= 1.3.1", 
	"pytest", 
	"pytest-cov"
]

setup(
    name="{{ cookiecutter.plugin_name }}",
    version="{{ cookiecutter.plugin_version }}",
    description="{{ cookiecutter.plugin_description }}",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="{{ cookiecutter.plugin_author }}",
    author_email="{{ cookiecutter.plugin_author_email }}",
    url="{{ cookiecutter.plugin_author_url }}",
    keywords="climmob plugin",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={"testing": tests_require},
    install_requires=requires,
    {%- if cookiecutter.plugin_hasCeleryTasks == "Y" or cookiecutter.plugin_hasCeleryTasks == "y" %}
    entry_points={
        "climmob.plugins": ["{{ cookiecutter.plugin_name }} = {{ cookiecutter.plugin_name }}.plugin:{{ cookiecutter.plugin_name }}"],
        "climmob.tasks": ["{{ cookiecutter.plugin_name }} = {{ cookiecutter.plugin_name }}.celerytasks"],
    },
    {%- else %}
    entry_points={"climmob.plugins": ["{{ cookiecutter.plugin_name }} = {{ cookiecutter.plugin_name }}.plugin:{{ cookiecutter.plugin_name }}"]},
    {%- endif %}
)
