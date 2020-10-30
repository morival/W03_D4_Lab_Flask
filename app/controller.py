import datetime
from app import app
from app.models.event_planner import events, add_new_event
from app.models.event import *
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/add-event', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_guests = request.form['number-of-guests']
    event_location = request.form['location']
    event_description = request.form['description']
    event_recurrence = True if 'recurrence' in request.form else False
    new_event = Event(date=event_date, name_of_event=event_name, number_of_guests=event_guests, 
                        room_location=event_location, description=event_description, recurrence=event_recurrence)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)
