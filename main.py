import os
import sys
import random
import time

players = []
games = []


def wait():
    time.sleep(0.2)


def line_print():
    columns, _ = os.get_terminal_size() # 터미널 너비
    print("~" * columns)


def drink_soju(loser, players):
    for i, player in enumerate(players):
        if player == loser:
            players[i] = (player[0], player[1] - 1, player[2] + 1)
    wait()


def current_status(players):
    line_print()
    for player in players:
        print(f'{player[0]}은(는) 지금까지 {player[2]}🍺! 치사량까지 {player[1]}')
    line_print()


def alcohol_game_list():
    print('''~~~~~~~~~~~~~~~~~~~  🍺 오늘의 Alcohol GAME 🍺  ~~~~~~~~~~~~~~~~~~~~~
                     🍺 1. 베스킨~라빈스~ 31🍦 
                     🍺 2. 💕좋아 게임
                     🍺 3. GO BACK JUMP!
                     🍺 4. 3-6-9 게임
                     🍺 5. 두부 게임
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')


def random_game_com(player):
    name = player[0]
    random_index = random.randint(1, 5)
    print(f'{name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : {random_index}')
    wait()
    line_print()
    print(f'{name} 님이 게임을 선택하셨습니다! 😊')
    print('')
    line_print()
    wait()
    return random_index


def random_game_player(player):
    name = player[0]
    while True:
        try:
            game_index = int(input(f'{name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : '))
            if game_index in range(1, 6):
                break
            else:
                print('1 ~ 5번 게임 중 하나를 선택해주세요.')
        except ValueError:
            print('정수를 입력해주세요.')
    line_print()
    print(f'{name} 님이 게임을 선택하셨습니다! 😊')
    print('')
    line_print()
    wait()
    return game_index


def ask_if_continue():
    if input('술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"를, 계속하고 싶으면 아무키나 입력해 주세요! : ').lower() == 'exit':
        print('게임을 종료합니다.')
        sys.exit()  # 전체 코드 강제종료
    else:
        pass


## 게임 목록 - 각자 게임 만든 후 삽입하기
## 플레이어 목록 : players --> players[0]은 실제 사용자, 나머지는 AI
## 게임 종료 시 return loser --> players[i]의 형식으로 패배자 플레이어 1명 선택할 것.

def game_1(players):  # 베스킨라빈스
    print('GAME START')
    print('베스킨라빈스')

    # 플레이어 2~4명. index[0]이 실제 플레이어. 나머지는 컴퓨터.
    loser = random.choice(players)  # 실제로는 random 대신 게임에서 진 사람 선택!
    return loser


def game_2(players):  # 좋아 게임
    print('GAME START')
    print('좋아 게임')

    loser = random.choice(players)  # 실제로는 random 대신 게임에서 진 사람 선택!
    return loser


def game_3(players, user_name):
    print('GAME START')
    print('고백점프')

    def contains_369(num):
        """Check if a number contains 3, 6, or 9"""
        return any(d in '369' for d in str(num))

    def get_gobackjump_response(num):
        """Get the correct response for a number containing 3, 6, or 9"""
        if num % 3 == 0:
            return "고"
        elif num % 6 == 0:
            return "백"
        else:
            return "점프"

    def next_player(current_index, step=1):

        return (current_index + step) % len(players)

    # Find the index of the user_name in players
    current_index = next(i for i, player in enumerate(players) if player[0] == user_name)
    count = 1

    while True:
        current_player = players[current_index][0]
        print(f'{current_player}의 차례입니다! ({count})')
        computer_response = ""
        if contains_369(count):
            correct_response = get_gobackjump_response(count)
            if current_player == user_name:
                user_response = input(f'{count}에는 뭐라고 대답해야 할까요? (고/백/점프): ').strip()

                # 사용자가 고, 백, 점프 중 하나를 입력했는지 확인
                if user_response not in ["고", "백", "점프"]:
                    print("다른거를 말해서 게임 아웃입니다ㅏ!!!.")
                    loser = players[current_index]

                    return loser  # 게임 종료: 잘못된 입력



            else:
                # 컴퓨터 플레이어의 임의 응답
                responses = ["고", "백", "점프", "3", "9", "11", "6", "15"]
                computer_response = random.choice(responses)
                print(f'{current_player}이(가) {computer_response}이라고 대답했습니다.')
                a=current_player
                if computer_response.isdigit():
                    print(f'오답입니다! {a}이(가) {correct_response} 대신 {computer_response}이라고 했습니다.')
                    loser = players[current_index]
                    return loser  # 게임 종료

            # 다음 플레이어 결정
            if computer_response == "고" or user_response == "고":
                current_index = next_player(current_index)
            elif computer_response == "백" or user_response == "백":
                players.reverse()
                current_index = next_player(current_index - 1)

            elif computer_response == "점프" or user_response == "점프":
                current_index = next_player(current_index, 2)
        else:
            if current_player == user_name:
                user_response = input(f'{current_player}, 답을(를) 외쳐주세요: ').strip()
                a=current_player
                if user_response != str(count):
                    print(f'오답입니다! {a}이(가) {count} 대신 {user_response}이라고 했습니다.')
                    loser = players[current_index]
                    return loser  # 게임 종료
            else:
                print(f'{current_player}이(가) {count}을(를) 외쳤습니다!')

            current_index = next_player(current_index)

        count += 1

        # 플레이어 순서 출력
        print("현재 순서:", " -> ".join(player[0] for player in players[current_index:] + players[:current_index]))

        if count > 100:  # 임시 조건: 무한 루프 방지
            break


def game_4(players):  # 369 게임
    print('GAME START')
    print('369 게임')
    loser = random.choice(players)  # 실제로는 random 대신 게임에서 진 사람 선택!
    return loser


def game_5(players):  # 두부 게임
    print('GAME START')
    print('두부 게임')
    loser = random.choice(players)  # 실제로는 random 대신 게임에서 진 사람 선택!
    return loser


def playing_game(game_index, players):
    games = [game_1, game_2, game_3, game_4, game_5]
    game_index = int(game_index)
    line_print()
    print('''
    ███╗   ██╗██╗ ██████╗███████╗ ██████╗  █████╗ ███╗   ███╗███████╗
    ████╗  ██║██║██╔════╝██╔════╝██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ██╔██╗ ██║██║██║     █████╗  ██║  ███╗███████║██╔████╔██║█████╗  
    ██║╚██╗██║██║██║     ██╔══╝  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ██║ ╚████║██║╚██████╗███████╗╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                    ''')
    line_print()
    wait()
    game_to_play = games[game_index - 1]
    if game_index == 3:  # game_3는 인자가 필요함
        game_loser = game_to_play(players, players[0][0])
    else:
        game_loser = game_to_play(players)

    print(f'아 누가누가 술을 마셔😮 {game_loser[0]}이(가) 술을 마셔😖 원~~~샷✨✨')
    drink_soju(game_loser, players)


def main():
    ### 1. 게임 시작 ###

    line_print()
    print('''
 ______     __         ______     ______     __  __     ______     __        
/\  __ \   /\ \       /\  ___\   /\  __ \   /\ \_\ \   /\  __ \   /\ \       
\ \  __ \  \ \ \____  \ \ \____  \ \ \/\ \  \ \  __ \  \ \ \/\ \  \ \ \____  
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\ 
  \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_____/ 

                ______     ______     __    __     ______                                
               /\  ___\   /\  __ \   /\ "-./  \   /\  ___\                               
               \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\                               
                \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\                             
                 \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/                             

    ''')
    line_print()
    wait()
    print('₍₍ ◝(・ω・)◟ ⁾⁾ 안주 먹을🍗 시간이⏰ 없어요🙅 마시면서 배우는 술게임🍺✨ ₍₍ (ว ˘ω˘ )ง ⁾⁾')
    line_print()
    wait()

    while True:
        start_game = input('게임을 진행할까요? (y/n) : ').strip().lower()  # 공백제거, 소문자화
        if start_game == 'y':
            break
        elif start_game == 'n':
            print('게임을 종료합니다.')
            sys.exit()  # 전체 코드 강제종료
        else:
            print('잘못된 입력입니다. 다시 입력해주세요.')

    ### 2. 사용자 이름 받기 ###

    my_name = input('오늘 거하게 취해볼 당신의 이름은?: ')

    ### 3. 본인 주량 선택하기 ###

    print('''
    ~~~~~~~~~~~~~~~~~~ 🍺 소주 기준 당신의 주량은? 🍺 ~~~~~~~~~~~~~~~~~~~~
                        🍺 1. 소주 반병 (2잔)
                        🍺 2. 소주 반병에서 한병 (4잔)
                        🍺 3. 소주 한병에서 한병 반 (6잔)
                        🍺 4. 소주 한병 반에서 두병 (8잔)
                        🍺 5. 소주 두병 이상 (10잔)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

    while True:
        try:
            my_drink_choice = int(input('당신의 치사량(주량)은 얼마인가요? (1~5를 선택해주세요): '))
            if my_drink_choice in range(1, 6):
                break
            else:
                print('1~5를 선택해주세요.')
        except ValueError:
            print('정수를 입력해주세요.')

    my_drink = my_drink_choice * 2
    line_print()

    ### 4. 같이 대결할 사람 초대하기 & 게임 리스트 출력하기 ###

    # players 리스트 안에 이름, 잔여 치사량, 패배카운트 표기! / players[0]이 실제 플레이어
    players = [(my_name, my_drink, 0)]

    # 함께 할 친구 수 정하기
    while True:
        try:
            invite_count = int(input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : '))
            if invite_count in range(1, 4):
                break
            else:
                print('1~3명을 선택해주세요.')
        except ValueError:
            print('정수를 입력해주세요.')
    wait()

    # 대결할 친구 이름, 주량 랜덤 생성
    friend_names = ['은서', '하연', '연서', '예진', '헌도']
    picked_names = random.sample(friend_names, invite_count)

    for i in range(invite_count):
        name = picked_names[i]
        drink = random.randint(1, 5) * 2
        players.append((name, drink, 0))
        print(f'오늘 함께 취할 친구는 {name}입니다! (치사량 : {drink})')

    line_print()
    wait()

    # 현재 상태 출력

    current_status(players)
    wait()

    # 게임 리스트 출력

    alcohol_game_list()
    wait()

    ### 5. 게임 선택 및 실행 ###

    # 게임 선택
    game_index = random_game_player(players)

    # 게임 실행
    playing_game(game_index, players)

    ### 6. 게임 결과 ###

    # 현재 상태 출력
    current_status(players)
    # 게임 리스트 출력
    alcohol_game_list()

    # 치사량 도달 시까지 반복

    everyone_alive = True
    first_round = True

    while everyone_alive:

        # player_order 로 게임플레이 순서 랜덤배치
        if first_round:
            # 맨 처음 라운드, 각자 게임 선택할때까지 - 플레이어를 제외하고 나머지 AI 순서 랜덤 배치
            player_order = players[1:]
            random.shuffle(player_order)
            first_round = False
        else:
            # 각자 한 번씩 선택하고 나서부터 - 모든 플레이어 순서 랜덤 배치
            player_order = players[:]
            random.shuffle(player_order)

        # 랜덤게임 실시 코드
        for player in player_order:
            if player == players[0]:
                ask_if_continue()
                game_index = random_game_player(player)
            else:
                ask_if_continue()
                game_index = random_game_com(player)

            playing_game(game_index, players)
            current_status(players)

            # 치사량 도달 시 엔딩
            for player in players:
                if player[1] == 0:
                    print('''
    ----------------------------------------------------------------------------------


        ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
        ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
        ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
        ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
        ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝


    ----------------------------------------------------------------------------------''')
                    wait()
                    print(f'{player[0]}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz')
                    everyone_alive = False
                    break

    line_print()
    print('                     🍺 다음에 술마시면 또 불러주세요~ 안녕! 🍺')
    line_print()


if __name__ == '__main__':
    main()