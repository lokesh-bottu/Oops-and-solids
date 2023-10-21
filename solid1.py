import sys
small = sys.maxsize
path = 'weather.dat'
with open(path) as data:
    next(data)
    next(data)
    for row in data:
        lines = row.split()
        if len(lines)>=10:
            difference = abs(int(lines[2][:2]) - int(lines[1][:2]))
            if difference <small:
                small = difference
                day = lines[0]
print(day)

        