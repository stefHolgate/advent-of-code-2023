import re

def part_one(data):
    sumints = []
    for l in data:
        ints = re.sub('\D', '', l)
        sumints.append(int(ints[0]+ints[-1]))

    return(sum(sumints))


def part_two(data):
    sumints = []
    replacing = {'one':'on1e', 'two':'tw2o', 'three':'thr3e', 'four':'fo4ur',
                 'five':'fi5ve', 'six':'si6x', 'seven':'sev7en', 'eight':'ei8ght',
                 'nine':'ni9ne'}
    
    for i in data:
        for k, v in replacing.items():
            i=i.replace(k, v)
        ints = re.sub('\D', '', i)
        sumints.append(int(ints[0]+ints[-1]))

    return(sum(sumints))


if __name__ == '__main__':
    f = open('day-01-data.txt', 'r')
    d = f.read().splitlines()
    print(part_one(d))
    print(part_two(d))

# 56465
# 55902