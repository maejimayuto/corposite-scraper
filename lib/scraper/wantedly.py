from urllib import parse
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import time

class Wantedly:
    def __init__(self):
        self.WANTEDLY_URL = 'https://www.wantedly.com'
        self.session = ''

    def __login(self, email, pw):
        LOGIN_URL = 'https://www.wantedly.com/user/sign_in'
        self.session = requests.session()
        response = self.session.get(LOGIN_URL)
        bs = BeautifulSoup(response.text, 'lxml')
        authenticity_token = bs.find(attrs={'name':'authenticity_token'}).get('value')
        login_data = {
            'authenticity_token': authenticity_token,
            'user[email]': email,
            'user[password]': pw,
            'commit': 'ログイン'
        }
        response_cookie = response.cookies
        self.session.post(LOGIN_URL, data=login_data, cookies=response_cookie)

    def __query_gen(self):
        page = 1
        while True:
            # TODO 条件を外部から指定できるようにしたい
            params = parse.urlencode({
                'type': 'mixed',
                'page': page,
                'occupation_types[]': 'jp__engineering',
                'hiring_types[]': 'contract',
                'locations[]': 'kanto',
            })
            yield self.WANTEDLY_URL + '/?' + params
            page += 1

    def __get_all_project_urls(self, last_page_num, query):
        project_urls = []
        for i in range(last_page_num):
            time.sleep(2)
            html = self.session.get(next(query)).text
            soup = BeautifulSoup(html, 'lxml')
            elements = soup.select('.project-title')
            for e in elements:
                project_urls += [self.WANTEDLY_URL + e.a.get("href")]
        return project_urls

    def __get_company_name(self, element):
        if element.find_all('div', class_='company-name'):
            return element.find_all('div', class_='company-name')[0].getText().strip()
        else:
            return ''

    def __get_corpo_url(self, element):
        if element.find_all('div', class_='company-description') and element.find_all('div', class_='company-description')[0].a:
            return element.find_all('div', class_='company-description')[0].a.get("href")
        else:
            return ''

    def __get_company_info(self, all_project_urls):
        company_info = []
        for url in all_project_urls:
            time.sleep(2)
            html = self.session.get(url).text
            soup = BeautifulSoup(html, 'lxml')
            elements = soup.find_all('div', class_='company')
            for e in elements:
                company_info += [{
                    'company_name': self.__get_company_name(e),
                    'corpo_url': self.__get_corpo_url(e),
                    'wantedly_url': url.split('?')[0]
                }]
        return company_info

    def scrape(self, email, pw):
        self.__login(email, pw)
        query = self.__query_gen()
        all_project_urls = self.__get_all_project_urls(last_page_num=300, query=query)
        return self.__get_company_info(all_project_urls)
