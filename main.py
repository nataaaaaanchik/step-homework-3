result = []

def divider(a, b):
    if a < b:
        raise ValueError("Первое число меньше второго.")
    if b > 100:
        raise IndexError("Знаменатель больше 100.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])
        result.append(res)
    except Exception as e:
        print(f"Ошибка с элементом ({key}, {data[key]}): {e}")

print("Результат:", result)
