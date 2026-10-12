# Basic Rule-Based Chatbot

A simple command-line chatbot written in Python. It matches user input against predefined phrases and returns a matching reply. It's a beginner-friendly project for practicing `if-elif` statements, functions, loops, and basic input/output.

## Features

- Responds to greetings such as "hello", "hi", and "hey"
- Answers "how are you" with a short reply
- Says goodbye and exits the program when the user types "bye", "goodbye", or "see you"
- Handles thanks, questions about its name, and unrecognized input
- Case-insensitive, and ignores extra spaces around input

## Requirements

- Python 3.6 or later
- No external libraries needed

## Installation

1. Clone or download this project.
2. Save the code as `chatbot.py`.

## Usage

Run the chatbot from the terminal:

```bash
python chatbot.py
```

Example session:

```
Chatbot: Hello! Type 'bye' to exit.
You: hello
Chatbot: Hi!
You: how are you
Chatbot: I'm fine, thanks!
You: bye
Chatbot: Goodbye!
```

## Supported Inputs

| User input | Chatbot reply |
|---|---|
| hello, hi, hey | Hi! |
| how are you, how r u | I'm fine, thanks! |
| bye, goodbye, see you | Goodbye! |
| thanks, thank you | You're welcome! |
| what is your name, who are you | I'm a simple rule-based chatbot. |
| anything else | Sorry, I don't understand that yet. |

## How It Works

- **`get_response(user_input)`** normalizes the input with `.strip().lower()` and checks it against each rule using `if-elif`. It returns the first matching reply, or a fallback reply if nothing matches.
- **`run_chatbot()`** runs a `while True` loop that reads input, prints the reply, and exits when the user says goodbye.

## Adding New Rules

Add another `elif` branch in `get_response`:

```python
elif message in ("good morning", "morning"):
    return "Good morning!"
```

## Project Structure

```
chatbot/
├── chatbot.py
└── README.md
```

## Limitations

- Matches only exact phrases. "Hello there" will not match "hello".
- Responses are fixed and do not use context from earlier messages.
- Not suitable for natural language understanding.

## Possible Improvements

- Use keyword matching or regular expressions for more flexible input
- Add random choice among several replies for variety
- Store conversation history
- Connect to a language model for open-ended conversation

## License

This project is free to use for learning purposes.
