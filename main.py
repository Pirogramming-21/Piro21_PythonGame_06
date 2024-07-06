import os
import sys
import random

def line_print():
    columns, _ = os.get_terminal_size() # 터미널 너비
    print("~" * columns)

# 게임 목록
def game_1(): # 베스킨라빈스
    print('GAME START')
    print('베스킨라빈스')

def game_2(): # 좋아 게임
    print('GAME START')
    print('좋아 게임')

def game_3(): # 고백점프
    print('GAME START')
    print('고백점프')

def game_4(): # 369 게임
    print('GAME START')
    print('369 게임')

def game_5(): # 두부 게임
    print('GAME START')
    print('두부 게임')


### 1. 게임 시작 ###

line_print()
print('ASCII ART 추가')
line_print()
print('안주먹을 시간이 없어요~ 마시면서 배우는 술게임~')
line_print()

while True:
    start_game = input('게임을 진행할까요? (y/n) : ').strip().lower() #공백제거, 소문자화
    if start_game == 'y':
        break
    elif start_game == 'n':
        print('게임을 종료합니다.')
        sys.exit() # 전체 코드 강제종료
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
        my_drink_choice =int(input('당신의 치사량(주량)은 얼마인가요? (1~5를 선택해주세요): '))
        if my_drink_choice in range(1,6):
            break
        else:
             print('1~5를 선택해주세요.')
    except ValueError:
        print('정수를 입력해주세요.')

my_drink = my_drink_choice * 2
line_print()



### 4. 같이 대결할 사람 초대하기 & 게임 리스트 출력하기 ###

# 함께할 친구 수 정하기
players = [(my_name, my_drink)]
while True:
    try: 
        invite_count = int(input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : '))
        if invite_count in range(1,4):
            break
        else:
            print('1~3명을 선택해주세요.')
    except ValueError:
        print('정수를 입력해주세요.')

# 대결할 친구 이름, 주량 랜덤 생성
friend_names = ['은서', '하연', '연서', '예진', '헌도']
picked_names = random.sample(friend_names, invite_count)

for i in range(invite_count):
    name = picked_names[i]
    drink = random.randint(1, 5) * 2
    players.append((name, drink))
    print(f'오늘 함께 취할 친구는 {name}입니다! (치사량 : {drink})')

line_print()
line_print()

# 현재 상태 출력
for i in range(len(players)):
    print(f'{players[i][0]}은(는) 지금까지 0🍺! 치사량까지 {players[i][1]}')
    # 나중에 0🍺을 변수 적용해서 바꿀 것!

line_print()

# 게임 리스트 출력
print('''~~~~~~~~~~~~~~~~~~~  🍺 오늘의 Alcohol GAME 🍺  ~~~~~~~~~~~~~~~~~~~~~
                     🍺 1. 베스킨~라빈스~ 31🍦 
                     🍺 2. 💕좋아 게임
                     🍺 3. GO BACK JUMP!
                     🍺 4. 3-6-9 게임
                     🍺 5. 두부 게임
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ''')



### 5. 게임 선택 및 실행 ###

while True:
    try: 
        game_index = int(input(f'{my_name}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : '))
        if game_index in range(1,6):
            break
        else:
            print('1 ~ 5번 게임 중 하나를 선택해주세요.')
    except ValueError:
        print('정수를 입력해주세요.')
line_print()
print(f'{my_name} 님이 게임을 선택하셨습니다! 😊')
print('')
line_print()
line_print()
print('ASCII ART 추가')
line_print()

games = [game_1, game_2, game_3, game_4, game_5]
game_to_play = games[game_index - 1]
game_to_play()

