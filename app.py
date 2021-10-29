from flask import Blueprint, current_app, g, render_template, redirect, request, flash, url_for, session
from flask.cli import with_appcontext

# from werkzeug.security import check_password_hash, generate_password_hash

import sqlite3
import click

import random
import string


app = Flask(__name__)

def get_messsage_db():
    if 'message_db' not in g:
    	g.message_db = sqlite3.connect("messages_db.sqlite")
    	cmd = \
		"""
		CREATE TABLE IF NOT EXISTS 'message' (id INTEGER, handle TEXT, message TEXT)
		"""

		curseur = g_message_db.cursor()
		curseur.execute(cmd)

    return g.message_db

def insert_message(request):
	if request.method == 'POST':
        message = request.form['message']
        handle = request.form['handle']

        cmd_2 = \
        """
        INSERT INTO messages (id, handle, message) VALUES (str(number_of_rows[0]+1), handle, message)
        """
        cursor = get_message_db().cursor()
        cursor.execute(cmd_2)
        get_message_db().commit()
        get_message_db().close()
        # db = get_message_db()
        # error = None


def random_messages(n):
	cursor = get_message_db().cursor()
	cursor.execute(" "SELECT * FROM messages ORDER BY RANDOM() LIMIT" + str(n) ")
	random_messages = cursor.fetchall()
	# print(random_messages)
	get_message_db().close()
	return random_messages





@app.route("/")
def main():
	return render_template("base.html")


@app.route("/submit/", methods = ["POST", "GET"])
def submit():
	if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            insert_message(request)
            return render_template('submit.html', thanks = True)
        except:
            return render_template('submit.html', error = True)

@app.route("/view/")
def view():
	random_messages(5)
	return render_template("view.html")






















