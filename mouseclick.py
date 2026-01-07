import sys
from pynput.mouse import Button, Controller


def main(x, y, mode):
    mouse = Controller()

    if mode == 3:  # scroll up
        scroll_amount = int(sys.argv[4]) if len(sys.argv) > 4 else 5
        mouse.position = (x, y)
        mouse.scroll(0, -scroll_amount)
    elif mode == 4:  # scroll down
        scroll_amount = int(sys.argv[4]) if len(sys.argv) > 4 else 5
        mouse.position = (x, y)
        mouse.scroll(0, scroll_amount)
    else:
        mouse.position = (x, y)
        mouse.click(Button.left, mode)
    # mouse.press(x, y, mode)
    # time.sleep(0.1)
    # mouse.release(x, y, mode)


if __name__ == "__main__":
    x, y, mode = int(sys.argv[1]) + 20, int(sys.argv[2]) + 20, int(sys.argv[3])
    main(x, y, mode)
