adj = input('Adjective: ')
verb1 = input('verb: ')
verb2 = input('verb: ')
famous_person = input('famous person: ')

madlib = 'computer programming is so {adj}! It makes me so exicted all\
    the time because I love to {verb1}. Stay hydrated and {verb2} like you are\
    {famous_person}'.format(adj=adj, verb1=verb1, verb2=verb2, famous_person=famous_person)

print(madlib)