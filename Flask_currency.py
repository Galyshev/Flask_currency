
from flask import Flask, request, render_template
import BDManager
from celery_work import print_word


flask_app = Flask(__name__)


def fix(num, sign = 0):
    '''
    функия возвращает заданное количество чисел после запятой
    :param num: число
    :param sign: кол-во знаков после запятой, по умолчанию - 0
    :return: отформатированное число
    '''
    return f"{num:.{sign}f}"


# Стартовая страница, с приветствием, полезной информацией. Данные не вводятся. Есть переадресация на Login и Register
@flask_app.route("/", methods=['GET'])
def index():
    return 'вывод стартовой страницы'


# страница с регистрацией, из нее переход на страницу Login или стартовую (отмена регистрации). Есть ввод данных
@flask_app.route("/Register", methods=['GET', 'POST'])
def Register():
    if request.method == 'GET':
        return 'вывод формы регистрации'
    else:
        return 'отправка данных из формы регистрации'


# страница с авторизацией, из нее переход на страницу User_page или стартовую (отмена входа). Есть ввод данных
@flask_app.route("/Login", methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        return 'вывод формы входа в систему'
    else:
        return 'отправка данных из формы'


# выход из авторизации и возврат на стартовую страницу
@flask_app.route("/Logout", methods=['GET'])
def Logout():
    task = print_word.delay('Hello')
    return 'page logout'


# странциа пользователя. Переход на страницу Currency или Logout
@flask_app.route("/User_page", methods=['GET'])
def User_page():
    return 'вывод страницы авторизировавшегося пользователя, с разного рода статистикой  \ историей взаимодействия'


# страница с формой запроса для получения параметров.
@flask_app.route("/Currency", methods=['GET', 'POST'])
def Currency():
    if request.method == 'GET':
        # в качестве параметра bank_from_form передается банк по умолчанию, верхний из списка, иначе идет из ветки
        # else в currency.html, а это самый нижний, что мне не нравится визуально )
        data_cur = [{'cur': 'UAH'}, {'cur': 'EUR'}, {'cur': 'USD'}, {'cur': 'GPB'}]
        return render_template('currency.html', bank_from_form='NBU', data_cur=data_cur)
    else:
        bank_from_form = request.form['bank']
        curr_base_from_form = request.form.get('currency_1')
        curr_conv_from_form = request.form['currency_2']
        date_from_form = request.form['date']

        # запрос в БД по ключам "банк", "дата", "код валюты". Возвращает список [buy_value, sell_value]
        query_list_base_curr = BDManager.query_to_db(bank_from_form, date_from_form, curr_base_from_form)
        buy_base_curr = query_list_base_curr[0]
        sell_base_curr = query_list_base_curr[1]
        # тот же запрос  для второй валлюты
        query_list_conv_curr = BDManager.query_to_db(bank_from_form, date_from_form, curr_conv_from_form)
        buy_conv_curr = query_list_conv_curr[0]
        sell_conv_curr = query_list_conv_curr[1]

        buy_exchange = buy_conv_curr / buy_base_curr
        sell_exchange = sell_conv_curr / sell_base_curr

        # функия возвращает заданное количество чисел после запятой
        buy_exchange = fix(buy_exchange, 2)
        sell_exchange = fix(sell_exchange, 2)

        lst_base_cur = [{'cur': 'UAH'}, {'cur': 'EUR'}, {'cur': 'USD'}, {'cur': 'GPB'}]
        lst_conv_cur = [{'cur': 'UAH'}, {'cur': 'EUR'}, {'cur': 'USD'}, {'cur': 'GPB'}]

        # код ниже удаляет кодировки валюты, заданные в форме запроса из общего списка, что бы не дублировались
        i = 0
        for element in lst_base_cur:
            if element['cur'] == curr_base_from_form:
                lst_base_cur.pop(i)
                break
            i = i + 1
        y = 0
        for element in lst_conv_cur:
            if element['cur'] == curr_conv_from_form:
                lst_conv_cur.pop(y)
                break
            y = y + 1
        return render_template('currency.html', bank_from_form=bank_from_form,
                               curr_base_from_form=curr_base_from_form,
                               buy_exchange=buy_exchange,
                               sell_exchange=sell_exchange,
                               curr_conv_from_form=curr_conv_from_form,
                               date_from_form=date_from_form,
                               lst_base_cur=lst_base_cur,
                               lst_conv_cur=lst_conv_cur)


if __name__ == '__main__':
    flask_app.run(debug=True, host="0.0.0.0", port=5000)
