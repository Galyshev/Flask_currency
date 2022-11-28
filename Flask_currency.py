from flask import Flask, request, render_template

app = Flask(__name__)


# url = 'http://127.0.0.1:5000/'

# Стартовая страница, с приветствием, полезной информацией. Данные не вводятся. Есть переадресация на Login и Register
@app.route("/", methods=['GET'])
def index():
    return 'вывод стартовой страницы'


# страница с регистрацией, из нее переход на страницу Login или стартовую (отмена регистрации). Есть ввод данных
@app.route("/Register", methods=['GET', 'POST'])
def Register():
    if request.method == 'GET':
        return 'вывод формы регистрации'
    else:
        return 'отправка данных из формы регистрации'


# страница с авторизацией, из нее переход на страницу User_page или стартовую (отмена входа). Есть ввод данных
@app.route("/Login", methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        return 'вывод формы входа в систему'
    else:
        return 'отправка данных из формы'


# выход из авторизации и возврат на стартовую страницу
@app.route("/Logout", methods=['GET'])
def Logout():
    return 'выход из авторизации и возврат на стартовую страницу'


# странциа пользователя. Переход на страницу Currency или Logout
@app.route("/User_page", methods=['GET'])
def User_page():
    return 'вывод страницы авторизировавшегося пользователя, с разного рода статистикой  \ историей взаимодействия'


# страница с формой запроса для получения параметров.
@app.route("/Currency", methods=['GET', 'POST'])
def Currency():

    currency_bd_tmp = [
        {'bank': 'NBU', 'date': '2022-11-25', 'currency': 'UAH', 'buy_value': 0.025, 'sell_value': 0.022},
        {'bank': 'NBU', 'date': '2022-11-25', 'currency': 'EUR', 'buy_value': 0.9, 'sell_value': 0.9},
        {'bank': 'NBU', 'date': '2022-11-25', 'currency': 'USD', 'buy_value': 1, 'sell_value': 1},
        {'bank': 'NBU', 'date': '2022-11-25', 'currency': 'GPB', 'buy_value': 1.1, 'sell_value': 1.2},

        {'bank': 'Privatbank', 'date': '2022-11-25', 'currency': 'UAH', 'buy_value': 0.026, 'sell_value': 0.023},
        {'bank': 'Privatbank', 'date': '2022-11-25', 'currency': 'EUR', 'buy_value': 0.91, 'sell_value': 0.96},
        {'bank': 'Privatbank', 'date': '2022-11-25', 'currency': 'USD', 'buy_value': 1, 'sell_value': 1},
        {'bank': 'Privatbank', 'date': '2022-11-25', 'currency': 'GPB', 'buy_value': 1.11, 'sell_value': 1.21},

        {'bank': 'Monobank', 'date': '2022-11-25', 'currency': 'UAH', 'buy_value': 0.027, 'sell_value': 0.024},
        {'bank': 'Monobank', 'date': '2022-11-25', 'currency': 'EUR', 'buy_value': 0.92, 'sell_value': 0.97},
        {'bank': 'Monobank', 'date': '2022-11-25', 'currency': 'USD', 'buy_value': 1, 'sell_value': 1},
        {'bank': 'Monobank', 'date': '2022-11-25', 'currency': 'GPB', 'buy_value': 1.12, 'sell_value': 1.22},
    ]
    if request.method == 'GET':
        return render_template('currency.html')
    else:
        bank_from_form = request.form['bank']
        curr_base_from_form = request.form['currency_1']
        curr_conv_from_form = request.form['currency_2']
        date_from_form = request.form['date']
        buy_base_curr = buy_conv_curr = sell_conv_curr = sell_base_curr = 0
        for line in currency_bd_tmp:
            if line['bank'] == bank_from_form and line['currency'] == curr_base_from_form \
                    and line['date'] == date_from_form :
                buy_base_curr = line['buy_value']
                sell_base_curr = line['sell_value']
            if line['bank'] == bank_from_form and line['currency'] == curr_conv_from_form \
                    and line['date'] == date_from_form:
                buy_conv_curr = line['buy_value']
                sell_conv_curr = line['sell_value']
        buy_exchange = buy_conv_curr / buy_base_curr
        sell_exchange = sell_conv_curr / sell_base_curr
        rez = [buy_exchange, sell_exchange]
        return render_template('currency.html', bank_from_form=bank_from_form,
                                                curr_base_from_form=curr_base_from_form,
                                                buy_exchange=buy_exchange,
                                                sell_exchange=sell_exchange,
                                                curr_conv_from_form=curr_conv_from_form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
