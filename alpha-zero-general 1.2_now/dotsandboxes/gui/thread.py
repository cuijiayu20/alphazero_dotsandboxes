import threading

from dotsandboxes.pitdotsandboxes import run_pit
from dotsandboxes.gui.main import GUI

if __name__ == "__main__":
    gui=GUI()
    add_thread = threading.Thread(target=run_pit)
    print_thread = threading.Thread(target=gui.create_board)  # remove the parentheses

    add_thread.start()
    print_thread.start()