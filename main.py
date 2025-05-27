# python imports

# application imports
from tmux_session import TmuxSession


def main():
    """
    Main function to do things in
    """
    # This code creates a new tmux session named "jq_trainer", kills any existing session with that name,
    # and sends the command to echo "Hello, World!" in the first pane of the attached window.
    window = TmuxSession("jq_trainer").session.active_window
    pane1 = window.panes[0]
    pane1.send_keys("echo 'Hello, World!'")


if __name__ == "__main__":
    main()
# This code is the entry point of the application.
