---
layout: default
title: ChatManger Package
nav_order: 2
has_children: true
permalink: /docs/ChatManager
---

# ChatManger Package
The logic for managing multiple chat instances with different agents has been put into this package.
The package was designed to support multiple output options to be more reusable in future projects.

## Features 
- Can handle any number of chats
- Multiple output formats (full response, stream, list object)
- Dynamic agent creation from mbti data
- Extra functions for calling hints
- Console inference option
- Llama wrapper


## Files
| File              | description                                                                           |
|:------------------|:--------------------------------------------------------------------------------------|
| ChatManager.py    | Implements the main class of the package (all interactions should be with this class) |
| ConsoleChat.py    | Runs console inference, useful for experimenting with system prompts                  |
| LlamaGenerator.py | Wrapper for llama_cpp_python used by the Chat Manager.                                |

