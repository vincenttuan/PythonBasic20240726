# 自訂函式
# 建立 get_bmi(h, w) 函式
def get_bmi(h, w):
    h = h / 100
    bmi = w / h**2
    return bmi


def print_bmi(h, w):
    bmi = get_bmi(h, w)
    print(bmi)


if __name__ == '__main__':
    bmi1 = get_bmi(170, 60)
    bmi2 = get_bmi(160, 49)
    print("bmi1: %.1f" % bmi1)
    print("bmi2: %.3f" % bmi2)
    # ---------------------------
    print_bmi(170, 60)
    print_bmi(160, 49)

