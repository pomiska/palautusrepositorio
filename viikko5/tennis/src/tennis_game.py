class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.equal_scores = ["Love-All", "Fifteen-All",
                             "Thirty-All", "Forty-All", "Deuce"]
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.equal_scores[self.player1_score]

        if self.player1_score >= 4 or self.player2_score >= 4:
            player1_leading_by = self.player1_score - self.player2_score

            if player1_leading_by == 1:
                return "Advantage player1"
            elif player1_leading_by == -1:
                return "Advantage player2"
            elif player1_leading_by >= 2:
                return "Win for player1"
            else:
                return "Win for player2"

        return self.scores[self.player1_score] + "-" + self.scores[self.player2_score]
