from musician.models import City
from musician.models import Genre
from musician.models import Profession

city = []
genre = []
profession = []


def record():
    with open('list_city.txt', 'r') as file:
        line = file.readlines()
        for l in line:
            city.append(l.rstrip())

    with open('list_genre.txt', 'r') as file:
        line = file.readlines()
        for l in line:
            genre.append(l.rstrip())

    with open('list_profession.txt', 'r') as file:
        line = file.readlines()
        for l in line:
            profession.append(l.rstrip())

    for c in city:
        CS = City(title=c)
        CS.save()

    for g in genre:
        GS = Genre(genre_style=g)
        GS.save()

    for p in profession:
        PS = Profession(title=p)
        PS.save()
