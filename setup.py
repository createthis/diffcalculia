from setuptools import setup

setup(
    name="diffcalculia",
    version="0.1.0",
    description="Tool to help AIs generate valid unified diffs for patching files",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/createthis/diffcalculia",
    author="Createthis",
    license="MIT",
    py_modules=["diffcalculia"],
    entry_points={
        "console_scripts": [
            "diffcalculia=diffcalculia:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Version Control",
    ],
)