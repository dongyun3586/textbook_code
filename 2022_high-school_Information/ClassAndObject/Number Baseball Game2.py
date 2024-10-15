import random


class Player:
    def __init__(self, name=None):
        self.name = name
        self.numbers = random.sample(range(10), 3)  # 3 개의 랜덤 야구 숫자 생성
        print(f'{self.name} : {self.numbers}')

    def check_strike(self, guessed_nums):
        strike_count = ball_count = 0
        for i in range(3):
            if guessed_nums[i] == self.numbers[i]:
                strike_count += 1
            elif guessed_nums[i] in self.numbers:
                ball_count += 1
        print(f"{strike_count} Strike, {ball_count} Ball")
        return strike_count == 3


class Game:
    def __init__(self, players):
        self.players = players

    def play(self):
        game_round = 1
        while True:
            game_result = []
            print(f'\n{"*" * 15} Round {game_round} {"*" * 15}', end='')
            # Player별 추측 숫자 입력받고 스트라이크 판별하기
            for p in self.players:
                print(f"\n{p.name}'s turn : ", end=' ')
                input_numbers = list(map(int, input().split()))
                game_result.append(p.check_strike(input_numbers))
            game_round += 1

            # 결과 판별
            if self.check_gameover(game_result):
                break

    def check_gameover(self, game_result):
        if sum(game_result):
            print(f"\n\n{'<GAME OVER>':^40}");
            print('=' * 40)
            for i in range(len(game_result)):
                if game_result[i]:
                    print(f'{self.players[i].name} Win!')
            print('=' * 40)
            return True


if __name__ == "__main__":
    print(f"{'<NUMERIC BASEBALL GAME>':^40}")
    n = int(input("게임 참가자 숫자는?"))
    players = []
    for i in range(n):
        name = input(f"{i + 1}번째 참가자 이름 입력: ")
        players.append(Player(name))
    game = Game(players)
    game.play()
