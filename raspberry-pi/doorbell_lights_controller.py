"""
DoorBellLightsController Class for APA102-2020 LED Strip

This class allows you to control lights based on a dark indicator sensor using a motion sensor or other sensor.
It manages turning on and off the lights based on the darkness detected by the sensor.

Example Usage:
1. Create a logger to capture events and initialize the DoorBellLightsController.
2. Continuously check and control the lights based on darkness conditions.

"""

import logging
import sys
import time

import RPi.GPIO as GPIO
# Import necessary libraries for APA102
import adafruit_dotstar
import board


class DoorBellLightsController:
    """
    Controller for managing APA102-2020 LED strip lights associated with a doorbell.

    Args:
        dark_indicator_pin (int): The GPIO pin number connected to the dark indicator sensor.
        ci_pin (board.Pin): Clock Interface pin for the APA102 LEDs.
        di_pin (board.Pin): Data Interface pin for the APA102 LEDs.
        logger (logging.Logger, optional): The logger to use for logging events. Defaults to None.
        max_pixels (int, optional): The maximum number of pixels in the LED strip. Defaults to 20.

    Attributes:
        dark_indicator_pin (int): The GPIO pin number connected to the dark indicator sensor.
        ci_pin (board.Pin): Clock Interface pin for the APA102 LEDs.
        di_pin (board.Pin): Data Interface pin for the APA102 LEDs.
        max_pixels (int): The maximum number of pixels in the LED strip.
        logger (logging.Logger or None): The logger used for logging events.

    Methods:
        _is_dark(): Check if it's dark based on the dark indicator sensor.
        turn_on(): Turn on the lights if it's dark and log the event.
        turn_off(): Turn off the lights.
    """
    LIGHTS_ON = (255, 255, 255)  # White
    LIGHTS_OFF = (0, 0, 0)  # Black

    def __init__(self, dark_indicator_pin, ci_pin, di_pin, logger=None, max_pixels=20):
        self.dark_indicator_pin = dark_indicator_pin
        self.ci_pin = ci_pin
        self.di_pin = di_pin
        self.max_pixels = max_pixels
        self.logger = logger

        # Initialize APA102 LED strip
        self.pixels = adafruit_dotstar.DotStar(self.ci_pin, self.di_pin, self.max_pixels, brightness=0.5,
                                               auto_write=False)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.dark_indicator_pin, GPIO.IN)

    def _is_dark(self):
        dark = bool(GPIO.input(self.dark_indicator_pin))
        print(f"dark: {dark}")
        return dark

    def turn_on(self):
        if self._is_dark():
            self.pixels.fill(DoorBellLightsController.LIGHTS_ON)
            self.pixels.show()
            if self.logger:
                self.logger.info("Lights turned ON")

    def turn_off(self):
        self.pixels.fill(DoorBellLightsController.LIGHTS_OFF)
        self.pixels.show()
        if self.logger:
            self.logger.info("Lights turned OFF")

if __name__ == "__main__":
    # Example usage with logger
    dark_pin = 17  # Physical pin 11
    ci_pin = board.D11  # Clock Interface pin
    di_pin = board.D10  # Data Interface pin

    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)

    controller = DoorBellLightsController(dark_pin, ci_pin, di_pin, logger=logger)

    while True:
        controller.turn_on()  # Turn on the lights if it's dark and log the event
        time.sleep(30)  # Wait for 30 seconds
        controller.turn_off()  # Turn off the lights
        time.sleep(30)  # Wait for 30 seconds
