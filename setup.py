import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('version.txt', 'r', encoding='utf-8') as vf:
    version = vf.read()

with open("requirements.txt") as f:
    requirements = f.read().split("\n")

setuptools.setup(
    name="dpextras",
    version=version,
    author="kcomain",
    author_email="me@kcomain.dev",
    description="utility extension for discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kcomain/dpextras",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    packages=['discord.ext.extras'],
    # packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
