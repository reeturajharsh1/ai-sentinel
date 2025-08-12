.. currentmodule:: ai_sentinel

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

    .. data models

    ai_sentinel.guards.toxicity_guard.ToxicityResult
    ai_sentinel.guards.toxicity_guard.ToxicityCategories
    ai_sentinel.guards.toxicity_guard.ToxicityScore

    .. detection TODO: should I add helper functions?

   ..  ai_sentinel.guards.toxicity_guard.ToxicityGuard
   ..  ai_sentinel.guards.toxicity_guard.analyze_async
   ..  ai_sentinel.guards.toxicity_guard.analyze
   ..  ai_sentinel.guards.toxicity_guard.structure_output
    
    .. system prompt

   ..  ai_sentinel.guards.toxicity_guard.SYSTEM_PROMPT
   ..  ai_sentinel.guards.toxicity_guard.ROLE
   ..  ai_sentinel.guards.toxicity_guard.CATEGORY_DESCRIPTIONS
   ..  ai_sentinel.guards.toxicity_guard.PROMPTS

.. _llm_api:

llm
-----
.. autosummary::
   :toctree: _autosummary  
   :recursive:
    ai_sentinel.llm.BaseLLMClient
    ai_sentinel.llm.AzureOpenAIClient
    ai_sentinel.llm.GeminiClient

    .. functions

   ..  ai_sentinel.llm.base.generate_text
   ..  ai_sentinel.llm.base.generate_text_async
   ..  ai_sentinel.llm.base.validate
   ..  ai_sentinel.llm.base.validate_async
   ..  ai_sentinel.llm.base.provider_name
   ..  ai_sentinel.llm.base.info
   ..  ai-sentinel.llm.base.format_llm_response
