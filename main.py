from tkinter import *
from tkintermapview import *
from Marker import *
from LocalMarkersDatabase import *
def add_marker_event(coords):
    map_widget.set_marker(coords[0], coords[1], text=textbox.get())
    localMarkerDatabase.AddMarker(Marker(coords[0], coords[1], textbox.get()))

def remove_marker_event(coords):
    localMarkerDatabase.RemoveNearesMarker(coords[0],coords[1])
    map_widget.delete_all_marker()
    for marker in localMarkerDatabase.AllMarkers:
        map_widget.set_marker(marker.latitude, marker.longitude, marker.description)
def coppy_all_markers_event():
    localMarkerDatabase.CoppyAlltoFile()

localMarkerDatabase = LocalMarkersDatabase()


window = Tk()
window.title("Xcitizen Prototype")
window.geometry("800x800+300+50")

map_widget = TkinterMapView(window,width=800,height=600,corner_radius=0)
map_widget.place(x=0,y=0)
map_widget.set_position(49.5992654, 34.5356311)

textbox = Entry(window, bg="gray")
textbox.place(x=400,y=600)

localMarkerDatabase.ReadAllFromFile()
for marker in localMarkerDatabase.AllMarkers:
    map_widget.set_marker(marker.latitude, marker.longitude, marker.description)

map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True)

map_widget.add_right_click_menu_command(label="Remove Marker",
                                        command=remove_marker_event,
                                        pass_coords=True)
map_widget.add_right_click_menu_command(label="Coppy All",
                                        command=coppy_all_markers_event,
                                        pass_coords=False)

window.mainloop()
