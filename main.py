import time
import random
import os
import sys


def game_5(players):
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
                    print(f"{player_names[0]} 땡!")
                    return players[0]

                player = player_point(player_names)
                cnt += 1

            # 컴퓨터 차례인 경우
            else:
                failure = random.randint(1, 100)
                next_player = random.randint(0, len(players) - 1)

                # 실패 확률 20%
                if failure > 80:
                    answer = random.choice(
                        [x for x in ppang_list if x != ppang_list[cnt]]
                    )
                    print(f"{player_names[player]}: {answer}")
                    if answer != "으악!":
                        print(f"{player_names[next_player]}을/를 가르켰습니다!")
                    print(f"{player_names[player]} 땡!")
                    return players[player]
                # 성공 확률 80%
                else:
                    print(f"{player_names[player]}: {ppang_list[cnt]}")
                    print(f"{player_names[next_player]}을/를 가르켰습니다!")
                    cnt += 1
                    player = next_player

        # 여기 코드가 너무 더럽다고 생각하지 않는지~...

        # 으악!
        right = (player + 1) % len(players)
        left = (player - 1 + len(players)) % len(players)
        scream = player_scream()

        # 컴퓨터 틀릴 확률
        failure = random.randint(1, 100)

        # 나 으악! 할거양~
        if scream:
            print(f"{player_names[0]}: 으악! ヽ༼⊙_⊙༽ﾉ")
            # 내가 오른쪽이면?
            if right == 0:
                # 근데 컴퓨터가 실수할지도 몰랑!
                if failure > 80:
                    left_fail = random.choice(
                        [x for x in range(0, len(players)) if x not in [left, right]]
                    )
                    print(f"{player_names[left_fail]}: 으악! ヽ༼⊙_⊙༽ﾉ")
                    print(f"{player_names[left_fail]} 땡!")
                    return player_names[left_fail]
                else:
                    print(f"{player_names[left]}: 으악! ヽ༼⊙_⊙༽ﾉ")
            # 내가 왼쪽이면?
            elif left == 0:
                # 컴퓨터 실수 확률 추가
                if failure > 80:
                    right_fail = random.choice(
                        [x for x in range(0, len(players)) if x not in [left, right]]
                    )
                    print(f"{player_names[right_fail]}: 으악! ヽ༼⊙_⊙༽ﾉ")
                    print(f"{player_names[right_fail]} 땡!")
                    return player_names[right_fail]
                else:
                    print(f"{player_names[right]}: 으악! ヽ༼⊙_⊙༽ﾉ")
            # 둘 다 아니면?
            else:
                print(f"{player_names[0]} 땡!")
                return players[0]

        else:
            if right == 0 or left == 0:
                print(f"{player_names[0]} 땡!")
                return players[0]
            # 컴퓨터 실수 33
            ind = random.randint(0, 1)
            if failure > 80:
                if ind == 0:
                    left = random.choice(
                        [x for x in range(0, len(players)) if x not in [left, right, 0]]
                    )
                    print(f"{player_names[left]}: 으악! ヽ༼⊙_⊙༽ﾉ")
                    print(f"{player_names[left]} 땡!")
                    return players[left]
                else:
                    right = random.choice(
                        [x for x in range(0, len(players)) if x not in [left, right, 0]]
                    )
                    print(f"{player_names[right]}: 으악! ヽ༼⊙_⊙༽ﾉ")
                    print(f"{player_names[right]} 땡!")
                    return players[right]

            else:
                print(f"{player_names[left]}: 으악! ヽ༼⊙_⊙༽ﾉ")
                print(f"{player_names[right]}: 으악! ヽ༼⊙_⊙༽ﾉ")

        cnt = 0
