# -*- coding:utf-8 -*-
# Author:James Chong

product_list = [
    ('iPhone',6000),
    ('mac pro',12000),
    ('watch',5000),
    ('bike',2000),
    ('coffee',50)
]

items_chosen = []

# 输入余额，并判断其数值类型
your_balance = input('Please input your salary: ')
if your_balance.isdigit():
    your_balance = int(your_balance)
else:
    your_balance = int(input('numbers only. please input salary again.'))
print('您现有余额是{balance}元'.format(balance=your_balance))
# 进去循环，依次选择商品
while your_balance > 0:
    for item in enumerate(product_list):
        print(item)
    chosen_item_number = input('请输入您要购买产品的编号:')
    while not chosen_item_number.isdigit():
        if chosen_item_number.isdigit():
            chosen_item_number = int(chosen_item_number)
        else:
            chosen_item_number = input("商品编号应为数字，请重新输入:")
    else:
        chosen_item_number = int(chosen_item_number)
    if chosen_item_number < len(product_list):
        name_of_chosen_item = product_list[chosen_item_number][0]
        price_of_chosen_item = product_list[chosen_item_number][1]

        if your_balance >= price_of_chosen_item:
            items_chosen.append(name_of_chosen_item)
            your_balance = your_balance - price_of_chosen_item
            print('-------您已选择以下商品--------')
            for item in enumerate(items_chosen):
                print(item)
            print('您的当前余额为{balance}'.format(balance=your_balance))

        else:
            print('您的余额不足，请选择其他商品。')
    else:
        print('您选择的商品不存在，请重新输入。')
    quit_loop = input('按字母q退出，或者按任意键继续购物。')
    if quit_loop == 'q':
        break
else:
    print('您的余额为0元，已为您退出本次购物。')
print('---------您的购物车清单----------')
for item in enumerate(items_chosen):
    print(item)
print('--------------------------------')
print('您的余额为{balance}元'.format(balance=your_balance))
