import json


class GameStats():
    """Tracks relevant game statistics and activity flag"""

    def __init__(self, settings):
        """Initializes gamestats object"""
        self.settings = settings
        self.high_score = self.load_high_score()
        self.reset_stats()
        # Check for prexisting high score and load in

    def reset_stats(self):
        """Sets game stats to game-start defaults"""
        self.game_active = False
        self.lives = self.settings.lives
        self.level = 1
        self.score = 0

    def score_increase(self, num_aliens):
        """Increases score based on number of aliens destroyed"""
        self.score += num_aliens * self.settings.alien_points

    def set_high_score(self):
        """Sets new high score if needed"""
        if self.score > self.high_score:
            self.high_score = self.score

    def load_high_score(self):
        """Retrieves high score from json file if it exists"""
        try:
            with open("high_score.json") as hs:
                return json.load(hs)
        except:
            return 0

    def save_high_score(self):
        """Sets new high score in high_score.json"""
        with open("high_score.json", "w") as hs:
            json.dump(self.high_score, hs)
