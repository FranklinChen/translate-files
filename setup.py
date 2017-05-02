from setuptools import setup, find_packages
setup(
    name='translate-files',
    version='1.0',
    py_modules=['translate_files'],
    install_requires=[
        'click',
        'google-api-python-client',
    ],
    entry_points={
        'console_scripts': ['translate-files=translate_files:main'],
    },
    author='Franklin Chen',
    author_email='franklinchen@franklinchen.com',
    description='Translate text files using Google Translate',
    license='BSD',
    keywords='translate',
    url='https://github.com/TalkBank/translate-files',
)
