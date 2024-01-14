# Standard
import sys

# Pip
# None

# Custom
# None


import sys

def update_progress(progress:float , label: str) -> None :
    """
    Display a progress bar in the console.

    Args:
        progress (float): A value between 0 and 1 representing the progress.
        label (str): A label to display alongside the progress bar.

    Raises:
        ValueError: If progress is not a float or is outside the range [0, 1].
    
    Returns:
        None


    based on https://stackoverflow.com/a/15860757
    """
    
    # Modify this to change the length of the progress bar
    bar_length = 10
    status = ""

    if isinstance(progress, int):
        progress = float(progress)

    if not isinstance(progress, float):
        raise ValueError("error: progress var must be float")

    if progress < 0:
        progress = 0
        status = "Halt...\r\n"

    if progress >= 1:
        progress = 1
        status = "Done...\r\n"

    block = int(round(bar_length * progress))

    text = "\r{3}: [{0}] {1}% {2}".format(
        "#" * block + "-" * (bar_length - block), progress * 100, status, label
    )
    
    sys.stdout.write(text)
    sys.stdout.flush()
