# 請印出 2~100 有哪些值數 ?
from day5.ForLoop4 import check_prime

if __name__ == '__main__':
    for n in range(2, 101):
        if check_prime(n):
            print(n)


