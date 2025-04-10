"""
8 kyu - Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.
Examples(Input1, Input2 --> Output):
"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
"""


def rps(p1, p2):
    match (p1, p2):
        case ("scissors", "paper"):
            return f"Player 1 won!"
        case ("scissors", "rock"):
            return f"Player 2 won"
        case ("paper", "scissors"):
            return f"Player 2 won"
        case ("paper", "rock"):
            return f"Player 1 won"
        case ("rock", "paper"):
            return f"Player 2 won"
        case ("rock", "scissors"):
            return f"Player 1 won"
        case _:
            return f"Draw"


print(rps("scissors", "rock"))
