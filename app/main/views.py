from flask import render_template, request, Blueprint
from app.models import Jobsearch
from app.request import get_flights, get_flights, get_jobs

main = Blueprint('main', __name__)

# get_flights = get_flights()


@main.route("/")
@main.route("/home")
def home():
    # flights = get_flights()
    # if flights is None:
    #     abort(404)
        
    jobs = get_jobs()
    page = request.args.get('page', 1, type=int)
    
    return render_template('index.html',jobs=jobs)

@main.route("/about")
def about():
    jobs = get_jobs()
    return render_template('about.html', jobs=jobs)


@main.route("/subscribe")
def subscribe():
    return render_template('subscribe.html')

