from player_reader import PlayerReader
import datetime

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        playerlist = []
        for player in self.players:
            if player.nationality == nationality:
                playerlist.append(player)

        time = datetime.datetime.now()

        playerlist.sort(key=lambda x: x.points, reverse=True)

        print("Top scorers from " + nationality + " " + str(time) + "\n")
        for player in playerlist:
            print(f"{player.name:23}" + player.team + " " + str(player.goals) +
                  " + " + str(player.assists) + " = " + str(player.points))
