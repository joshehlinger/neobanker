import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='neobanker',
    version="0.0.1",
    author="Joshua Ehlinger",
    install_requires=open('requirements.txt').read(),
    description='Collects neointerest',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshehlinger/neobanker",
    py_modules=['banker'],
    entry_points={
        'console_scripts': [
            'neobanker = banker:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
