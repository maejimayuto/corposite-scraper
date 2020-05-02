from lib.scraper import wantedly
from lib import csv_util
import sys

if __name__ == "__main__":
    wantedly_scraper = wantedly.Wantedly()
    company_info = []
    company_info = wantedly_scraper.scrape(email=sys.argv[1], pw=sys.argv[2])
    csv_util.write_to_csv(company_info)

    # filename = '202005011545.csv'
    # path = 'data/'
    # csv_util.drop_company_name_duplications(path, filename)
