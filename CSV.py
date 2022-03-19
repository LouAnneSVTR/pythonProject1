
import csv


def datefilter(x):
    #print(x)
    #print(x[-4:])
    #if x[-4:] >= '1980':
     #   print(True)
    #else:
    #    print(False)
    if len(x) > 0 and x[-4:] >= '2010':
        return True
    else:
        return False


def data_in_CSV():
    with open('billboard.csv', 'r+', newline='') as fichiercsv:
        with open('billboard_output.csv', 'r+', newline='') as output:
            header = ['url', 'week_id', 'week_position', 'song', 'performer', 'song_id', 'instance', 'previous_week_position', 'peak_position', 'weeks_on_chart']
            writer = csv.DictWriter(output,  fieldnames=header)
            writer.writeheader()
            test = csv.DictReader(fichiercsv, delimiter=',')
            for row in test:
                if datefilter(row['week_id']):
                    writer.writerow(row)