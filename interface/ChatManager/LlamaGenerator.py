# pip install llama-cpp-python
from llama_cpp import Llama

# This class takes care of loading the model, generating responses and filtering responses that give the person away.
class Llama_cpp_generator:
    # llama-2-7b-chat-Q4_K_M will be the default model used in the project. It's both effective and resource friendly.
    # ctx_length describes the number of tokens in the generation process h
    def __init__(self, ctx_length=4096, m_path="./llama-2-7b-chat.Q4_K_M.gguf", n_gpu_layers=1000, n_batch=52):
        self.ctx_length = ctx_length
        self.black_list = []
        self.base_prompt = ""
        self.LLM = Llama(model_path=m_path, n_ctx=ctx_length,n_gpu_layers=n_gpu_layers, n_batch=n_batch)

    # returns a single response object from the LLM
    def get_response(self, chat):
        response = self.LLM.create_chat_completion(chat)
        response = response["choices"][0]["message"]

        return response

    # returns basic LLM stream object
    def create_response_stream(self, chat):
        stream = self.LLM.create_chat_completion(chat, stream=True,repeat_penalty=1.1, max_tokens=256)
        return stream

    # Checks response for words that tell too much about the person
    def validate_response(self, response):
        if response == "":
            return False
