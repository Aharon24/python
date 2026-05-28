def main():
    data = dict()
    i = int(input())
    for j in range(i):
        s = input()
        k_v = s.split()
        data[k_v[0]] = k_v[1:]
    na = input()
    r = []
    for key, value in data.items():
        if (na in value):
            r.append(key)
    if len(r) == 0:
        print("Таких нет")
    else:
        r.sort()
    for name in r:
        print(name)


if __name__ == "__main__":
    main()
