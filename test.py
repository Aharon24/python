def main():

    s = set()
    i = int(input())
    a = []
    j = 0
    while j < i:
        words = input().split()
        for w in words:
            if w not in s:
                s.add(w)
                a.append(w)
        j += 1
    for c in a:
        print(c)


if __name__ == "__main__":
    main()
