from setuptools import setup, find_packages

setup(
    name="greenlix-cv-screener",
    version="2.0.0",
    author="Greenlix Technologies",
    author_email="contact@greenlix.com",
    description="AI-powered CV screening system with accurate keyword matching",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/greenlix-tech/cv-screening",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyMuPDF>=1.23.0",
        "pandas>=2.0.0",
        "openpyxl>=3.1.0",
        "tqdm>=4.66.0",
    ],
    entry_points={
        "console_scripts": [
            "cv-screener=cv_screener:main",
        ],
    },
)