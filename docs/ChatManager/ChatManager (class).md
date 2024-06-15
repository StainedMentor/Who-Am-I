---
layout: default
title: ChatManager (class)
parent: ChatManger Package
nav_order: 1
---

# ChatManager Class
{: .no_toc }

This is an overview of the ChatManager class.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Usage

## Attributes

### n_people : Int
Specifies the number of active chats

### chats : List
A list of lists containing chat history in openai standard.

### person_list: List
A list of names (Strings) for each agent.

### system_prompts: List
A list of system prompts used to create agents. (strings)

### selected_p: Int
The currently selected chat.

### generator: LlamaGenerator
A generator object for chat completion.

## Methods


### init()(n_people=4):
Initializes the chat system with a specified number of participants.
### reset(n_people=4):
Resets the chat system, reinitializing with a specified number of participants and clearing all existing chat histories, participant lists, and system prompts.
### switch_p(p):
Switches the current active participant to the specified participant index.
### generate_response(): String
Generates a response from the chat system by preparing a copy of the current chat, obtaining a response from the generator, adding the response to the chat, and returning the response content.
### prepare_chat_copy(): List
Creates and returns a copy of the current chat and inserts a system message based on the corresponding system prompt.
### prepare_chat_hint(): List
Prepares a chat sequence for providing a hint, including a user question and a system prompt with the name of the currently selected agent.
### add_bot_response_to_chat(response):
Adds the given response from the bot to the chat history of the currently selected agent.
### get_response_stream(): Stream
Prepares a copy of the current chat and generates a response stream using the generator.
Returns a wrapped version of the stream for displaying.

### get_hint_stream(): Stream
Returns a hint stream for the chat.

### hint_stream_wrapper(stream): yield token
Iterates over a stream of hint responses, extracting and yielding tokens that contain content.
### stream_wrapper(stream): yield token
Iterates over a stream of hint responses, extracting and yielding tokens that contain content.
Updates the chat history with the content.
### add_system_prompt(prompt):
Adds a system prompt to the chat manager. Appends to the end of the list.

### add_defaulted_system_prompt(name,extras=""): 
Creates and appends a default prompt created with mbti data for the given name. Uses data specified in data.json and mbti.json.

### add_user_message(message):
Appends the message to the currently active chat.
