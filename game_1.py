import random

players = [('시환', '4'), ('예진', '3'), ('민서', '10'), ('은서', '3')]
num = 0

for i in range(len(players)):
    print(i)


while True:
    try:
        call_count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
        if call_count in [1, 2, 3]:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요")
    except ValueError:
        print("정수를 입력하세요")


for i in range(num + 1, num + call_count + 1):
    print(f"{players[0][0]} : {i}")

num += call_count

def brGame():
    global num, player
    if player == 'computer':
        call_count = random.randint(1, 3)
    else:
        while True:
            try:
                call_count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
                if call_count in [1, 2, 3]:
                    break
                else:
                    print("1, 2, 3 중 하나를 입력하세요")
            except ValueError:
                print("정수를 입력하세요")

    for i in range(num + 1, num + call_count + 1):
        print(f"{player} : {i}")

    num += call_count

    if player == 'player':
        player = 'computer'
    else:
        player = 'player'
    
    if num >= 31:
        print(f"{player} win!")
        return True
    
num = 0
player = 'player'
while True:
    if brGame():
        break