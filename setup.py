from setuptools import setup, find_packages


version = '0.0.1'


install_requires = (
    'djangorestframework>=2.3.13,<3',
)

setup(
    name='incuna-event-api',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='',
    long_description='',
    author='Incuna',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/incuna-event-api/',
    install_requires=install_requires,
    zip_safe=False,
)
