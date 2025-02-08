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

    def get_computer_move(self, player_move):
        """
        Обирає хід для комп'ютера.
        Залежно від рівня складності, комп'ютер може «бачити» хід гравця:
          - Якщо випадкове число менше встановленої ймовірності,
            комп'ютер обирає хід, що переможе хід гравця.
          - Інакше комп'ютер обирає випадковий хід.
        :param player_move: хід, зроблений гравцем.
        """
        chance_to_see = self.DIFFICULTY_PROB[self.difficulty]
        if random.random() < chance_to_see:
            # Комп'ютер бачить хід гравця – шукаємо хід, який переможе вибір гравця.
            winning_moves = [move for move in self.moves if player_move in self.WINNING_MOVES[move]]
            if winning_moves:
                return random.choice(winning_moves)
        return random.choice(self.moves)

    def play_round(self):
        """
        Провадить один раунд гри: отримує ходи, визначає переможця і виводить результат.
        """
        player_move = self.get_player_move()
        computer_move = self.get_computer_move(player_move)
        winner = self.determine_winner(player_move, computer_move)
        print(f"\nВи обрали: {player_move.value.capitalize()}. Комп'ютер обрав: {computer_move.value.capitalize()}.")
        if winner is None:
            print("Нічия!")
        elif winner == "player":
            print("Ви перемогли!")
        else:
            print("Комп'ютер переміг!")
        print("-" * 40)
        return winner