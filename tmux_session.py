# python imports
from typing import Optional

# third-party imports
import libtmux
from libtmux.constants import PaneDirection

# application imports
from prompts.prompts import start_prompts
from helpers import shell_escape_single_quotes


# Tmux Session Creation Class
class TmuxSession:
    """
    A class to manage a tmux session for the jq trainer application.
    It creates a session with three panes: one for the question, one for user input,
    and one for feedback.
        # The panes are arranged as follows:
        # ┌───────────────┬───────────────┐
        # │   Question    │   User Input  │
        # │     Pane      │     Pane      │
        # └───────────────┴───────────────┘
        # ┌───────────────────────────────┐
        # │         Feedback Pane         │
        # └───────────────────────────────┘

    """

    def __init__(self, session_name: str = "jq_trainer", prompts: Optional[dict] = None):
        """
        Initialize a TmuxSession instance.
        :param session_name: Name of the tmux session to create or attach to.
        """
        self.session_name = session_name
        self.server = libtmux.Server()
        self.session = self.__get_or_create_session()
        self.start_prompts = prompts if prompts is not None else start_prompts

    def __get_or_create_session(self):
        """
        Create a new tmux session, kills any existing session with the same name.
        """
        return self.server.new_session(session_name=self.session_name, kill_session=True)

    def __split_panes(self):
        """
        Split current window into three panes (upper left, upper right, lower).
        """
        window = self.session.active_window
        # Split the window into three panes
        window.split(direction=PaneDirection.Below)
        # Further split the upper left pane into two panes
        window.panes[0].split(direction=PaneDirection.Right)

    def __send_startup_prompts(self):
        """
        Send initial prompts to the panes.
        """
        pane1, pane2, pane3 = self.session.active_window.panes

        pane_map = {
            "question": pane1,
            "input": pane2,
            "feedback": pane3,
        }

        for pane_name, lines in start_prompts.items():
            for line in lines:
                escaped_line = shell_escape_single_quotes(line)
                pane_map[pane_name].send_keys(f"echo -e '{escaped_line}'")

    def start(self):
        self.__split_panes()
        self.__send_startup_prompts()

    def __repr__(self):
        """
        String representation of the TmuxSession instance.
        """
        return f"TmuxSession(session_name={self.session_name})"
