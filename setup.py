from setuptools import setup, find_packages

setup(
    name='MolR',
    version='0.1.0',
    author='Hongwei Wang, Weijiang Li, Xiaomeng Jin, Kyunghyun Cho, Heng Ji, Jiawei Han, Martin Burke',
    author_email='{hongweiw@illinois.edu',
    description='Chemical-Reaction-Aware Molecule Representation Learning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hwwang55/MolR',
    packages=find_packages(include=['MolR', 'MolR.*']),
    include_package_data=True,
    install_requires=[
        'torch==1.8.1',
        'dgl-cu110==0.6.1',
        'pysmiles==1.0.1',
        'scikit-learn==0.24.2',
        'networkx==2.5.1',
        'matplotlib==3.4.2',
        'openbabel-wheel',
        'scipy==1.7.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    package_data={
        'MolR': ['models/**/*']
    },
)