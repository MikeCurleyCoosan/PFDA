class Stations:

    stations = {
        "Athenry" :1875,
        "Cork_Airport" : 3904,
        "Shannon_Airport" : 518,
        "Dublin_Airport" : 532,
        "Mullingar": 875,
        "Gurteen" : 1475
    }

    def __init__(self, stations):
        self.stations = stations

    def get_stations(self):
        return self.stations

    def get_station_name(self, station_name):
        return self.stations[station_name]

    def get_station_id(self, station_id):
        return self.stations[station_id]
