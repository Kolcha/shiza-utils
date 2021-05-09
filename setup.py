import setuptools

setuptools.setup(
    name="shiza-utils",
    version="0.2.0",
    author="Nick Korotysh",
    author_email="kolchaprogrammer@list.ru",
    description="download torrents from shiza-project.com",
    url="https://github.com/Kolcha/shiza-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    python_requires='>=3.6',
)
