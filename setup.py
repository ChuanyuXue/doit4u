from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="doit4u",
    version="0.1.0",
    author="Chuanyu Xue",
    author_email="skewcy@gmail.com",
    description="A natural language hybrid Python programming framework based on OpenAI API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChuanyuXue/doit4u",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
    install_requires=[
        "openai",
    ],
)