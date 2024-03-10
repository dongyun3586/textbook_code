import random

class Player:
    """ 숫자 야구 게임의 플레이어 클래스
    각 플레이어는 고유한 이름, 3개의 랜덤 숫자를 속성으로 갖고,
    check_strike() 함수로 모든 숫자를 맞힌 결과를 반환함."""
    def __init__(self, name=None):
        self.name = name
        self.numbers = random.sample(range(10), 3)   # player의 3 개의 랜덤 야구 숫자 생성
        print(f"{self.name}: {self.numbers}")

    def check_strike(self, guessed_nums) -> bool:
        """ guessed_nums에서 strike와 ball의 개수를 체크하고, 모든 숫자를 맞힌 결과를 반환함. """
        strike_count = ball_count = 0
        for i in range(3):
            if guessed_nums[i] == self.numbers[i]:
                strike_count += 1
            elif guessed_nums[i] in self.numbers:
                ball_count += 1
        print(f"{strike_count} Strike, {ball_count} Ball")
        return strike_count == 3

class Game:
    """ 숫자 야구 게임 클래스
    모든 Player 관리, 게임 라운드 관리, 게임 종료 결정
    세 개의 숫자를 모두 올바른 순서로 맞출 때까지 게임이 계속 진행됨."""
    def __init__(self, players):
        self.players = players

    def play(self):
        """
        승자가 나올 때까지 게임 라운드 관리, 예측 숫자 입력받기, 스트라이크&볼 판정, 게임 종료 체크
        """
        game_round = 1
        while True:
            game_result = []
            print(f'\n{"*" * 15} Round {game_round} {"*" * 15}', end='')

            # Player별 추측 숫자 입력받고 스트라이크 판별하기
            for p in self.players:
                guessed_nums = list(map(int, input(f"\n{p.name}'s turn : ").split()))
                game_result.append(p.check_strike(guessed_nums))
            game_round += 1

            # 모든 숫자를 맞힌 참가자가 있으면 게임 종료
            if self.check_gameover(game_result):
                break

    def check_gameover(self, game_result) -> bool:
        """ 모든 플레이어에 대해 게임 종료(3 strikes) 여부 판별 """
        if sum(game_result):
            print(f"\n\n{'<GAME OVER>':^40}"); print('=' * 40)
            for i in range(len(game_result)):
                if game_result[i]:
                    print(f'{self.players[i].name} Win!')
            print('=' * 40)
            return True


if __name__ == "__main__":
    print(f"{'<NUMERIC BASEBALL GAME>':^40}")
    n = int(input("게임 참가자 숫자는?"))
    players = [Player(input(f"{i+1}번째 참가자 이름 입력: ")) for i in range(n)]
    game = Game(players)
    game.play()
