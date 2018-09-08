# 每一轮，你先输入一个方向射门，然后电脑随机判断一个方向扑救。
# 方向不同则算进球得分，方向相同算扑救成功，不得分。
# 之后攻守轮换，你选择一个方向扑救，电脑随机方向射门。
# 第5轮结束之后，如果得分不同，比赛结束。
# 5轮之内，如果一方即使踢进剩下所有球，也无法达到另一方当前得分，比赛结束。
# 5论之后平分，比赛继续进行，直到某一轮分出胜负。


# my thoughts

from random import randint

player_score = 0
com_score = 0
match_round = 1
match_flag = True
direction = ['a', 's', 'd']

print('''
Penalty Kick

You need to enter your direction of the goal and gatekeeper

'A' means left
'S' means center
'D' means right

Of course,If you want to press any key,you can do that.I can't stop you.
Com will borrow your ball in a random direction.
Who gets five points who is the winner.
Good lucky for you.
''')


def player_direction():
    '''
    玩家手动输入攻击/防御方向
    '''
    # python似乎没有do/while循环
    player_operating = input()
    player_operating = player_operating.lower()
    # 算是防止玩家误输入
    while not(player_operating == 'a' or player_operating == 's' or player_operating == 'd'):
        print('pleace choose your direction angin:')
        player_operating = input()
        player_operating = player_operating.lower()
    return player_operating


while match_flag:
    print('Round %d.' % match_round)
    print('attack.')
    print('A or a => left, S or s => center, D or d => right:')
    player_attack = player_direction()
    # 电脑随机选择防御方向，这个地方随机可以使用choice()函数
    com_defense = direction[randint(0, 2)]
    if player_attack != com_defense:
        # 判断是否进球
        player_score += 1
        print('player gets one points.\tplayer_score:%d\n' % player_score)
    else:
        print('com aught your shot.\n')
    print('defense.')
    print('A or a => left, S or s => center, D or d => right:')
    com_attack = direction[randint(0, 2)]
    # 玩家选择进攻方向
    player_defense = player_direction()
    if player_defense != com_attack:
        com_score += 1
        print('com gets one points.\tcom_score:%d\n' % com_score)
    else:
        print('you aught his shot.\n')

    if match_round >= 5:
        # 第五轮之后判断分数情况，多者胜利，相同则继续比赛
        if player_score != com_score:
            match_flag = False
            if player_score > com_score:
                print('you win!\n')
            elif player_score < com_score:
                print('you lose!\n')
    else:
        # 五轮内如果一方即使踢进剩下所有球，也无法达到另一方当前得分，比赛结束
        if player_score + (5-match_round) < com_score:
            match_flag = False
            print('you lose!\n')
        elif com_score + (5-match_round) < player_score:
            match_flag = False
            print('you win!\n')
    match_round += 1
