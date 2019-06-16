from flask import Flask,render_template,request,jsonify
from decoder2 import main
import json

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return render_template('music_index.html')


@app.route('/index/search')
def search():
    key_vlaue = request.args.get('query_value')
    print("我的参数是")
    check_vlaue = request.form.get('cars')
    print(check_vlaue)
    print("wode shi ",key_vlaue)
    song_id = main(key_vlaue)
    print(song_id)
    if song_id != '':
        data=dict(data = song_id)
        return jsonify(data)
    else:
        return jsonify({})
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
