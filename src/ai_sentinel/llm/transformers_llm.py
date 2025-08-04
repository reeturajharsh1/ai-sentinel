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

    def generate_text(
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

        return response # doesn't work correctly rn

    def format_llm_response(self, response) -> LLMResponse:
            '''Convert response to built in Model type to a response type of LLMResponse'''

            output: LLMResponse = LLMResponse(
                content=response.choices[0].message.content,
                model = self.model
            )
            output.usage = {
                'model_tokens': response.usage.completion_tokens,
                'prompt_tokens': response.usage.prompt_tokens,
                'total_tokens': response.usage.total_tokens,
            }

            output.response_time_ms = output.timestamp.timestamp() - response.created
            output.finish_reason = response.choices[0].finish_reason
            return output
    
    
    def generate_text_async(self, prompt, system_prompt = None, context = None, temperature = 0.7, **kwargs):
        return super().generate_text_async(prompt, system_prompt, context, temperature, **kwargs)
    
    def validate_async(self):
        return super().validate_async()
    
    def provider_name(self):
        pass