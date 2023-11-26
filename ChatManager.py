from LlamaGenerator import Llama_cpp_generator

class ChatManager:
    def __init__(self, n_people=4):
        self.n_people = n_people
        self.chats = [[],[],[],[]]
        self.p_info = [{}]
        self.selected_p = 0
        self.generator = Llama_cpp_generator()

    def switch_p(self, p):
        self.selected_p = p

    def generate_response(self):
        chat = self.generator.get_response(self.chats[self.selected_p])

        # generator.validate
        self.chats[self.selected_p] = chat

    def add_user_message(self, message):
        self.chats[self.selected_p].append({"role": "user", "content": message})
