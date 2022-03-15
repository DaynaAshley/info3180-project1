"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for,flash,send_from_directory
from app.models import Property
from werkzeug.utils import secure_filename
from .forms import PropertyForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Dayna-Ashley Roberts")

@app.route('/properties/create',methods=["GET", "POST"])
def create():
    form = PropertyForm()

    # Validate file upload on submit
    if request.method == 'POST' and form.validate_on_submit():
        # Get file data and save to your uploads folder

        file=request.files['file']

        filename=secure_filename(file.filename)

        file.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))

        property=Property(title = request.form['title'],num_bed=int(request.form['num_bed']),num_bath=int(request.form['num_bath']),
        location=request.form['location'],price=float(request.form['price']), type=request.form['type'],
        desc=request.form['desc'],filename=filename)
       
        db.session.add(property)
        db.session.commit()
        flash('Property Added Successfully', 'success')
        return redirect(url_for('properties'))

    return render_template('propertyform.html',form=form)

def get_uploaded_images():
    filenames=[]
   
    return filenames

@app.route("/uploads/<filename>")
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

    

@app.route('/properties')
def properties(): 
    return render_template('properties.html', files=get_uploaded_images())

@app.route('/properties/<propertyid>')
def property():
    return render_template('home.html')

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
