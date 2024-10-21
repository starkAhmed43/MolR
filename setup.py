import sys
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

python_version = f"{sys.version_info.major}{sys.version_info.minor}"
dgl_wheel_url = None
if python_version == "310":
    dgl_wheel_url = "https://data.dgl.ai/wheels/torch-2.4/cu118/dgl-2.4.0%2Bcu118-cp310-cp310-manylinux1_x86_64.whl"
elif python_version == "311":
    dgl_wheel_url = "https://data.dgl.ai/wheels/torch-2.4/cu118/dgl-2.4.0%2Bcu118-cp311-cp311-manylinux1_x86_64.whl"
elif python_version == "38":
    dgl_wheel_url = "https://data.dgl.ai/wheels/torch-2.4/cu118/dgl-2.4.0%2Bcu118-cp38-cp38-manylinux1_x86_64.whl"
elif python_version == "39":
    dgl_wheel_url = "https://data.dgl.ai/wheels/torch-2.4/cu118/dgl-2.4.0%2Bcu118-cp39-cp39-manylinux1_x86_64.whl"

if dgl_wheel_url:
    requirements.append(f"dgl @ {dgl_wheel_url}")

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
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    package_data={
        'MolR': ['models/**/*']
    },
)