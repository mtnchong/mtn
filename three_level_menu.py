# -*- coding:utf-8 -*-
# Author:James Chong

data = {
    '北京':{
        '昌平': {
            '沙河':['oldboy','test'],
            '天通苑': ['链家地产', '我爱我家'],
        },
        '朝阳': {
            '望京':['奔驰','陌陌'],
            '国贸': ['CICC', 'HP'],
            '东直门': ['Advent', '飞信'],
        },
        '海淀': {},
    },
    '山东': {
        '枣庄': {},
        '德州': {},
        '潍坊': {},
    },
    '广东': {
        '东莞':{},
        '佛山': {},
        '深圳': {},
    },
}

exit_flag = True
while exit_flag:
    for L1 in data:
        print(L1)
    choice1 = input('请选择省份，按q退出>>>:')
    if choice1 in data:
        while exit_flag:
            for L2 in data[choice1]:
                print('\t',L2)
            choice2 = input('请选择城市，按b返回上一层，按q退出。>>>:')
            if choice2 in data[choice1]:
                while exit_flag:
                    for L3 in data[choice1][choice2]:
                        print('\t\t',L3)
                    choice3 = input('请选择区域，按b返回上一层，按q退出。>>>:')
                    if choice3 in data[choice1][choice2]:
                        for L4 in data[choice1][choice2][choice3]:
                            print('\t\t\t',L4)
                        choice4 = input('这是最后一层，按b返回上一层，按q退出。')
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = False
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = False
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = False
    if choice1 == 'q':
        break