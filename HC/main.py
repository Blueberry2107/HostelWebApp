from flask import Flask, flash, render_template, request, redirect, Blueprint
from . import db, allowed_file, UPLOAD_FOLDER
from .forms import RegistrationForm
import os
from .models import Student
from werkzeug.utils import secure_filename

# Reset Database
# with app.app_context():
#     db.drop_all()
#     db.create_all()

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # hostels = Hostel.query.all()
    return render_template("index.html", page_name='Home')

@main.route('/contactus')
def contactus():
    return 'Contact Us'
    # return render_template('contactus.html')

@main.route('/rooms')
def rooms():
    return render_template('rooms.html', page_name='Rooms')

# Helper function to save files
def save_file(file_field):
    if file_field:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            print('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            print('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            # Get form data
            name = form.name.data
            address = form.address.data
            phone = form.phone.data
            email = form.email.data
            parent_name = form.parent_name.data
            parent_phone = form.parent_phone.data
            year = form.year.data
            semester = form.semester.data
            pr_number = form.pr_number.data
            department = form.department.data
            photo = ''
            id_proof = ''

            # Save the data to the database
            registration_data = Student(name=name, address=address, phone=phone, email=email,
                                                parent_name=parent_name, parent_phone=parent_phone, year=year,
                                                semester=semester, pr_number=pr_number, department=department,
                                                photo=photo, id_proof=id_proof)
            db.session.add(registration_data)
            db.session.commit()

            return 'Registration successful! Gn'
        return 'Something Broke, Ask Adibaba'
    return render_template('register.html', form=form, page_name='Register')

