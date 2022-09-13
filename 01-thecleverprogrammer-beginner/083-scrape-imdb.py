from imdb import Cinemagoer

c = Cinemagoer()

the_matrix = c.get_movie('0133093')

for d in the_matrix['directors']:
    print(d['name'])

print(sorted(the_matrix.keys()))

print(the_matrix['original air date'])

print(c.get_popular100_tv())
