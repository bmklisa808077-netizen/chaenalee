dan = int(input("출력할 단을 입력하세요: "))

def print_dan():
    print(dan,"단 출력")
    for a in range(1,10):
        print(dan,"X",a,"=",dan*a)

print_dan()