import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import nltk
from nltk.chat.util import Chat, reflections
from chat import pairs

# Download necessary NLTK data
nltk.download('punkt')

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to send message
def send_message():
    user_input = user_entry.get()
    if user_input.lower() == "quit":
        root.destroy()
        return
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    chat_history.config(state=tk.DISABLED)
    response = chatbot.respond(user_input)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "Bot: " + response + "\n")
    chat_history.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)

# Initialize GUI
root = tk.Tk()
root.title("Basic Chatbot")

# Create chat history window
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_history.pack(padx=10, pady=10)

# Create user input entry
user_entry = tk.Entry(root, width=50)
user_entry.pack(padx=10, pady=10)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Run the GUI main loop
root.mainloop()