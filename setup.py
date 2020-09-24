import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logic-lnker-riledigital",  # Replace with your own username
    version="0.0.1",
    author="Ri Le",
    author_email="rl2999@columbia.edu",
    description="A utility to quickly symlink files for Logic Pro X on Mac OS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Mac OS",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        logiclnker=LogicLnker:run
    """,
)
