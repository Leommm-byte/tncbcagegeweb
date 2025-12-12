import os
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import current_app

def save_event_image(image_file):
    """
    Save uploaded image and return the filename
    """
    if not image_file or image_file.filename == '':
        return None
    
    # Validate file extension
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    if '.' not in image_file.filename or \
       image_file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return None
    
    # Generate a secure filename
    filename = secure_filename(image_file.filename)
    
    # Add timestamp to make filename unique
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
    filename = timestamp + filename
    
    # Create uploads directory if it doesn't exist
    upload_folder = os.path.join(current_app.root_path, 'static', 'uploads', 'events')
    os.makedirs(upload_folder, exist_ok=True)
    
    # Save the file
    filepath = os.path.join(upload_folder, filename)
    try:
        image_file.save(filepath)
        return filename
    except Exception as e:
        current_app.logger.error(f"Error saving image: {str(e)}")
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