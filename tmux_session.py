# python imports

# third-party imports
import libtmux


server = libtmux.Server()
session = server.new_session(session_name="jq_trainer", kill_session=True)
window = session.attached_window
pane1 = window.panes[0]
pane1.send_keys("echo 'Hello, World!'")
# This code creates a new tmux session named "jq_trainer", kills any existing session with that name,
# and sends the command to echo "Hello, World!" in the first pane of the attached window.
