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