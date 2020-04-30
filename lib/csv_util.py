from datetime import datetime
import csv

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
