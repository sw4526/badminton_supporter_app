from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def home():
	return render_template('main_page.html')

@app.route('/main_page.html')
def main_page():
	return render_template('main_page.html')

@app.route('/log_in_page.html')
def log_in_page():
	return render_template('log_in_page.html')

@app.route('/my_page.html')
def my_page():
	return render_template('my_page.html')

@app.route('/main_page_login.html')
def main_page_login():
	return render_template('main_page_login.html')

@app.route('/game_save_or_not.html')
def game_save_or_not():
	return render_template('game_save_or_not.html')

@app.route('/game_page.html')
def game_page():
	return render_template('game_page.html')

@app.route('/game_setting_page.html')
def game_setting_page():
	return render_template('game_setting_page.html')

if __name__ == '__main__' :   
	app.run(host='0.0.0.0', port=8000, debug=True)
