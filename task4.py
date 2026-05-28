from collections import Counter


def main():
    count_1 = int(input())
    count_2 = int(input())

    r = []
    s1 = []
    s2 = []
    for i in range(count_1):
        name = input()
        s1.append(name)
    for i in range(count_2):
        name = input()
        s2.append(name)
    all = s1 + s2
    cnt = Counter(all)
    for name in cnt:
        if cnt[name] == 1:
            r.append(name)
    r.sort()
    if len(r) == 0:
        print("Таких нет")
    else:
        for x in r:
            print(x)


if __name__ == "__main__":
    main()
