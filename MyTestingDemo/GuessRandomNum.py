'一个骗你猜数字的小游戏'

from random import randint

num = randint(1, 100)

print('Guess the number.')

success = False

while success == False:
    answer = input()
    answer = int(answer)
    if answer < num:
        print('Too Small')
    elif answer > num:
        print('Too Big')
    else:
        print('Bingo!')
        success = True
