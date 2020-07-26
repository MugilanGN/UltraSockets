import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ultra_sockets",
    version="1.0.4",
    author="Mugilan Ganesan",
    author_email="mugi.ganesan@gmail.com",
    description="Protocol to provide fast and light communication between devices over (W)LAN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MugilanGN/UltraSockets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires='>=3.4',
)
