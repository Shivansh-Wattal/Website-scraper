"""
A simple web scraper built using BeautifulSSoup.
Scraping a sample website for job postings.
"""
from bs4 import BeautifulSoup
import requests

def job_info():
    with open("job info.txt","a")as f:
        print("input skill you do not have:")
        not_skilled=input()
        print("Please wait:\n")
        html_txt=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
        soup = BeautifulSoup(html_txt,'lxml')
        jobs=soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
        for job in jobs:
            publish_date=job.find("span",class_="sim-posted").text
            if "few" in publish_date:
                skills=job.find("span",class_="srp-skills").text
                company_name=job.find("h3",class_="joblist-comp-name").text
                details=job.header.h2.a["href"]
                if not_skilled not in skills:
                    print(company_name.strip())
                    print(skills.strip())
                    print(details)
                    print(" ")
                    f.write(f"Company name: {company_name.strip()}\n")
                    f.write(f"Skills required: {skills.strip()}\n")
                    f.write(f"Link for details: {details}\n\n")
    f.close()

job_info()