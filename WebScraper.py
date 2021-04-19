import requests as requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/jobs?q=python+developer&remotejob=032b3046-06a3-4876-8dfd-474eb5e7ed11"
raw_response = requests.get(URL)
beautiful_soup = BeautifulSoup(raw_response.content, "html.parser")
results = beautiful_soup.find(id="resultsCol")

job_elements = results.find_all("div", class_="jobsearch-SerpJobCard unifiedRow row result")

for job_element in job_elements:
    print(job_element, end="\n"*2)
    #title_element = job_elements.find('h2', class_="title")
    #company_elem = job_elements.find('div', class_="company")
    #location_elem = job_elements.find('div', class_="location accessible-contrast-color-location")
