friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}
domestic = {'James', 'Heather'}

local_friends = friends.difference(abroad)

print(local_friends)

all_friends = friends.union(domestic)
print(all_friends)

art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

both = art.intersection(science)
print(both)