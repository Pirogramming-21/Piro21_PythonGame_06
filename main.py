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
