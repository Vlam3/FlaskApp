from gevent import monkey;monkey.patch_all()
from flask import Flask, Response, render_template, stream_with_context
from gevent.pywsgi import WSGIServer
import json
import time
import random

app = Flask(__name__)


def timer_random():
    valor = random.randint(2, 8)
    return valor


##############################
@app.route("/")
def render_index():
    return render_template("index.html")


##############################
@app.route("/listen")
def listen():
    def respond_to_client():
        while True:
            color = "red"
            valor=0
            if color != "white":
                _data = json.dumps({"color": color, "counter": valor})
                yield f"id: 1\ndata: {_data}\nevent: online\n\n"
            print("Start : %s" % time.ctime())
            time.sleep(timer_random())
            print("End : %s" % time.ctime())

    return Response(respond_to_client(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run()
