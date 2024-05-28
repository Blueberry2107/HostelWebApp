<<<<<<< HEAD
from pathlib import Path
from flask import Flask, flash, render_template, request, redirect, Blueprint, url_for
=======
from flask import Flask, flash, render_template, request, redirect, Blueprint
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742
from . import db, allowed_file, UPLOAD_FOLDER
from .forms import RegistrationForm
import os
from .models import Student
from werkzeug.utils import secure_filename
<<<<<<< HEAD

=======
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742

# Reset Database
# with app.app_context():
#     db.drop_all()
#     db.create_all()

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # hostels = Hostel.query.all()
    return render_template("index.html", page_name='Home')
    return render_template("index.html", page_name='Home')

@main.route('/contactus')
def contactus():
    return 'Contact Us'
    # return render_template('contactus.html')

@main.route('/rooms')
def rooms():
    return render_template('rooms.html', page_name='Rooms')

# Helper function to save files
<<<<<<< HEAD
def save_file(file_field, pr_number):
    if file_field:
        # check if the post request has the file part
        if file_field not in request.files:
=======
def save_file(file_field):
    if file_field:
        # check if the post request has the file part
        if 'file' not in request.files:
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742
            flash('No file part')
            print('No file part')
            return redirect(request.url)
        
<<<<<<< HEAD
        file = request.files[file_field]
=======
        file = request.files['file']
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            print('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
<<<<<<< HEAD
            Path(os.path.join(UPLOAD_FOLDER, str(pr_number))).mkdir(parents=True, exist_ok=True)

            path = os.path.join(UPLOAD_FOLDER, str(pr_number), filename)
            file.save(path)

            return path
=======
            file.save(os.path.join(UPLOAD_FOLDER, filename))
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST':
<<<<<<< HEAD
        if True:
=======
        if form.validate_on_submit():
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742
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
<<<<<<< HEAD

            path_photo = save_file(form.photo.name, pr_number=pr_number)
            path_id_proof = save_file(form.id_proof.name, pr_number=pr_number)

            # Save the data to the database
            registration_data = Student(warden_id='', hostel_id='', room_num='', name=name, address=address, phone=phone, email=email,
                                                parent_name=parent_name, parent_phone=parent_phone, year=year,
                                                semester=semester, pr_number=pr_number, department=department,
                                                photo=path_photo, id_proof=path_id_proof)
            db.session.add(registration_data)
            db.session.commit()

            return redirect(url_for('main.rooms'))
        return 'Something Broke'
=======
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
>>>>>>> 34d7ed92a3dc20b0641120eeda956b3602ff9742
    return render_template('register.html', form=form, page_name='Register')

