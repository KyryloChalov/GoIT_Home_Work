from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="2.3.7",
    description="Sorting folders",
    author="Kyrylo Chalov",
    author_email="ks7977166@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)