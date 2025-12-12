import os
from werkzeug.utils import secure_filename
from flask import current_app

def save_event_image(image_file):
    """
    Save uploaded image and return the filename
    """
    if image_file:
        # Generate a secure filename
        filename = secure_filename(image_file.filename)
        
        # Add timestamp to make filename unique
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        filename = timestamp + filename
        
        # Create uploads directory if it doesn't exist
        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads', 'events')
        os.makedirs(upload_folder, exist_ok=True)
        
        # Save the file
        filepath = os.path.join(upload_folder, filename)
        image_file.save(filepath)
        
        return filename
    return None


def delete_event_image(filename):
    """
    Delete event image from the filesystem
    """
    if filename:
        try:
            filepath = os.path.join(current_app.root_path, 'static', 'uploads', 'events', filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
        except Exception as e:
            current_app.logger.error(f"Error deleting image {filename}: {str(e)}")
            return False
    return False


def delete_event_image(filename):
    """
    Delete event image from the filesystem
    """
    if filename:
        try:
            filepath = os.path.join(current_app.root_path, 'static', 'uploads', 'events', filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
        except Exception as e:
            current_app.logger.error(f"Error deleting image {filename}: {str(e)}")
            return False
    return False


# Example usage in your routes:
# 
# @app.route('/add_event', methods=['GET', 'POST'])
# def add_event():
#     form = EventForm()
#     if form.validate_on_submit():
#         # Save the image
#         image_filename = save_event_image(form.image.data)
#         
#         # Create event with image
#         event = Events(
#             name=form.name.data,
#             description=form.description.data,
#             date=form.date.data,
#             time=form.time.data,
#             location=form.location.data,
#             image=image_filename
#         )
#         db.session.add(event)
#         db.session.commit()
#         
#         flash('Event created successfully!')
#         return redirect(url_for('main.events'))
#     
#     return render_template('add_event.html', form=form)
#
#
# @app.route('/delete_event/<int:event_id>', methods=['POST'])
# def delete_event(event_id):
#     event = Events.query.get_or_404(event_id)
#     
#     # Delete the associated image from filesystem
#     if event.image:
#         delete_event_image(event.image)
#     
#     # Delete the event from database
#     db.session.delete(event)
#     db.session.commit()
#     
#     flash('Event deleted successfully!')
#     return redirect(url_for('main.events'))
#
#
# @app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
# def edit_event(event_id):
#     event = Events.query.get_or_404(event_id)
#     form = EventForm(obj=event)
#     
#     if form.validate_on_submit():
#         # If new image is uploaded, delete old one and save new one
#         if form.image.data:
#             # Delete old image
#             if event.image:
#                 delete_event_image(event.image)
#             # Save new image
#             event.image = save_event_image(form.image.data)
#         
#         # Update other fields
#         event.name = form.name.data
#         event.description = form.description.data
#         event.date = form.date.data
#         event.time = form.time.data
#         event.location = form.location.data
#         
#         db.session.commit()
#         flash('Event updated successfully!')
#         return redirect(url_for('main.events'))
#     
#     return render_template('edit_event.html', form=form, event=event)