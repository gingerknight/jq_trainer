# python imports
import subprocess

# application imports
from tmux_session import TmuxSession
from prompts.prompts import start_prompts
from watcher import PaneWatcher
from helpers import bash_log_file, validator


def setup_tmux_session():
    """
    Set up the tmux session with three panes:
    - The first pane displays the question.
    - The second pane is for user input.
    - The third pane is for feedback.
    """
    window = TmuxSession(session_name="jq_trainer", prompts=start_prompts)
    window.start()
    return window


def main():
    """
    Main function to do things in
    """
    # This code creates a new tmux session named "jq_trainer", kills any existing session with that name,
    # and sends the command to echo "Hello, World!" in the first pane of the attached window.
    window = setup_tmux_session()
    bash_log_file(window.session.active_window.panes[1])
    # Kick off the watcher thread to monitor user input
    watcher = PaneWatcher(
        log_file="./input.log", feedback_pane=window.session.active_window.panes[2], validator=validator
    )
    watcher.start()

    # Now attach to the session
    subprocess.run(["tmux", "attach-session", "-t", window.session_name])


if __name__ == "__main__":
    main()
# This code is the entry point of the application.
