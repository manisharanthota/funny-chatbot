# 😎 Funny Chatbot

A command-line chatbot built with the Claude API. It chats in a witty, sarcastic tone and remembers the conversation.

## Features
- Multi-turn conversation (remembers chat history)
- Streaming replies (word by word)
- Custom personality via system prompt
- Token budget to control cost
- Colorful CLI with `rich`

## Setup
```bash
pip install anthropic python-dotenv rich
```

Create a `.env` file:
```
ANTHROPIC_API_KEY=your-key-here
```

## Run
```bash
python chatbot.py
```
Type `quit` or `exit` to leave.

## Built while learning
Part of my journey through the *Building with the Claude API* course on Claude Academy.