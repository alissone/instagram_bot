import time
import random

"""
Helper functions that will be used in every aspect of the project
"""


def wait(seconds) -> None:
    time.sleep(seconds + (random.randint(0, 9) / 10))


def progress_bar(current, total, message="processing..."):
    """Simple progress bar that should be replaced with tqdm later

    Args:
        current (int): current iteration
        total (int): total iterations
        message (str, optional): Will appear  on the left of progress 
        bar. Defaults to "processing...".
    """

    percent = (current / total) * 100
    print(str(message) + " " +
          "".join(["#" if percent >= x else "." for x in range(100)]) +
          " {:.2f}%".format(float(percent)) if current <= total else "",
          end="\r")
    if current == total or current == 0:
        print()


