from setuptools import setup, find_packages

with open('django_fieldbustier/version.py', 'r') as fp:
    g = {}
    exec(fp.read(), g)
    version = g['__version__']

packages = find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests'])

def readme():
    with open('README.md', 'r') as fp:
        return fp.read()

setup(
    name='django-fieldbustier',
    version=version,
    description='A package that allows modifying a model of any django app from the outside, without modifying the code of the app itself.',
    author='MrJmad',
    author_email='j-mad@j-mad.com',
    license='MIT License',
    url='https://github.com/mrjmad/django-fieldbustier',
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords='',
    packages=['django_fieldbustier'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
