def game_2(players):  
    print('GAME START')
    print('좋아 게임')

    turn = 0  
    reject_count = 0  # 캌 퉤를 받은 수


    while True:
        current_player = players[turn][0]  
        complimented_index = random.randint(0, len(players) - 1)  

        while current_player == players[complimented_index][0]:
            complimented_index = random.randint(0, len(players) - 1)

        complimented = players[complimented_index][0]  

        print(f"{current_player}: {complimented} 좋아!")

        if complimented == players[0][0]:  
            response = input(f'{complimented}, 답변을 선택하세요 ("나도 좋아" 또는 "캌 퉤"): ').strip()
            if response not in ["나도 좋아", "캌 퉤"]:
                print('잘못된 입력입니다. "나도 좋아" 또는 "캌 퉤" 중 하나를 입력해주세요.')
                continue
        else:  
            response = random.choice(["나도 좋아", "캌 퉤"])
            print(f'{complimented}: {response}')

        if response == "캌 퉤":
            reject_count += 1
            if reject_count >= 3:
                print(f"{current_player}가 술을 마십니다! 🍻")
                return current_player  
        else:
            reject_count = 0
            turn = complimented_index  

        wait()
        line_print()