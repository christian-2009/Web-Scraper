import requests
from bs4 import BeautifulSoup

URL="https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="ResultsContainer")

python_jobs = results.find_all('h2', string= lambda text: 'python' in text.lower())
print(python_jobs)

container_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]
print(container_elements)

# job_elements = results.find_all('div', class_='card-content')

def print_job(jobs):
    for job_element in jobs:
        
        print(job_element.find('h2', class_='title is-5').text.strip())
        print(job_element.find('h3', class_='subtitle is-6 company').text.strip())
        print(job_element.find('p', class_='location').text.strip())
        print()

def get_url(jobs):
    for job in jobs:

        links = job.find_all('a')

        for link in links:
            link_url = link.get('href')
            print(f'Apply here: {link_url}\n')

print_job(container_elements)
get_url(container_elements)


