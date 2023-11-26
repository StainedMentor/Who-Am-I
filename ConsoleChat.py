
from ChatManager import ChatManager


CM = ChatManager()
prompt = ""

while prompt != "die":

    prompt = input()

    if prompt.isdigit() and 4 > int(prompt) >= 0:
        CM.switch_p(int(prompt))
        print("Switching chat")

        continue

    CM.add_user_message(prompt)
    CM.generate_response()

    print(CM.chats[CM.selected_p][-1]["content"])


# download link for small model
# https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf?download=true


# prompt format
#prompt = [{"role": "user", "content": "Can you roleplay shakespeare? If so tell me a story."}]
