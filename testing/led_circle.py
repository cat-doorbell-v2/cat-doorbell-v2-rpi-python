import sys

import adafruit_dotstar as dotstar
import board

# Number of LEDs on your strip
num_pixels = 20  # Adjust this to match the number of LEDs you have
pixels = dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=0.2)


def set_leds(r, g, b):
    """Set all LEDs to the specified RGB color."""
    for i in range(num_pixels):
        pixels[i] = (r, g, b)
    pixels.show()


def turn_off_pixels():
    """Turn off all pixels."""
    set_leds(0, 0, 0)


# Main program logic
if len(sys.argv) == 4:
    # Parse RGB values from command line arguments
    r, g, b = [int(val) for val in sys.argv[1:4]]
    set_leds(r, g, b)
else:
    turn_off_pixels()
