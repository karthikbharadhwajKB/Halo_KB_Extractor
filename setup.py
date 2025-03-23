from setuptools import setup, find_packages

setup(
    name="halo_kb_extractor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "python-dotenv>=1.0.0",
    ],
    entry_point={
        "console_script": [
            "halo-kb-extract=halo_kb_extractor.main:main", 
        ]
    },
    author="Karthik Kolluri",
    author_email="karthik.kolluri@gmail.com",
    description="A tool to extract knowledge Base articles from Halo PSA"
)