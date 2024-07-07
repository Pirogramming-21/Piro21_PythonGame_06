# players 사용하시면 list 정보가 있고


# 마지막에 loser 리턴해야합니다
import time
import random
import os
import sys


def ppang_intro():
    print("빠밤빠밤⎝⍢⎠ 빠바밤( -_•)╦̵̵̿╤─")
    print("빠밤빠밤(●_-)–ε/̵͇̿/’̿’̿ ̿ ̿ ̿ 💥 빠바밤⎝⍥⎠")


def ppang_player_input(ppang_list):
    answer = input("당신의 행동을 입력하세요(공, 칠, 빵, 으악!): ")
    while answer not in ppang_list:
        answer = input('"공", "칠", "빵", "으악!"을 입력하세요: ')
    return answer


def player_point(player_names):
    print("플레이어: ", end="")
    for p in player_names:
        print(p, end=" ")
    player = input("지목할 사람을 입력하세요: ")
    while player not in player_names:
        player = input("잘못된 사람을 지목하였습니다. 다시 지목해주세요: ")
    return player_names.index(player)


def player_scream():
    scream = input("으악! 을 하시겠습니까? Y/N: ")
    while scream not in ["Y", "y", "N", "n"]:
        scream = input("으악! 을 하시겠습니까? Y/N: ")
    if scream in ["Y", "y"]:
        return True
    else:
        return False


def game_5(players):
    player_names = [player[0] for player in players]
    ppang_intro()
    ppang_list = ["공", "공", "칠", "빵", "으악!"]  # ヽ༼⊙_⊙༽ﾉ

    player = 0
    cnt = 0

    while True:
        # 공 공 칠 빵!
        while cnt < 4:
            # "내" 차례인 경우
            if player == 0:
                answer = ppang_player_input(ppang_list)
                if answer != ppang_list[cnt]:
                    return players[0]

                player = player_point(player_names)
                cnt += 1

            # 컴퓨터 차례인 경우
            else:
                #!!!!!!!!!!!!실패할 확률 추가하기
                print(f"{player_names[player]}: {ppang_list[cnt]}")
                player = random.randint(0, len(players) - 1)
                print(f"{player_names[player]}을/를 가르켰습니다!")
                cnt += 1

        # 으악!
        right = (player + 1) % len(players)
        left = (player - 1 + len(players)) % len(players)
        scream = player_scream()

        # 으악! 하면 안 되는데 으악! 했을 때
        if scream and (right != 0 or left != 0):
            return players[0]

        print(f"{player_names[right]}: 으악! ヽ༼⊙_⊙༽ﾉ")
        print(f"{player_names[left]}: 으악! ヽ༼⊙_⊙༽ﾉ")
        cnt = 0


players = [("은서", 10), ("하연", 10), ("연서", 10)]
loser = game_5(players)
