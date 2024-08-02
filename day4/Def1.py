import random
# 自訂函式

def print_hello(name):
    print("Hello", name)


def get_lucky_number():
    number = random.randint(1, 99)  # 產生隨機數當作幸運數字
    return number


# 主程式
if __name__ == '__main__':
    print_hello("John")
    print_hello("Mary")
    print_hello("Helen")
    number1 = get_lucky_number()
    number2 = get_lucky_number()
    print(number1, number2)
    print(type(number1), type(number2))
    print(number1 + number2)

