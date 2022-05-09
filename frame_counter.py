class FrameCounter():
    """Counts number of frames as a way of telling time in game"""

    def __init__(self):
        """Sets counter to 0"""
        self.reset_counter()

    def reset_counter(self):
        """resets counter to 0"""
        self.counter = 0

    def tick(self):
        """Increases frame counter by 1"""
        self.counter += 1
