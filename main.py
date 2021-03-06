from lib.scraper import wantedly
from lib import csv_util
import sys
from lib import slack_nortify

if __name__ == "__main__":
    try:
        slack_nortify.post('start to scrape the Wantedly')
        wantedly_scraper = wantedly.Wantedly()
        company_info = []
        company_info = wantedly_scraper.scrape(email=sys.argv[1], pw=sys.argv[2])
        slack_nortify.post('finish to scrape the Wantedly')
        csv_util.write_to_csv(company_info)
        slack_nortify.post('complete write to the csv <@maejimayuto>')
    except Exception as e:
        slack_nortify.post('got erros in scraping the Wantedly <@maejimayuto>')
        slack_nortify.post('error' + str(e))
        print(e)

    # filename = '202005011545.csv'
    # path = 'data/'
    # csv_util.drop_company_name_duplications(path, filename)
