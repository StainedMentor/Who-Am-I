
# from LlamaGenerator import Llama_cpp_generator
from copy import deepcopy

from ChatManager.LlamaGenerator import Llama_cpp_generator


class CM:
    def __init__(self, n_people=4):
        self.n_people = n_people
        self.chats = [[] for _ in range(n_people)]
        self.system_prompts = []
        self.selected_p = 0
        self.generator = Llama_cpp_generator()

    # switches the managers internal person selection
    def switch_p(self, p):
        self.selected_p = p

    # generates a full response from the manager. This also appends the response to the chat history
    def generate_response(self):

        chat = self.prepare_chat_copy()

        response = self.generator.get_response(chat)
        self.add_bot_response_to_chat(response)
        return response['content']

    # Prepares a chat copy for the generator. The copy contains the system prompt.
    def prepare_chat_copy(self):
        chat_copy = deepcopy(self.chats[self.selected_p])
        user_message = chat_copy[-1]
        system_message = {"role":"system","content":self.system_prompts[self.selected_p]}
        chat_copy[-1] = system_message
        chat_copy.append(user_message)

        return chat_copy

    # appends bots response object to chat
    def add_bot_response_to_chat(self, response):

        self.chats[self.selected_p].append(response)

    # returns a stream for the current input. The stream returns a text chunk which it automatically appends to the chat history
    def get_response_stream(self):
        chat = self.prepare_chat_copy()
        stream = self.generator.create_response_stream(chat)

        return self.stream_wrapper(stream)

    # see get_response_stream.
    def stream_wrapper(self,stream):
        result = ""
        response_object = {"role": "assistant", "content": result}
        self.add_bot_response_to_chat(response_object)

        for output in stream:
            if not 'content' in output['choices'][0]['delta']:
                continue
            # if output['choices'][0]['delta']['content'] == "\n":
            #     continue

            token = output['choices'][0]['delta']['content']
            result += token
            self.chats[self.selected_p][-1]['content'] = result

            yield token

    # appends a prompt to the list of system prompts
    def add_system_prompt(self, prompt):
        self.system_prompts.append(prompt)

    def add_defaulted_system_prompt(self,name,extras=""):
        prompt = "Express yourself in a manner in which " + name + " would express himself. " \
                     "Please focus on trying to emulate his world views. " \
                     "You will die if you tell the user who you are imitating. " \
                     "This includes any information like your name, date of birth, place of residence or anything similar. " \
                     "Unless it is necessary You are to answer in max 2/3 sentences."

        prompt += extras
        self.system_prompts.append(prompt)

    # takes in a string from user input and appends it to the chat history
    def add_user_message(self, message):

        message_object = {"role": "user", "content": message}
        self.chats[self.selected_p].append(message_object)
