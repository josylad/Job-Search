import os
import urllib.request
import json
from app.models import Jobsearch
import requests
from dotenv import load_dotenv


load_dotenv()


def get_jobs(keyword, city):
    
    response = requests.request("GET", f'https://jobs.github.com/positions.json?description={keyword}&location={city}')
    
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
        
        # print(new_jobs.company)
        
        all_jobs.append(new_jobs)

    return all_jobs
   

        