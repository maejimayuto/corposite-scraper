from datetime import datetime
import csv
import pandas as pd

def write_to_csv(list_):
    filename = datetime.now().strftime("%Y%m%d%H%M") + '.csv'
    with open("data/" + filename, "a") as f:
        id_ = 0
        for dict in list_:
            writer = csv.writer(f, lineterminator='\n')
            csv_list = list(dict.values())
            csv_list.insert(0, id_)
            writer.writerow(csv_list)
            id_ += 1

def drop_company_name_duplications(path, filename):
    header = ['id', 'company_name', 'corpo_url', 'wantedly_url']
    df = pd.read_csv(path + filename, names=header, index_col=0)
    no_duplicated_df = df.drop_duplicates('company_name', keep='first')
    no_duplicated_df.reset_index(drop=True).to_csv(path + 'no_dupli_' + filename)