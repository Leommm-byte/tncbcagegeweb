from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Events
from .forms import EventForm

from sqlalchemy import or_

# Create main blueprint
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def home():
    events = Events.query.all()
    return render_template('index.html', event=events)

@mainbp.route('/admin')
def admin():
    event_form = EventForm()
    return render_template('admin.html', form=event_form)



