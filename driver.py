# remeber to import the trip class here
from trip import Trip
#remember this: a driver has many trips, but a trip belongs to one driver
# that's why you import trips here; to call all the collected trips (in trip._all)


class Driver:
    def __init__(self, _name):
        self._name = _name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def my_trips(self):
        return list(filter(lambda trip: (vars(trip))['_driver'] == self ,Trip.all()))

    def my_trip_summaries(self):
        list_trips = self.my_trips()
        return list(map(lambda trip : (vars(trip))['_start'] + ' to ' + (vars(trip))['_destination'],list_trips))
