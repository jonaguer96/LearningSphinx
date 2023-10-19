
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jubler'
copyright = '2023, Jonathan'
author = 'Jonathan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []
html_static_path = ['_static']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "navbar_align": "content"
}
html_sidebars = {
    'beforeyoubegin': [
        'globaltoc.html'
    ],
    'tips': [
        'globaltoc.html'
    ],
    'excmmain':[
        'globaltoc.html'
    ],
    'excmfunctions':[
        'globaltoc.html'
    ]

}
