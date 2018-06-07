import random


def get_ticket():
    """
    获取ticket
    :return:
    """
    ticket = ''
    s = 'abcdefghijkrmnopqrstuvwxyz1234567890'
    for _ in range(28):
        a = random.choice(s)
        ticket += a
    return ticket


def get_order_id():

    order_num = ''
    s = 'abcdefghijkrmnopqrstuvwxyz1234567890'
    for _ in range(28):
        a = random.choice(s)
        order_num += a
    return order_num
