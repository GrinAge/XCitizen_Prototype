class Marker:
    latitude = None #x
    longitude = None #y
    description = None
    danger_lvl = None

    def __init__(self, latitude=49.5992654, longitude=34.5356311, description="Загроза", danger_lvl=1):
        self.latitude=latitude
        self.longitude=longitude
        self.description=description
        self.danger_lvl=danger_lvl