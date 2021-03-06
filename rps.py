import random

moves = ["rock", "paper", "scissors"]


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass

    def beats(self, one, two):
        if (
            (one == "rock" and two == "scissors") or
            (one == "scissors" and two == "paper") or
            (one == "paper" and two == "rock")
        ):
            return "player1"
        elif one == two:
            return "tie"
        else:
            return "player2"


class RandomPlayer(Player):
    def move(self):
        random_move = random.choice(moves)
        return random_move


class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input("Rock, paper,scissors?\n").lower()
            if human_move in moves:
                return human_move
            else:
                print("Invalid input: type rock, paper, scissors")


class ReflectPlayer(Player):
    def __init__(self):
        self.opp = "rock"

    def learn(self, m1, m2):
        self.opp = m2

    def move(self):
        reflection = self.opp
        return reflection


class CyclePlayer(Player):
    def __init__(self):
        self.last = "rock"

    def learn(self, m1, m2):
        self.last = m1

    def move(self):
        lastmove = self.last
        moves_lst = ["rock", "paper", "scissors"]
        moves_lst.remove(lastmove)
        currentmove = random.choice(moves_lst)
        return currentmove


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.win = 0
        self.p2.win = 0
        self.round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}")
        print(f"Opponent played {move2}")
        result1 = self.p1.beats(move1, move2)
        if result1 == "player1":
            self.p1.win += 1
            print ("**Player 1 wins**")
        elif result1 == "player2":
            self.p2.win += 1
            print ("**Player 2 wins**")
        else:
            print("**Tie**")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        while True:
            q = input("Type quit if you want to quit."
                      "Type 'yes' to continue").lower()
            if "quit" in q:
                break
            print(f"Round {self.round}:")
            self.play_round()
            print (f"Score: Player One {self.p1.win},"
                   f"Player Two {self.p2.win}")
            self.round += 1
        print (f"Final Score: Player One {self.p1.win},"
               f"Player Two {self.p2.win}")
        print("Game over!")


if __name__ == "__main__":
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
