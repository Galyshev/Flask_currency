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


# страница с формой запроса для получения параметров. Как я предполагаю, вывод результатов можно реализовать динамически
# на этой же странице, или сделать еще одну, например /Currency/rezult. Данные вводятся. Есть переход на Logout и User_page
@app.route("/Currency", methods=['GET', 'POST'])
def Currency():
    if request.method == 'GET':
        return render_template ('currency.html')
    else:
        return 'отправка параметров для обработки'


if __name__ == '__main__':
    app.run(debug=True, port=5000)