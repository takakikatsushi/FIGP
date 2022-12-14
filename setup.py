from setuptools import setup, find_packages
#from os.path import basename, splittext
#from glob import glob

def _requirement_packages(filename):
	return open(filename).read().splitlines()

setup(
	name="figp",
	version="0.1.0",
	license="Creative Commons Attribution 4.0 International License",
	description="Symbolic regression with FIGP",
	author="Katsushi Takaki",
	url="https://github.com/takakikatsushi/FIGP",
	packages=find_packages("src"), # detect python packages in the codes
	package_dir={"":"src"},
	#py_modules=[splittext(basename(path))[0] for path in glob('src/fgpnls/*.py')]
	zip_safe=False,
	install_requires=_requirement_packages("requirements.txt")
)
