
.. _overviews:

Setup Overviews
----------------
This section provides an overview of setting up the use of AI Sentinel.


.. _env_examples:

Environment
================
..  Discuss setting up environmental variables to hold secret keys 
    is the best way to ensure no secret leaks of sensitive information.

.. toctree::
    :glob:
    :maxdepth: 1

    example_notebooks/environment/env_setup

.. _supported_llm_services:

Supported LLM API Services
===========================

AI Sentinel supports multiple LLM API services through a unified interface.
It is Model-agnostic, meaning you can switch between different LLM providers
with minimal code changes. Currently, the following LLM services are supported:

+---------------+----------------------------------+---------------------+-------------------------------------------------------------------------------------+
| Provider      | Models                           | Notes               | Example                                                                             |
+===============+==================================+=====================+=====================================================================================+
| Azure OpenAI  | GPT-4, GPT-4o, GPT-3.5-turbo     | ...                 | `basic client <ai-sentinel\example_notebooks\api_examples\llm\azure_openai.ipynb>`_ |
+---------------+----------------------------------+---------------------+-------------------------------------------------------------------------------------+
| Google Gemini | Gemini 2.* Flash, Gemini 2.5 Pro | ...                 | `basic client <ai-sentinel\example_notebooks\api_examples\llm\gemini.ipynb>`_       |
+---------------+----------------------------------+---------------------+-------------------------------------------------------------------------------------+
| Anthropic     | ...                              | *To be implemented* | ...                                                                                 |
+---------------+----------------------------------+---------------------+-------------------------------------------------------------------------------------+
| Open Source   | ...                              | *To be implemented* | ...                                                                                 |
+---------------+----------------------------------+---------------------+-------------------------------------------------------------------------------------+