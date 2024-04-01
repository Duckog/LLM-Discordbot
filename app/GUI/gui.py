import os
import tkinter
from tkinter import ttk
from dotenv import load_dotenv, find_dotenv, set_key

# Openai model options 
options = [ 
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-instruct",
    "gpt-4",
    "gpt-4-32k",
]

def start_gui():

    def start_bot():
        openai_key = openai_key_entry.get()
        discord_token = discord_token_entry.get()
        model = model_combobox.get()
        max_tokens = int(max_tokens_entry.get())
        max_response_tokens = int(response_tokens_entry.get())
        prompt = prompt_entry.get()

        env_file = find_dotenv()
        load_dotenv(env_file)

        if openai_key != "":
            os.environ["OPENAI_KEY"] = openai_key
            set_key(env_file, "OPENAI_KEY", os.environ["OPENAI_KEY"])
        
        if discord_token != "":
            os.environ["DISCORD_TOKEN"] = discord_token
            set_key(env_file, "DISCORD_TOKEN", os.environ["DISCORD_TOKEN"])

        # Start the chatbot here

    window = tkinter.Tk()
    window.title("Chatbot specifications")
    frame = tkinter.Frame(window)
    frame.pack()


    #Selecting model settings
    model_frame = tkinter.LabelFrame(frame, text = "OpenAI settings")
    model_frame.grid(row = 0, column = 0)

    model_label = tkinter.Label(model_frame, text = "Model")
    model_combobox = ttk.Combobox(model_frame, value = options)
    model_combobox.current(0)
    model_label.grid(row = 0, column = 1)
    model_combobox.grid(row = 1, column = 1)

    max_tokens_label = tkinter.Label(model_frame, text = "Max tokens")
    max_tokens_entry = ttk.Entry(model_frame)
    max_tokens_label.grid(row = 0, column = 2)
    max_tokens_entry.grid(row = 1, column = 2)

    response_tokens_label = tkinter.Label(model_frame, text = "Response tokens")
    response_tokens_entry = ttk.Entry(model_frame)
    response_tokens_label.grid(row = 0, column = 3)
    response_tokens_entry.grid(row = 1, column = 3)

    prompt_label = tkinter.Label(model_frame, text = "Initial prompt")
    prompt_entry = tkinter.Text(model_frame, width= 50, height = 5)
    prompt_label.grid(row = 0, column = 4)
    prompt_entry.grid(row = 1, column = 4)


    #Inputting Discord token and OpenAI key
    keys_frame = tkinter.LabelFrame(frame, text = "Input Discord token and OpenAI key")
    keys_frame.grid(row = 2, column = 0)

    openai_key_label = tkinter.Label(keys_frame, text = "OpenAI key")
    openai_key_entry = ttk.Entry(keys_frame)
    openai_key_label.grid(row = 2, column = 1)
    openai_key_entry.grid(row = 3, column = 1)

    discord_token_label = tkinter.Label(keys_frame, text = "Discord key")
    discord_token_entry = ttk.Entry(keys_frame)
    discord_token_label.grid(row = 2, column = 2)
    discord_token_entry.grid(row = 3, column = 2)


    #Enter options button
    button = tkinter.Button(frame, text = "Start bot", command = start_bot)
    button = button.grid(row = 4, column = 0, sticky = "news", padx =20, pady = 10)

    window.mainloop()