.. currentmodule:: ai_sentinel

API Reference
=============
This page contains the API reference for public objects and functions in ai_sentinel.


.. _core_api:

core
-----------
.. autosummary::
    :toctree: generated/

    ai_sentinel.LLMResponse

.. _guards_api:

guards 
----------
.. autosummary::
    :toctree: generated/

    .. data models

    ai_sentinel.toxicity_guard.ToxicityResult
    ai_sentinel.toxicity_guard.ToxicityCategories
    ai_sentinel.toxicity_guard.ToxicityScore

    .. detection TODO: should I add helper functions?

    ai_sentinel.toxicity_guard.ToxicityGuard
    ai_sentinel.toxicity_guard.analyze_async
    ai_sentinel.toxicity_guard.analyze
    ai_sentinel.toxicity_guard.structure_output
    
    .. system prompt

    ai_sentinel.toxicity_guard.SYSTEM_PROMPT
    ai_sentinel.toxicity_guard.ROLE
    ai_sentinel.toxicity_guard.CATEGORY_DESCRIPTIONS
    ai_sentinel.toxicity_guard.PROMPTS

.. _llm_api:

llm
-----
.. autosummary::
    :toctree: generated/

    .. models 
    
    ai_sentinel.BaseLLMClient
    ai_sentinel.AzureOpenAIClient
    ai_sentinel.GeminiClient

    .. functions

    ai_sentinel.generate_text
    ai_sentinel.generate_text_async
    ai_sentinel.validate
    ai_sentinel.validate_async
    ai_sentinel.provider_name
    ai_sentinel.info
    ai-sentinel.format_llm_response
