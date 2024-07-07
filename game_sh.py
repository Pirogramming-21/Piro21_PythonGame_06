import random
import time
from main import line_print

def select_targets(players):
    targets = {}
    players_name = [player[0] for player in players]
    
    for player in players:
        if player == players[0]:
            while True:
                avaliable_targets_name = [name for name in players_name if name != player[0]]
                print(f'~~~~~~~~~~   🎯  지목 가능한 플레이어 목록: {avaliable_targets_name}  ~~~~~~~~~~')
                target = input(f"                  ✅ 누구를 지목할건가요? : ")
                if target in avaliable_targets_name:
                    line_print()
                    break
                else:
                    print("올바른 플레이어를 선택해주세요.")
        else:
            avaliable_targets_name = players_name[:]
            avaliable_targets_name.remove(player[0])
            target = random.choice(avaliable_targets_name)
        
        targets[player[0]] = target
        print(f"                         {player[0]}   👉   {target}")
    
    line_print()
    return targets

def move_count():
    while True:
        try:
            moves = int(input("                  ✅ 몇 번 이동할까요? (2 이상 15 이하): "))
            if 2 <= moves <= 15:
                print(f'\n   🎯  {moves} 번 이동합니다!')
                line_print()
                return moves
            else:
                print("2에서 15 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("숫자를 입력해주세요.")

def pass_bomb(players, targets, moves):
    current_holder = random.choice(players)[0]
    print(f"\n   🍺  {current_holder} 부터 시작합니다!\n\n")
    time.sleep(1)
    
    for i in range(moves):
        next_holder = targets[current_holder]
        remaining_moves = moves - (i + 1)
        print(f"💣 {i + 1}번째 !! |  {current_holder}   👉   {next_holder}  |  남은 횟수 ...{remaining_moves}")
        print('')
        current_holder = next_holder
        time.sleep(1)
    
    print(f'.\n.\n.\n')
    time.sleep(1)

    print("🤯  🤯  🤯  당첨!!  🤯  🤯  🤯")

    time.sleep(1)
    line_print()
    return current_holder

def play_game(players):
    targets = select_targets(players)
    moves = move_count()
    
    loser = pass_bomb(players, targets, moves)
    
    print(f"\n🍺 패배자는~~~~~~ ✨ {loser} ✨ !!")
    return loser

# 플레이어 리스트
players = [('player1', 0, 0), ('com1', 0, 0), ('com2', 0, 0), ('com3', 0, 0)]

# 게임 실행
play_game(players)