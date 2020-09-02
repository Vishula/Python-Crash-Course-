# make an empty list to store aliens
aliens = []

# make 30 red green aliens
for num_alien in range(30):
    alienprop = {'color':'green',
         'health':50}
    aliens.append(alienprop)
 #   print(alienprop)

# print first 5 aliens

for alien in aliens[1:6]:
    print(alien)
count = 0

print( "Total number of aliens is ",len(aliens))