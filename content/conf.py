# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bouncmpe/docs'
copyright = '2025 Department of Computer Engineering, Boğaziçi University'
author = 'Dogan Ulus'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]

myst_title_to_header = True
myst_heading_anchors = 2
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
    "attrs_inline",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "@bouncmpe/docs"
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
]
html_permalinks_icon = "<span>#</span>"
html_theme_options = {
     "light_css_variables": {
        "color-brand-primary": "#1e4a8b",
        "color-brand-content": "#1e4a8b",

        "color-foreground-primary": "#2e3440", 
        "color-foreground-secondary": "#4c566a", 
        "color-foreground-muted": "#0050a0",  
        "color-foreground-border": "#3b4252",  

        "color-background-primary": "#f2f4f7",
        "color-background-secondary": "#eceff4",
        "color-background-hover": "#97afc6",
        "color-background-hover--transparent": "#fff",
        "color-background-border": "#e5e9f0",
        "color-background-item": "#fff",

        "color-admonition-background": "#f8d7da",  
        "color-admonition-warning-border": "#f5c6cb",  
        "color-admonition-warning-text": "#721c24",  
    },

    "dark_css_variables": {
 
        "color-brand-primary": "#eceff4",
        "color-brand-content": "#eceff4",
        "color-brand-visited": "#872ee0",

        "color-foreground-primary": "#eceff4",
        "color-foreground-secondary": "#e5e9f0", 
        "color-foreground-muted": "#81a1c1",
        "color-foreground-border": "#88c0d0",
       
        "color-background-primary": "#2e3440",
        "color-background-secondary": "#292f3a",
        "color-background-hover": "#434c5e",
        "color-background-hover--transparent":"#434c5e",
        "color-background-border":"#4c566a",
        "color-background-item":"#4c566a",

        "color-link--visited": "#eceff4",

         "color-admonition-background": "#3e1f1b", 
        "color-admonition-warning-border": "#d9534f",  
        "color-admonition-warning-text": "#ffffff",  

    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/bouncmpe/docs",
            "html": "",
            "class": "fa-brands fa-solid fa-git-alt fa-2x",
        },
    ],
    "source_repository": "https://github.com/bouncmpe/docs/",
    "source_branch": "main",
    "source_directory": "content",
    "announcement": "This site is <em>under construction.</em>",
}
