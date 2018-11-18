from flask import Flask, render_template
from scrap import BukalapakData

app = Flask(__name__)

@app.route('/')
def home():
	rows = BukalapakData.showAll()
	for row in rows:
		print(row)
	return render_template('list.html', rows = rows)
    
if __name__ == '__main__':
	app.run()