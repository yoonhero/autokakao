import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autokakao",
    version="0.0.3",
    author="Yoonhero",
    author_email="yoonhero06@naver.com",
    description="A Simple Kakaotalk Automation Wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoonhero/autokakao",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)