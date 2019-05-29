import datetime
import os

from flask import Flask, render_template, redirect, url_for, Response
from forms import ItemForm
from models import Items
from database import db_session

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        if 'send' in request.form:
            item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
            db_session.add(item)
            db_session.commit()
            return redirect(url_for('success'))
        elif 'view' in request.form:
            return redirect(url_for('list'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    results = []
 
    qry = db_session.query(Items)
    results = qry.all()

    strResult = ("\n".join(str(row) for row in results))
    return Response(strResult, mimetype='text/plain')

@app.route('/list')
def list():
    results = []
 
    qry = db_session.query(Items)
    results = qry.all()

    strResult = ("\n".join(str(row) for row in results))
    return Response(strResult, mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
