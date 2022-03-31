import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


def write_to_file(data):
    with open("db.txt", mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        db.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("db.csv", mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # first argument is where to write this file
        csv_writer = csv.writer(
            db, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thank_you.html")
    else:
        return render_template("error_page.html", error_msg="Form request failed")


@app.route("/")
def get_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def get_page(page_name):
    return render_template(page_name)
