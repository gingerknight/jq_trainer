# python imports

# third-party imports
import libtmux


# Tmux Session Creation Class
class TmuxSession:
    def __init__(self, session_name: str = "jq_trainer"):
        """
        Initialize a TmuxSession instance.
        :param session_name: Name of the tmux session to create or attach to.
        """
        self.session_name = session_name
        self.server = libtmux.Server()
        self.session = self.get_or_create_session()

    def get_or_create_session(self):
        """
        Create a new tmux session, kills any existing session with the same name.
        """
        return self.server.new_session(session_name=self.session_name, kill_session=True)


# This code creates a new tmux session named "jq_trainer", kills any existing session with that name,
# and sends the command to echo "Hello, World!" in the first pane of the attached window.
window = TmuxSession("jq_trainer").session.active_window
pane1 = window.panes[0]
pane1.send_keys("echo 'Hello, World!'")
