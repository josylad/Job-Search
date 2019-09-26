from flask import render_template, request, Blueprint
from app.models import Flight, Hotel
from app.request import get_flights, get_flightgroup

main = Blueprint('main', __name__)

# get_flights = get_flights()


@main.route("/")
@main.route("/home")
def home():
    flights = get_flights()
    if flights is None:
        abort(404)
    page = request.args.get('page', 1, type=int)
    # categories = Post.query.filter_by(category=post.category).all()
    # print (flights[0])
    print(flights)
    return render_template('index.html',flights=flights)

@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/subscribe")
def subscribe():
    return render_template('subscribe.html')

