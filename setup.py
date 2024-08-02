from setuptools import setup, find_packages

setup(
    name='my_latex_compiler',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my_latex_compiler=my_latex_compiler.app:main',
        ],
    },
    author='Abhoy Sarkar',
    author_email='sarkar.ab07@gmail.com.com',
    description='A LaTeX compilation service using Flask and Docker',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/abhoy21/latex_api.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
