import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='neobanker',
    install_requires=open('requirements.txt').read(),
    description='Collects neointerest',
    long_description=long_description,
    py_modules=['neobanker'],
    entry_points={
        'console_scripts': [
            'neobanker = neobanker:main'
        ]
    }
)
