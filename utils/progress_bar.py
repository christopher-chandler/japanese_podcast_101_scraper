# Standard
import sys

# Pip
#

# Custom
#


def update_progress(progress, label:str):

    # Modify this to change the length of the progress bar
    bar_length = 10
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(bar_length * progress))

    text = "\r{3}: [{0}] {1}% {2}".format("#" * block + "-" * (bar_length - block),
                                          progress * 100, status, label)
    sys.stdout.write(text)
    sys.stdout.flush()
