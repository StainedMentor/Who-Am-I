# pip install llama-cpp-python
from llama_cpp import Llama


# This class takes care of loading the model, generating responses and filtering responses that give the person away.
class Llama_cpp_generator:
    # llama-2-7b-chat-Q4_K_M will be the default model used in the project. It's both effective and resource friendly.
    # ctx_length describes the number of tokens in the generation process
    def __init__(self, ctx_length=2048, m_path="./llama-2-7b-chat.Q4_K_M.gguf"):
        self.ctx_length = ctx_length
        self.black_list = []
        self.base_prompt = ""
        self.LLM = Llama(model_path=m_path, n_ctx=ctx_length)

    # Adds llms response to chat
    def get_response(self, chat):
        response = self.LLM.create_chat_completion(chat)

        chat.append(response["choices"][0]["message"])
        return chat

    # Checks response for words that tell too much about the person
    def validate_response(self, response):
        if response == "":
            return False
