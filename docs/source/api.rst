
API Reference
=============

This page contains the API reference for public objects and functions in ai_sentinel.


.. _core_api:

core
-----------

.. autosummary::
   :toctree: _autosummary  
   :recursive:  
             
    ai_sentinel.core.LLMResponse

.. _guards_api:

guards 
----------

.. autosummary::
   :toctree: _autosummary  
   :recursive:            

    ai_sentinel.guards.toxicity_guard.ToxicityResult
    ai_sentinel.guards.toxicity_guard.ToxicityCategories
    ai_sentinel.guards.toxicity_guard.ToxicityScore

.. _llm_api:

llm
-----

.. autosummary::
   :toctree: _autosummary  
   :recursive:

    ai_sentinel.llm.BaseLLMClient
    ai_sentinel.llm.AzureOpenAIClient
    ai_sentinel.llm.GeminiClient

