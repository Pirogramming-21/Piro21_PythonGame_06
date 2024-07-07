def print_intro():
        intro = """
----------------------------------------  
  ____        __      ___  
 |___ \      / /     / _ \ 
   __| |    / /_    | (_) |
  |__  |   | '_ \    \__, |
 ___ | |   | (_) |   ___| |
 |____/     \___/    \___/ 
----------------------------------------
        """
        print(intro)
        print("369~! 369~! 369게임 시작!!!")
        print("------------------------------------------")

    def is_clap(number):
        # 숫자에 3, 6, 9가 포함되어 있는지 확인
        return '3' in str(number) or '6' in str(number) or '9' in str(number)

    def count_claps(number):
        # 숫자에 포함된 3, 6, 9의 개수를 세는 함수
        return str(number).count('3') + str(number).count('6') + str(number).count('9')

    def play_369():
        print_intro()

        turn = 0  # 게임이 진행될 때마다 1씩 증가
        number = 1

        while True:
            current_player = turn % len(players)
            claps_needed = count_claps(number)

            if current_player == 0:  # 사용자 차례
                print("------------------------------------------")
                user_input = input(f"✔ {players[current_player][0]} 차례입니다!: ")
                if is_clap(number):
                    expected_claps = '짝' * claps_needed
                    if user_input != expected_claps:
                        print(f"💥💥💥Game over...💥💥💥 \n😈 {players[current_player][0]} 가 졌습니다!😈")
                        return players[current_player]
                else:
                    if user_input != str(number):
                        print(f"💥💥💥Game over...💥💥💥 \n😈 {players[current_player][0]} 가 졌습니다!😈")
                        return players[current_player]
            else:  # 컴퓨터 차례
                # 20% 확률로 실수
                if random.random() < 0.2:
                    if is_clap(number):
                        print(f"{players[current_player][0]} 차례: {number}")  # 숫자 잘못 말함
                    else:
                        print(f"{players[current_player][0]} 차례: 짝")  # 박수 잘못 침
                    print(f"💥💥💥Game over...💥💥💥 \n😈 {players[current_player][0]} 가 졌습니다!😈")
                    return players[current_player]
                else:
                    if is_clap(number):
                        print(f"{players[current_player][0]} 차례: {'짝' * claps_needed}")
                    else:
                        print(f"{players[current_player][0]} 차례: {number}")

            number += 1
            turn += 1

    loser = play_369()
    return loser