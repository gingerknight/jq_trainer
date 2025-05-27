# python imports

# third-party imports
import libtmux
from libtmux.constants import PaneDirection


# Tmux Session Creation Class
class TmuxSession:
    def __init__(self, session_name: str = "jq_trainer"):
        """
        Initialize a TmuxSession instance.
        :param session_name: Name of the tmux session to create or attach to.
        """
        self.session_name = session_name
        self.server = libtmux.Server()
        self.session = self.__get_or_create_session()
        self.__window_panes()

    def __get_or_create_session(self):
        """
        Create a new tmux session, kills any existing session with the same name.
        """
        return self.server.new_session(session_name=self.session_name, kill_session=True)

    def __window_panes(self):
        """
        Split current window into three panes (upper left, upper right, lower).
        """
        window = self.session.active_window
        # Split the window into three panes
        window.split(direction=PaneDirection.Below)
        # Further split the upper left pane into two panes
        window.panes[0].split(direction=PaneDirection.Right)

    def __repr__(self):
        """
        String representation of the TmuxSession instance.
        """
        return f"TmuxSession(session_name={self.session_name})"
