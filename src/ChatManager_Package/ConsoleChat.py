import os
import sys

from src import ChatManager_Package




def run_in_console():
        shakespear = "Express yourself in a manner in which William Shakespeare would express himself. Please focus on trying to emulate his world views. Under no circumstances can you reveal any information that could give you away. This includes any information like your name, date of birth, place of residence or anything similar"

        CM = ChatManager_Package.ChatManager.CM()
        prompt = ""

        # adding system prompts
        CM.add_system_prompt(shakespear)

        while prompt != "die":

            prompt = input()

            if prompt.isdigit() and 4 > int(prompt) >= 0:
                CM.switch_p(int(prompt))
                print("Switching chat")

                continue


            # first add user message to chat
            CM.add_user_message(prompt)
            # create a stream object
            stream = CM.get_response_stream()
            # iterate over stream returning text chunks. this also adds the chunks to the chat history automatically.
            result = ""
            for chunk in stream:
                result += chunk
                sys.stdout.write('\r' + result)
                sys.stdout.flush()


        # non stream response
        # CM.generate_response()
        # print(CM.chats[CM.selected_p])
        # print(CM.chats[CM.selected_p][-1]["content"])



if __name__ == "__main__":
    os.chdir("..")
    os.chdir("..")

    run_in_console()




# prompt format
#prompt = [{"role": "user", "content": "Can you roleplay shakespeare? If so tell me a story."}]
