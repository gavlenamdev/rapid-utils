from setuptools import find_packages, setup

setup(
    name="rapid-utils",
    version="0.0.2",
    description="high level functions",
    url="https://github.com/gnaam/rapid-utils",
    author="Namdev Gavle",
    author_email="gavlenamdevprabha@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests==2.22.0"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)