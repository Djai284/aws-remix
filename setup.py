from setuptools import setup, find_packages

setup(
    name="aws-remix",
    version="0.1.0",
    description="AWS Remix: A CLI tool to generate comprehensive summaries of AWS accounts.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "typer",
        "pyyaml",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "aws-remix=aws_remix.cli:app",
        ],
    },
)
