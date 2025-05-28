import threading
import time
from libtmux import Pane, Session, Window


# Pane Watcher Class

class PaneWatcher(threading.Thread):
    """
    A class to monitor the tmux panes for changes and trigger actions based on those changes.
    """
    def __init__(self, log_file, feedback_pane, validator, interval=5.0):
        super().__init__(daemon=True)
        self.log_file = log_file
        self.feedback_pane: Pane = feedback_pane # The pane where feedback is displayed
        self.validator = validator
        self.interval: float = interval
        self.last_position: int = 0
        self.attempt_count = 0

    def run(self):
        """
        The main loop of the watcher thread that checks for new input in the input pane
        and sends feedback to the feedback pane.
        This method runs in a loop until the thread is stopped.
        """
        while True:
            with open(self.log_file, "r") as f:
                f.seek(self.last_position)
                new_lines = f.readlines()
                self.last_position = f.tell()
            for line in new_lines:
                cleaned = line.strip()
                if cleaned:
                    self.attempt_count += 1
                    if self.validator(cleaned):
                        feedback = f"✅ Correct on attempt {self.attempt_count}!"
                    else:
                        feedback = f"❌ Incorrect. Attempt {self.attempt_count}."
                    self.feedback_pane.send_keys(f"echo -e '{feedback}'")

            time.sleep(self.interval)

    def stop(self):
        """
        Stop the watcher thread.
        """
        self.running = False