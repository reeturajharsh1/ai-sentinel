Usage
=====

Basic Usage
----------

Here's how to use the basic functionality of ai_sentinel:

.. code-block:: python

    from ai_sentinel import AzureOpenAIClient, ToxicityGuard

    # Initialize LLM client
    client = AzureOpenAIClient(
        api_key="YOUR-API-KEY",
        model="gpt-4o-mini",
        api_version="2024-02-01",
        azure_endpoint="https://your-resource.openai.azure.com/"
    )

    # Create toxicity guard
    guard = ToxicityGuard(client)

    # Analyze text
    result = guard.analyze("This is a normal message")

    print(f"Is toxic: {result.is_toxic}")
    print(f"Confidence: {result.confidence}")
    print(f"Categories: {result.categories}")
    print(f"Reason: {result.reason}")
    print(f"Severity: {result.score}")

Async Usage
------------

Generate text and validate responses asynchronously.

.. code-block:: python
    
    import asyncio
    from ai_sentinel import AzureOpenAIClient, ToxicityGuard

    client = AzureOpenAIClient(
        api_key="YOUR-API-KEY",
        model="gpt-4o-mini",
        api_version="2024-02-01",
        azure_endpoint="https://your-resource.openai.azure.com/"
    )

    async def main() -> None:
        guard = ToxicityGuard(client)
        response = await guard.analyze_async("Text to analyze")

        print(f"Is toxic: {result.is_toxic}")
        print(f"Confidence: {result.confidence}")
        print(f"Categories: {result.categories}")
        print(f"Reason: {result.reason}")
        print(f"Severity: {result.score}")

    asyncio.run(main())   

