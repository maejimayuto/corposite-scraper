from lib.scraper import wantedly
from lib import csv_util
import sys

if __name__ == "__main__":
    wantedly_scraper = wantedly.Wantedly()
    company_info = []
    company_info = wantedly_scraper.scrape(email=sys.argv[1], pw=sys.argv[2])
    csv_util.write_to_csv(company_info)

