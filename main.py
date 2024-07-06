import os
import sys

def line_print():
    columns, _ = os.get_terminal_size() # 터미널 너비
    print("~" * columns)

### 1. 게임 시작 / 인트로 / 진행할까요? (y/n) ###
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
name = input('당신의 이름은?: ')

### 3. 본인 주량 선택하기 ###
print('~~~~~~~~~~~~~~~~ 🍺 소주 기준 당신의 주량은? 🍺 ~~~~~~~~~~~~~~~~~~')
print('''
                    🍺 1. 소주 반병 (2잔)
                    🍺 2. 소주 반병에서 한병 (4잔)
                    🍺 3. 소주 한병에서 한병 반 (6잔)
                    🍺 4. 소주 한병 반에서 두병 (8잔)
                    🍺 5. 소주 두병 이상 (10잔)
      
''')
line_print()

while True:
    try:
        max_drink_choice =int(input('당신의 치사량(주량)은 얼마인가요? (1~5를 선택해주세요): '))
        if max_drink_choice in range(1,6):
            break
        else:
             print('1~5를 선택해주세요.')
    except ValueError:
        print('정수를 입력해주세요.')

max_drink = max_drink_choice * 2
print(max_drink)

