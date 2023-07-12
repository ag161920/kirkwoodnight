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
    description="A short description of your project",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="Link to your project",
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
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