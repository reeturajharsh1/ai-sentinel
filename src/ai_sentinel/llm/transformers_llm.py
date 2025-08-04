import json
from typing import Optional, Any
from datetime import datetime

from transformers import AutoTokenizer, AutoModelForCausalLM

from ai_sentinel.llm.base import BaseLLMClient
from ai_sentinel.core.models import LLMResponse

class TransformersClient(BaseLLMClient):
    '''Open Source LLM client implementation using Transformers framework from Huggingface'''

    def __init__(
            self, 
            model: str,
            api_key: Optional[str] = 'EMPTY',
            timeout: Optional[float] = 30.0, 
            **kwargs
        ):
        super().__init__(api_key, model, timeout, **kwargs)
        # write smth to check if model is a supported model???

        self.tokenizer = AutoTokenizer.from_pretrained(self.model)
        self.client = AutoModelForCausalLM.from_pretrained(self.model)

    def generate_text_async(
            self, 
            prompt: str, 
            system_prompt: Optional[str] = None, 
            context: Optional[list[dict[str,str]]] = None,
            temperature: Optional[float] = 0.0,
            **kwargs # supply response format in kwargs
        ) -> LLMResponse:

        if not prompt or not isinstance(prompt, str):
            raise ValueError('Prompt must be a non-empty string')
        
        message = []
        # check if there is a system prompt given
        if system_prompt:
            message.append({
                'role': 'system',
                'content': system_prompt
            })
        # check if there is context given
        if context:
            message.extend(context)

        message.append({
            'role': 'user',
            'content': prompt
        })

        inputs = self.tokenizer.apply_chat_template(
            message,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
            temperature=temperature
        ).to(self.client.device)

        response_start_time: datetime = datetime.utcnow()
        response = self.client.generate(**inputs, max_new_tokens=512)
        response = self.tokenizer.decode(response[0][inputs["input_ids"].shape[-1]:])
        response_end_time: datetime = datetime.utcnow()

        return self.format_llm_response(response, response_start_time, response_end_time)

    '''
    ```
    {
    "is_toxic": true,
    "confidence": 0.95,
    "categories": ["threats", "violence"],
    "reason": "The text contains a direct threat of violence, specifically hitting the speaker with a baseball bat, which implies a physical attack. This constitutes a threat of harm and falls under the threats and violence categories.",
    "score": "high"
    }
    ```
    '''
    def format_llm_response(self, response, start_time: datetime, end_time: datetime) -> LLMResponse:
            '''Convert response to built in Model type to a response type of LLMResponse'''
            cleaned_response = response.strip('```')
            try:
                response_dict = json.loads(cleaned_response)
            except ValueError:
                raise Exception('llm response couldnt be converted to a dict')


            output: LLMResponse = LLMResponse(
                content=response_dict,
                model = self.model,
                response_time_ms = start_time.timestamp() - end_time.timestamp()
            )
            return output
    
    def validate_async(self):
        try:
            self.client.models.list()
            return True
        except Exception as e: 
            print(f'An unexpected error occurred during API key validation: {e}')
            return False
    
    def provider_name(self):
        return f'Transformers Open Source: {self.model}'