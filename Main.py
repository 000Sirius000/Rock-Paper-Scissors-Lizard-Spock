import random
import argparse
from enum import Enum

# Перерахування можливих ходів
class Move(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    LIZARD = 'lizard'
    SPOCK = 'spock'

class RPSLSGame:
    """
    Клас для гри "Rock Paper Scissors Lizard Spock".
    Принципи SOLID забезпечують чітке розділення відповідальностей,
    DRY – уникнення дублювання коду, KISS – простоту реалізації.
    """
    # Правила перемоги: кожен хід перемагає перелічені ходи.
    WINNING_MOVES = {
        Move.ROCK: [Move.SCISSORS, Move.LIZARD],
        Move.PAPER: [Move.ROCK, Move.SPOCK],
        Move.SCISSORS: [Move.PAPER, Move.LIZARD],
        Move.LIZARD: [Move.SPOCK, Move.PAPER],
        Move.SPOCK: [Move.ROCK, Move.SCISSORS],
    }

    # Ймовірність того, що комп'ютер "бачить" хід гравця залежно від складності
    DIFFICULTY_PROB = {
        "легкий": 0.0,
        "середній": 0.5,
        "важкий": 0.9,
        "неможливий": 1.0,
    }

    def __init__(self, difficulty="легкий"):
        """
        Ініціалізує гру з обраним рівнем складності.
        :param difficulty: один із рівнів: "легкий", "середній", "важкий", "неможливий"
        """
        self.moves = list(Move)
        if difficulty not in self.DIFFICULTY_PROB:
            raise ValueError("Невірний рівень складності!")
        self.difficulty = difficulty

    def get_player_move(self):
        """
        Запитує хід гравця в циклі до отримання коректного введення.
        """
        valid_moves = [move.value for move in self.moves]
        while True:
            user_input = input(f"Введіть ваш хід ({', '.join(valid_moves)}): ").strip().lower()
            for move in self.moves:
                if user_input == move.value:
                    return move
            print("Невірний хід. Спробуйте ще раз.")

