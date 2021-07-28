import random
from locust import HttpUser, TaskSet, task
from pyquery import PyQuery

class AwesomeUser(HttpUser):    
    def login(l):
        l.client.post("/login", {
            "username":"EXAMPLE_USER", 
            "password":"PASSWORD"
        })

    def index_page(self):
        r = self.client.get("/")
        pq = PyQuery(r.content)
        
        link_elements = pq("a")
        self.toc_urls = []
        
        for l in link_elements:
          if "href" in l.attrib:
            self.toc_urls.append(l.attrib["href"])

    def on_start(self):
        self.index_page()

    @task
    def load_page(self):
        url = random.choice(self.toc_urls)
        r = self.client.get(url)
