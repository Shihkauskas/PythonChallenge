import geoplotlib
from geoplotlib.utils import DataAccessObject


class Coords:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return 'Координата: {},{}'.format(
            self.latitude, self.longitude)

    def __add__(self, other):
        return Coords(
            self.latitude + other.latitude,
            self.longitude + other.longitude)

    def map(self):
        geoplotlib.dot(DataAccessObject(
            {'lat': [self.latitude], 'lon': [self.longitude]}))
        geoplotlib.show()


def main():
    chelyabinsk = Coords(55.14402, 61.42915)
    melburn = Coords(-37.8140000, 144.9633200)


    print(chelyabinsk)
    print(chelyabinsk + melburn)
    Coords.map(chelyabinsk)

if __name__ == '__main__':
    main()
