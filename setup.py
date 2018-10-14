import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-lite-captcha',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2',  # example license
    description='Lite captcha for django projects.',
    url='https://github.com/memclutter/django-lite-captcha',
    long_description=README,
    author='Memory Clutter',
    author_email='memclutter@gmail.com',
    install_requires=['captcha==0.2.4',
                      'Pillow==5.3.0'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.x',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)