from math import sqrt
from Marker import *

class LocalMarkersDatabase:
    AllMarkers=[]
    FileString = 'text.txt'

    def AddMarker(self, newMarker):
        self.AllMarkers.append(newMarker)
        file = open(self.FileString, 'a')
        file.write(str(newMarker.latitude)+'\n')
        file.write(str(newMarker.longitude)+'\n')
        file.write(newMarker.description+'\n')
        file.write(str(newMarker.danger_lvl)+'\n')
        file.close()
    def RemoveMarker(self, oldMarker):
        self.ReadAllFromFile()
        for marker in self.AllMarkers:
            if marker.longitude == oldMarker.longitude \
                    and marker.latitude == oldMarker.latitude \
                    and marker.description == oldMarker.description \
                    and marker.danger_lvl == oldMarker.danger_lvl:
                        self.AllMarkers.remove(marker)
                        break
        self.CoppyAlltoFile()


    def RemoveNearesMarker(self, latitude, longitude):
        markerToRemove = self.AllMarkers[0]
        minDistance = sqrt((self.AllMarkers[0].latitude - latitude)**2 + (self.AllMarkers[0].longitude - longitude)**2)
        for marker in self.AllMarkers:
            distance = sqrt((marker.latitude - latitude)**2 + (marker.longitude - longitude)**2)
            if distance<minDistance:
                minDistance = distance
                markerToRemove = marker
        self.RemoveMarker(markerToRemove)


    def CoppyAlltoFile (self):
            file = open(self.FileString, 'w')
            for marker in self.AllMarkers:
                dataString = str(marker.latitude) + '\n'
                dataString += str(marker.longitude) + '\n'
                dataString += str(marker.description) + '\n'
                dataString += str(marker.danger_lvl) + '\n'
                file.write(dataString)
            file.close()
    def ReadAllFromFile(self):
        file =open(self.FileString,'r')
        self.AllMarkers=[]
        rawDataMas =[]
        for line in file:
            rawDataMas.append(line)
            rawDataMas[-1] = rawDataMas[-1][0:-1]
        print(rawDataMas)
        for i in range(0, len(rawDataMas), 4):
            latitude = float(rawDataMas[i])
            longitude = float(rawDataMas[i+1])
            description = rawDataMas[i+2]
            danger_lvl = int(rawDataMas[i+3])
            self.AllMarkers.append(Marker(latitude,longitude,description,danger_lvl))
            print("iteration ",i,' ',len(rawDataMas))
        file.close()