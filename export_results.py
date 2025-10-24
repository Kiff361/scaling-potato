import csv
from Model import Result
from flask import current_app

def add_results_to_csvfile():
    with current_app.app_context():
        results = Result.query.all()
        with open('results.csv', 'w', newline = '', encoding='utf-8-sig') as csvfile:
            fielednames = ['Email', 'Favorite_time','Favorite_season','Favorite_game','Favorite_country']
            writer = csv.DictWriter(csvfile, fieldnames = fielednames)

            writer.writeheader()

            for r in results:
                print(r.email,r.favorite_time,r.favorite_season,r.favorite_game,r.favorite_country)
                writer.writerow({
                    'Email': r.email,
                    'Favorite_time': r.favorite_time,
                    'Favorite_season': r.favorite_season,
                    'Favorite_game': r.favorite_game,
                    'Favorite_country': r.favorite_country

                })