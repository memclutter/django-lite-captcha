import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lite_captcha',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2',  # example license
    description='Lite captcha for django projects.',
    url='https://github.com/memclutter/django-lite-captcha',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Memory Clutter',
    author_email='memclutter@gmail.com',
    install_requires=['captcha==0.2.4',
                      'Pillow==8.1.1'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)