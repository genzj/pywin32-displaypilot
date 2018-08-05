import setuptools

setuptools.setup(
    name="pywin32-displaypilot",
    version="0.1.0",
    url="https://github.com/genzj/pywin32-displaypilot",

    author="genzj",
    author_email="zj0512@gmail.com",

    description="A python script sets monitor display orientation with PyWin32",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['pywin32', ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    entry_points={
        'console_scripts': [
            'pywin32-displaypilot=pywin32displaypilot.cli:entry',
        ],
    }
)
