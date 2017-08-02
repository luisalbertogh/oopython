# oopython
Object oriented python sample project

# Modules
A python file is a module (i.e):

oopython\oopython.py

# Packages
A package is presented here:

oopython\mypackage

It contains a module (module01.py). It requires the __init__.py file. It can import any other module/package.

# Testing
Test package is in: oopython\test

There are different files with different test suite. Each test suite contains different test cases. To launch all the tests at once:

$ python -m unittest discover test

# Generate documantation automatically

1. Install sphinx:

http://www.sphinx-doc.org/en/stable/install.html

2. Sphinx quickstart

http://www.sphinx-doc.org/en/stable/tutorial.html

$ sphinx-quickstart

3. Sphinx apidoc

http://scriptsonscripts.blogspot.com.es/2012/09/quick-sphinx-documentation-for-python.html

$ sphinx-apidoc -F -o doc src

Copy generated RST files from /doc to /source

4. Modify sys path to point to modules

- Edit conf.py under 'doc/source'
- Add the following where appropriate:
sys.path.insert(0, os.path.abspath('../../src'))

4. Build the doc

$ sphinx-build.exe -b html doc/source/ doc/build/

5. Make the html

$ cd doc
$ make html