import sys
small = sys.maxsize
team = None

path = 'football.dat'

with open(path) as data:
    next(data)
    for row in data:
        columns = row.split()
        team_name = columns[1]
        goals_for = int(columns[6])
        goals_against = int(columns[8])
        difference = abs(goals_for - goals_against)

        if difference < small:
            small = difference
            team = team_name

print(team)
