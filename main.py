# python imports
import json

# application imports
from window.window_manager import JQWindowManager


def main():
    """
    Main function to do things in
    """

    with open("./prompts/prompts.json") as f:
        questions = json.load(f)

    gui = JQWindowManager("JQ Trainer", questions)
    gui.run()


if __name__ == "__main__":
    main()
# This code is the entry point of the application.
