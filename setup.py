from setuptools import setup

setup(
    name='cli_click',
    version='0.1.0',
    py_modules=['cli_click'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cli_click = cli_click:click_main',
        ],
    },
)