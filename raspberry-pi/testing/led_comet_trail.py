import time

import adafruit_dotstar as dotstar
import board

# LED strip configuration
NUM_LEDS = 20
BRIGHTNESS = 0.3  # Adjust the brightness as needed

# Create a DotStar instance
spi = board.SPI()
# strip = dotstar.DotStar(spi, board.D5, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)
strip = dotstar.DotStar(board.SCK, board.MOSI, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

# Comet settings
COMET_SIZE = 5  # Length of the comet
COMET_SPEED = 0.05  # Speed of the effect


def generate_gradient(start_color, end_color, steps):
    """ Generate a gradient between two colors """
    gradient = []
    for step in range(steps):
        intermediate_color = [
            start_color[j] + (end_color[j] - start_color[j]) * step / (steps - 1)
            for j in range(3)
        ]
        gradient.append(tuple(map(int, intermediate_color)))
    return gradient


# Define start and end colors of the comet (RGB)
start_color = (0, 0, 255)  # Bright blue
end_color = (100, 100, 255)  # Lighter blue

# Generate the color gradient
color_gradient = generate_gradient(start_color, end_color, COMET_SIZE)


def comet_effect(strip, comet_size, comet_speed, color_gradient):
    while True:
        for start_pos in range(-comet_size, NUM_LEDS):
            strip.fill((0, 0, 0))  # Turn off all LEDs

            # Draw the comet
            for i in range(comet_size):
                pos = start_pos + i
                if 0 <= pos < NUM_LEDS:
                    strip[pos] = color_gradient[i]

            strip.show()
            time.sleep(comet_speed)


try:
    comet_effect(strip, COMET_SIZE, COMET_SPEED, color_gradient)
except KeyboardInterrupt:
    strip.fill((0, 0, 0))
    strip.show()
