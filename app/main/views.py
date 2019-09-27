from flask import render_template, request, Blueprint
from app.models import Jobsearch
from app.request import get_jobs
from flask_login import login_user, logout_user, login_required
from app.jobs.forms import JobSearchForm

main = Blueprint('main', __name__)

# get_flights = get_flights()


@main.route("/")
@main.route("/home")
def home():
   
    form = JobSearchForm()
    
    city = request.args.get('city')
    keyword = request.args.get('keyword')
    
    jobs = get_jobs(keyword, city)
    page = request.args.get('page', 1, type=int)
    
    
    return render_template('index.html',jobs=jobs, form=form)


@main.route("/about")
def about():
    jobs = get_jobs()
    return render_template('about.html', jobs=jobs)


@main.route("/search")
@login_required
def search():
   
    form = JobSearchForm()
    
    city = request.args.get('city')
    keyword = request.args.get('keyword')
    
    jobs = get_jobs(keyword, city)
    page = request.args.get('page', 1, type=int)
    
    
    return render_template('post.html',jobs=jobs, form=form)