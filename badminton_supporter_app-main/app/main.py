from flask import Flask, render_template

app = Flask(__name__)

#사이트 실행 코드(터미널) : python main.py
#사이크 클로즈(터미널) : ctrl + c
#사이트 열기 : 실행후 나오는 주소 ctrl + click


@app.route('/') 
def home():
	return render_template('main_page.html')
# 실행시 처음 켜지는 페이지

@app.route('/main_page.html')
def main_page():
	return render_template('main_page.html')
# 로그인 하지 않은 상태에서 들어가는 메인 페이지

@app.route('/main_page_login.html')
def main_page_login():
	return render_template('main_page_login.html')
# 로그인한 상태에서 들어가는 메인 페이지

@app.route('/log_in_page.html')
def log_in_page():
	return render_template('log_in_page.html')
#로그인 페이지

@app.route('/my_page.html')
def my_page():
	return render_template('my_page.html')
#마이 페이지(프로필)

@app.route('/game_save_or_not.html')
def game_save_or_not():
	return render_template('game_save_or_not.html')
#마지막 저장 유무 확인 페이지(나중에 실행페이지 만들고 연결해야함)

@app.route('/game_page.html')
def game_page():
	return render_template('game_page.html')
#실행 페이지(구현 안함)

@app.route('/game_setting_page.html')
def game_setting_page():
	return render_template('game_setting_page.html')
#실생 세팅 페이지(나중에 실행페이지 만들고 연결해야함)

@app.route('/score_board.html')
def score_board():
	return render_template('score_board.html')
# 점수판 페이지

@app.route('/test3.py')
def test():
	return render_template('test3.py')
# 점수판 페이지

if __name__ == '__main__' :   
	app.run(host='0.0.0.0', port=8000, debug=True)