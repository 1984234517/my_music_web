from flask import Flask,render_template,request,jsonify
from decoder2 import main
import json
from qq_music import get_song
app = Flask(__name__)


@app.route('/index')
def hello_world():
    return render_template('music_index.html')


@app.route('/index/search')
def search():
    key_vlaue = request.args.get('query_value')
    print("我的参数是")
    # check_vlaue = request.values.get("selectid")
    check_vlaue = request.args.get("type")
    print("选择的播放器是0")
    print(check_vlaue)
    print("wode shi ", key_vlaue)
    if check_vlaue == 'qq音乐':
        song_url = get_song(key_vlaue)
        if song_url != '':
            data = dict(data = song_url,statu = 0)
            return jsonify(data)
    else:
        song_id = main(key_vlaue)
        print(song_id)
        if song_id != '':
            data=dict(data = song_id,statu = 1)
            return jsonify(data)
        else:
            return jsonify({})
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
