from app.models.event import *
from datetime import datetime

event1 = Event("12-03-2020", "Rampage", 500, "Belgium", "Drum and Bass", False)
event2 = Event("06-06-2020", "TomorrowLand", 1200, "Belgium", "EDM", True)
events = [event1, event2]

def add_new_event(new_event):
    events.append(new_event)
