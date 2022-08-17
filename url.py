import requests
from bs4 import BeautifulSoup
jobTitleDict = {}
X = 4
def job_title():
    URL = "https://www.indeed.com/career-advice/finding-a-job/it-job-titles"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    title_tag = soup.find_all('p', class_='rich-text-component css-1g5t2dl e1wnkr790')
    a = list(filter(lambda tag: len(tag.text) < 20, title_tag))
    a = list(map(lambda tag: tag.text , a[4:]))
    StudentDict = dict.fromkeys(a, None)
    connections_page = "https://www.linkedin.com/search/results/people/?currentCompany=%5B%222824374%22%2C%221586%22%2C%221441%22%2C%221035%22%2C%2210667%22%2C%222382910%22%2C%221009%22%2C%221815218%22%2C%221028%22%2C%223185%22%2C%221482%22%2C%221053%22%2C%223608%22%2C%221480%22%2C%2215088102%22%2C%221063%22%2C%2215564%22%2C%2296622%22%2C%221025%22%2C%221066442%22%2C%221070%22%2C%221115%22%2C%2211348%22%2C%221252%22%2C%2213633257%22%2C%2214404238%22%2C%221497%22%2C%22165158%22%2C%22166328%22%2C%2216783%22%2C%221753%22%2C%2219133%22%2C%222017%22%2C%2222688%22%2C%222497653%22%2C%222532259%22%2C%222812%22%2C%223072%22%2C%22309694%22%2C%223364%22%2C%223653845%22%2C%223812750%22%2C%223839570%22%2C%223894%22%2C%2248433%22%2C%225390798%22%2C%2260368%22%2C%22784652%22%2C%228221%22%2C%228869%22%5D&keywords={}&origin=FACETED_SEARCH&sid=.Gd"
    jobTitleDict = {key: connections_page.format(key.replace(' ', '%20')) for key in a}
    return jobTitleDict