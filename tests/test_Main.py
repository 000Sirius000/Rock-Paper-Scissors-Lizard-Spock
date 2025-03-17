import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import random
from main import RPSLSGame, Move

# Фікстура для створення гри з легким рівнем складності
@pytest.fixture
def game_easy():
    return RPSLSGame(difficulty="легкий")

# Фікстура для створення гри з неможливим рівнем (тобто 100% бачення ходу гравця)
@pytest.fixture
def game_impossible():
    return RPSLSGame(difficulty="неможливий")

# Тестування функції визначення переможця з використанням параметризації
@pytest.mark.unit
@pytest.mark.parametrize("player_move, computer_move, expected", [
    (Move.ROCK, Move.SCISSORS, "player"),
    (Move.PAPER, Move.ROCK, "player"),
    (Move.SCISSORS, Move.PAPER, "player"),
    (Move.LIZARD, Move.SPOCK, "player"),
    (Move.SPOCK, Move.SCISSORS, "player"),
    (Move.ROCK, Move.ROCK, None),
    (Move.ROCK, Move.PAPER, "computer"),
])
def test_determine_winner(game_easy, player_move, computer_move, expected):
    result = game_easy.determine_winner(player_move, computer_move)
    assert result == expected

# Тестування методу get_computer_move з мокуванням випадкового числа та вибору
@pytest.mark.unit
def test_get_computer_move_sees_player_move(game_impossible, monkeypatch):
    player_move = Move.ROCK
    # Мокаємо random.random, щоб завжди поверталося значення нижче порогу
    monkeypatch.setattr(random, "random", lambda: 0.0)
    # Мокаємо random.choice для детермінованого результату (наприклад, завжди повертаємо Move.PAPER, що є виграшним проти ROCK)
    monkeypatch.setattr(random, "choice", lambda lst: Move.PAPER if Move.PAPER in lst else lst[0])
    computer_move = game_impossible.get_computer_move(player_move)
    assert computer_move == Move.PAPER

# Тестування методу get_player_move за допомогою monkeypatch (імітація введення користувача)
@pytest.mark.unit
def test_get_player_move(game_easy, monkeypatch):
    # Імітуємо спочатку невірне введення, а потім коректне "rock"
    inputs = iter(["invalid", "rock"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    move = game_easy.get_player_move()
    assert move == Move.ROCK

# Тестування методу choose_difficulty за допомогою monkeypatch
@pytest.mark.unit
def test_choose_difficulty(game_easy, monkeypatch, capsys):
    # Імітуємо спочатку невірний рівень, а потім правильний "важкий"
    inputs = iter(["wrong", "важкий"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    game_easy.choose_difficulty()
    captured = capsys.readouterr().out
    assert "Рівень складності змінено" in captured
    assert game_easy.difficulty == "важкий"

# Тестування одного раунду гри (play_round) за допомогою мокування внутрішніх методів
@pytest.mark.unit
def test_play_round(game_easy, monkeypatch, capsys):
    # Мокаємо методи, щоб отримати завжди задані ходи: гравець - ROCK, комп'ютер - SCISSORS
    monkeypatch.setattr(game_easy, "get_player_move", lambda: Move.ROCK)
    monkeypatch.setattr(game_easy, "get_computer_move", lambda player_move: Move.SCISSORS)
    winner = game_easy.play_round()
    captured = capsys.readouterr().out
    assert "Ви перемогли" in captured
    assert winner == "player"
