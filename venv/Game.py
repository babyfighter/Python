class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("help")

    @classmethod
    def show_top_score(cls):
        print("History %d" %cls.top_score)

    def start_game(self):
        print("%s starts game" % self.player_name)


game = Game("xm")
game.start_game()
