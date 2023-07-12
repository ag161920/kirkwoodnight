from setuptools import setup, find_packages

def get_requires():
    reqs = []
    for line in open("requirements.txt", "r").readlines():
        reqs.append(line)
    return reqs

setup(
    name="kirkwoodnight",
    version="0.1",
    packages=find_packages(),

    # Metadata
    author="Your Name",
    author_email="your-email@example.com",
    description="kirkwoodnight allows you to plan your Kirkwood observations in just minutes!",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="Link to your project",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python :: 3.10",
    ],

    # Specify console scripts
    entry_points={
        'console_scripts': [
            'kirkwoodnight = kirkwoodnight:main',
        ],
    },

    # Include additional files into the package
    package_data={'': ['obj_list.csv']},

    install_requires= get_requires(),
)
