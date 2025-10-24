from flask import Flask, render_template,request, redirect, url_for
from Model import Result, db
from export_results import add_results_to_csvfile

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdb.sqlite3'
db.init_app(app)


@app.route('/', methods =['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            return render_template('index.html', error= 'Пожалуйста введите email')
        return redirect(url_for('survey', email=email))
    return render_template('index.html')

@app.route('/survey', methods =['GET', 'POST'])
def survey():
    email = request.args.get('email')

    if request.method == 'POST':
        favorite_time = request.form.get('favorite_time')
        favorite_season = request.form.get('favorite_season')
        favorite_game = request.form.get('favorite_game')
        favorite_country = request.form.getlist('favorite_country')
        favorite_country_str = ', '.join(favorite_country)


        new_results = Result(
            email= email,
            favorite_time = favorite_time,
            favorite_season = favorite_season,
            favorite_game = favorite_game,
            favorite_country = favorite_country_str
        )
        db.session.add(new_results)
        db.session.commit()
        add_results_to_csvfile()

        return  render_template('thankyou.html')

    return render_template('survey.html', email=email)

if __name__ == '__main__':
    # при запуске приложения создается таблица результатов
    with app.app_context():
        db.create_all()
        add_results_to_csvfile()

    app.run(debug=True)
