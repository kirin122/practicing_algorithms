"""二元搜尋法題目"""


def binary_search(_list, item, search_position):
    """二元搜尋法"""
    i = 0 # 次數
    low = 0
    high = len(_list)-1

    while low <= high:
        mid = (low + high) // 2  # 取中間位置
        guess = _list[mid]
        i += 1
        if guess == item:
          return mid  if search_position else i
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def example():
    """範例：指定數字在數列中的第幾個位置(位置由0開始)"""
    test_list = [1, 3, 5, 7, 9]
    position = binary_search(test_list, 3,True)
    position_2 = binary_search(test_list, -1, True)
    return f'3在第{position}個位置, -1在第{position_2}個位置'


def test_1():
    """題目：長度128,最差情況要找幾次"""
    length = 128
    test_list = [i for i in range(1, length+1)]
    num = binary_search(test_list, length,False)
    return f'1-1.找到答案要{num}次'


def test_2():
    """題目：如果長度增加1倍, 最差情況要找幾次"""
    length = 128 * 2
    test_list = [i for i in range(1, length+1)]
    num = binary_search(test_list, length, False)
    return f'1-2.找到答案要{num}次'


def test_3():
    """題目：長度24萬, 最差情況要找幾次"""
    length = 240000
    test_list = [i for i in range(1, length+1)]
    num = binary_search(test_list, length, False)
    return f'1-3.找到答案要{num}次'


print(example())  # 3在第3個位置, -1在第None個位置
print(test_1())  # 1-1.找到答案要8次
print(test_2())  # 1-2.找到答案要9次
print(test_3())  # 1-3.找到答案要18次
