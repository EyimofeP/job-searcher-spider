"""
Job Search Scraper
Added Extra Features to FreeCodeCamp's Web Scraping Course with Jim Shaped Coding
"""

from bs4 import BeautifulSoup
import requests

print("What type of job are you looking for?")
search = str(input("> "))
print(f"Searching {search} jobs....")

# Input Url
url = requests.get(
    f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={search}&txtLocation=").text

# Ask If you User wants specific skills
print(
    """
Do you want have any specific skills for the job
Answer yes or no
"""
)

is_specific = str(input("> ")).lower()

if is_specific == "yes":
    print("Type Skills you are familiar with")
    familiar_skills = input("> ")
    print(f"Searching for {familiar_skills} skills of {search}...")

else:
    print(f"Searching {search} jobs....")

# Create soup object
soup = BeautifulSoup(url, "lxml")

# Fetch Job Posting Div
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    # Date Posted
    date_posted = job.find("span", class_="sim-posted").text

    # Job Skills
    skills = job.find(
        "span", class_="srp-skills").text.replace(" ", "").strip().lower()

    if is_specific == "yes":
        if familiar_skills in skills:
            # Checking if job posting is fresh
            if "few" in date_posted:
                # Job Title
                title = job.find("strong", class_="blkclor").text

                # Company Name
                company = job.find(
                    "h3", class_="joblist-comp-name").text.strip()

                # Job Location
                location = job.find(
                    "ul", class_="top-jd-dtl clearfix").span.text

                # Job Link
                link = job.header.h2.a["href"]

                print(f"Job Title: {title}")
                print(f"Job Company: {company}")
                print(f"Job Location: {location}")
                print(f"Job Skills: {skills}")
                print(f"Job Link: {link}")
                print()

    else:
        # Checking if job posting is fresh
        if "few" in date_posted:
            # Job Title
            title = job.find("strong", class_="blkclor").text

            # Company Name
            company = job.find(
                "h3", class_="joblist-comp-name").text.strip()

            # Job Location
            location = job.find(
                "ul", class_="top-jd-dtl clearfix").span.text

            # Job Link
            link = job.header.h2.a["href"]

            print(f"Job Title: {title}")
            print(f"Job Company: {company}")
            print(f"Job Location: {location}")
            print(f"Job Skills: {skills}")
            print(f"Job Link: {link}")
            print()
