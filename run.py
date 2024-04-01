import os
from app.GUI.gui import start_gui

if not os.path.exists(".env"):
    with open(".env", 'w') as file:
        file.write("OPENAI_KEY = \n")
        file.write("DISCORD_TOKEN = ")
else:
    pass

if __name__ == "__main__":
    start_gui()