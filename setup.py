from setuptools import setup, find_packages

setup(
    name="pointnet_pytorch", 
    version="0.1",  
    packages=find_packages(),  
    install_requires=[

    ],
    description="Pointnet Pytorch implementation",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[  
    ],
    python_requires='>=3.6',  
)
