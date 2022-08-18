# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Safire Engine'
copyright = '2022, TwoBitMachines'
author = 'TwoBitMachines'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['rst2pdf.pdfbuilder']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def setup(app):
    app.add_css_file('custom.css')


pdf_documents = [('index', u'Safire Engine',
                  u'Safire Engine Documentation', u'Two Bit Machines'), ]


# 1. Install rst2pdf
#     - use your package manager (or)
#     - pip install rst2pdf (or)
#     - easy_install rst2pdf

# 2. Add rst2pdf to the list of extensions in conf.py


# extensions = ['rst2pdf.pdfbuilder']


#     This list will be empty if you accepted the defaults when the project was setup. If not, just append 'rst2pdf.pdfbuilder' to the list.


# 3. Add a pdf_documents variable to conf.py

#   pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Your Name'),]
#   # index - master document
#   # rst2pdf - name of the generated pdf
#   # Sample rst2pdf doc - title of the pdf
#   # Your Name - author name in the pdf

# 4. Generate pdf


# sphinx-build -b pdf source build/pdf


#    The generated pdf will be in the build/pdf directory.
