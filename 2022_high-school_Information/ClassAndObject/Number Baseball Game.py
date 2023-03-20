import random


class Player:
    def __init__(self, name=None):
        self.name = name

        # 3 개의 랜덤 야구 숫자 생성
        self.numbers = random.sample(range(1, 10), 3)
        print(self.numbers)

    def check_strike(self, guess_numbers):
        strike_count = ball_count = 0
        for i in range(3):
            if guess_numbers[i] == self.numbers[i]:
                strike_count += 1
            elif guess_numbers[i] in self.numbers:
                ball_count += 1
        print(f"{strike_count} Strike, {ball_count} Ball")
        return strike_count == 3


class Game:
    def __init__(self, *players):
        self.players = []
        for i in players:
            self.players.append(i)

    def play(self):
        round = 1
        while True:
            results = []
            print(f'\n{"*" * 15} Round {round} {"*" * 15}', end='')
            for i, p in enumerate(self.players):
                print(f"\nPlayer{i + 1}({p.name})'s turn : ", end=' ')
                input_numbers = list(map(int, input().split()))
                results.append(p.check_strike(input_numbers))
            print('*' * 40)
            print('results', results)
            round += 1

            # 결과 판별
            if sum(results):
                print(f"\n{'GAME OVER':^40}")
                print('=' * 40)
                for i in range(len(results)):
                    if results[i]:
                        print(f'Player{i + 1} Win!!!')
                print('=' * 40)
                return

    def display(self, *numbers):
        for p in self.players:
            print(f'{p.name:20}', end='')


if __name__ == "__main__":
    players = Player(name='player1'), Player(name='player2'), Player(name='player3')
    game = Game(*players)
    game.play()
