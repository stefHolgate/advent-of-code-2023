

def puzzle_one(data):
    numbers = []
    for i in data:
        fn = -1
        ln = -1

        for l in range(0, len(i)):
            try:
                fn = int(i[l])
                break
            except:
                pass

        for ll in range(len(i)-1, 0, -1):
            try:
                ln = int(i[ll])
                break
            except:
                pass

        if l != ll and fn > 0 and ln > 0:
            numbers.append(int(str(fn)+str(ln)))
        else:
            x = max(fn, ln)
            numbers.append(int(str(x)+str(x)))

    return sum(numbers)
                           
        

def puzzle_two(data):
    replacing = {'one':'on1e', 'two':'tw2o', 'three':'thr3e', 'four':'fo4ur',
                 'five':'fi5ve', 'six':'si6x', 'seven':'sev7en', 'eight':'ei8ght',
                 'nine':'ni9ne'}

    numbers = []

    for i in data:
            
        for k, v in replacing.items():
            i=i.replace(k, v)

        fn = -1
        ln = -1

        for l in range(0, len(i)):
            try:
                fn = int(i[l])
                break
            except:
                pass

        for ll in range(len(i)-1, 0, -1):
            try:
                ln = int(i[ll])
                break
            except:
                pass

        if l != ll and fn > 0 and ln > 0:
            numbers.append(int(str(fn)+str(ln)))
        else:
            x = max(fn, ln)
            numbers.append(int(str(x)+str(x)))

    return sum(numbers)

def main():
    f = open('day-01-data.txt', 'r')
    d = f.read().splitlines()
    print(puzzle_one(d))
    print(puzzle_two(d))


if __name__ == '__main__':
    main()