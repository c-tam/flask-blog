import setuptools

setuptools.setup(
    name="c-tam",
    version="0.1",
    author="Charles Tam",
    description="A simple flask blog",
    url="https://github.com/c-tam/flask-blog",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    license="MIT",
    install_requires=(
        "Click>=7.0",
        "Flask>=1.1.1",
        "Flask-Login>= 0.4.1",
        "Flask-SQLAlchemy>=2.4.1",
        "itsdangerous>=1.1.0",
        "Jinja2>=2.10.3",
        "MarkupSafe>=1.1.1",
        "pip>=19.3.1",
        "setuptools>=41.2.0",
        "SQLAlchemy>=1.3.10",
        "Werkzeug>=0.16.0",
    ),

)