import os
import urllib.request
import json
from app.models import Flight, Hotel, Jobsearch
import requests
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get('TOKEN')


def get_flights():
    url = "https://api.travelpayouts.com/v2/prices/latest"

    querystring = {"origin":"CDG","destination":"JFK","depart_date":"2019-11", "return_date":"2019-12", "currency":"USD"}

    headers = {'x-access-token': TOKEN}

    response = requests.request("GET", 'https://api.travelpayouts.com/v2/prices/latest?origin=JFK&destination=CDG&depart_date=2019-11&return_date=2019-12&currency=USD&token=9d69ff17b962950c4f4640be33ac9a77')
    
    flight_list = response.json()

    # print(flight_list['data']['PAR']['0'])
    flight_lists = flight_list
    all_flights = []
    for flight in flight_lists['data']:
        value = flight.get('value')    
        return_date = flight.get('return_date')
        origin = flight.get('origin')
        distance = flight.get('distance')
        destination = flight.get('destination')
        depart_date = flight.get('depart_date')
        
        new_flight = Flight(value, return_date, origin, distance, destination,depart_date)
        # print(new_flight.distance)
        all_flights.append(new_flight)
        
    
    return all_flights


# def get_cheapflights():
#     url = "https://api.travelpayouts.com/v1/prices/cheap"
    
#     querystring = {"origin":"CDG","destination":"JFK","depart_date":"2019-11", "return_date":"2019-12", "currency":"USD"}

#     headers = {'x-access-token': TOKEN}
    
#     response = requests.request("GET", 'https://api.travelpayouts.com/v1/prices/cheap?origin=JFK&destination=CDG&depart_date=2019-11&return_date=2019-12&currency=USD&token=9d69ff17b962950c4f4640be33ac9a77')
    
#     tickets = []
    
#     data_par = data['data']['PAR']
    
#     for ticket in data_par.values(): # loop through the dictionaries values
#             tickets.append({
#             'price': ticket['price']

#         })
            
#     print(tickets)
        
#     return tickets


def get_jobs():
    
    response = requests.request("GET", 'https://jobs.github.com/positions.json?description=javascript&full_time=true&location=sf')
    
    job_list = response.json()
    job_lists = job_list
    
    # print(job_lists)

    all_jobs = []
    for job in job_lists:
            
        url = job.get('url')
        types = job.get('type')
        created_at = job.get('created_at')
        company_url = job.get('company_url')
        company = job.get('company')
        location = job.get('location')
        title = job.get('title')
        description = job.get('description')
        company_logo = job.get('company_logo')
        
        new_jobs = Jobsearch(url, types, created_at, company_url, company, location,title, description,company_logo)
        
        print(new_jobs.company)
        
        all_jobs.append(new_jobs)

    return all_jobs
   

        