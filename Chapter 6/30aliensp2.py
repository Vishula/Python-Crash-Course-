# changing aliens properties from 30aliens.py using if statement and for loops

# For example lets change the first three aliens to yellow, medium speed aliens worth 10 points.

# Make an empty list
aliens = []

# Make 30 green aliens
for alien in range(30):
    alienprop = {"color":"green", "points":5, "speed":"slow"}
    aliens.append(alienprop)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# show the first 5 aliens

for alien in aliens [:5]:
    print(alien)