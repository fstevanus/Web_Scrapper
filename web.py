from flask import Flask, render_template, request, jsonify
from scrap import BukalapakData
from db import createConn

app = Flask(__name__)

@app.route('/')
def home():
	rows = BukalapakData.showAll()
	for row in rows:
		print(row)
	return render_template('list.html', rows = rows)

# for api
def dictFactory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

## api v1
@app.route('/api/v1/', methods=['GET'])
def api():
	conn = createConn()
	conn.row_factory = dictFactory
	cur = conn.cursor()
	allData = cur.execute('select * from (select distinct name, terjual,rating, harga, urldetail from bukalapak where rating > 3 order by terjual desc) limit 100').fetchall()

	return jsonify(allData)


    
if __name__ == '__main__':
	app.run()