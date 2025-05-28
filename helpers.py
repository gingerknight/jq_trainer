import libtmux

def shell_escape_single_quotes(s: str) -> str:
    return s.replace("'", "'\\''")

def bash_log_file(pane: libtmux.Pane) -> None:
    """
    Generate a log file path for a given tmux pane.
    The log file is named after the pane's unique identifier.
    """
    pane.send_keys('clear; bash ./jq_trainer_input.sh')

def validator(user_text: str) -> bool:
    """
    Checks if the input matches expected from the log file
    """
    if user_text == "cat olympics_2022.json| jq '.[0] | keys | length'":
        return True
    return False
