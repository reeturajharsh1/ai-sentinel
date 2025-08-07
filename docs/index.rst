..  AI-Sentinel documentation master file, 
    created by sphinx-quickstart
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

Welcome to the AI Sentinel documentation
---------------------------------

**AI Sentinel** AI Sentinel is a Python package designed to help developers 
integrate toxicity analysis into their applications with ease. It provides 
a simple, unified interface to leverage powerful AI models for detecting 
and categorizing harmful content in text.

Install
=======

AI Sentinel can be installed from either `PyPI <https://pypi.org/project/ai-sentinel/>`_ ::

    pip install ai_sentinel
    
.. or # TEST THIS FIRST
   uv run --with ai-sentinel --no-project -- python -c "import ai_sentinel"

Requirements
-------
- Python 3.11+

.. toctree::
    :maxdepth: 2
    :caption: Introduction

    Setup overviews <overviews>

.. toctree::
    :maxdepth: 2
    :caption: Examples

    Text examples <text_examples>

.. toctree::
    :maxdepth: 2
    :caption: Reference

    API reference <api>
    API examples <api_examples>

.. toctree::
    :maxdepth: 1
    :caption: Development

    Release notes <release_notes>
    Contributing guide <contributing>
