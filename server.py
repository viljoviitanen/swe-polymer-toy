from flask import Flask, request, send_from_directory, make_response, jsonify, redirect
app = Flask(__name__)

@app.route("/api/createsession/<path:token>")
def createsession(token):
    if (token == "1"):
      resp=redirect('/index.html')
      resp.set_cookie('auth', '1')
      return resp
    else:
      return "Sorry."

@app.route("/api/getstuff")
def querystuff():
    if request.cookies.get('auth')=='1':
      return jsonify(name='CMDR Joe Doe')
    else:
      return jsonify(name='Not authenticated.')


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')
   
#all the rest, serve plain files from project directory
@app.route('/<path:file>')
def send(file):
    return send_from_directory('.', file)

if __name__ == "__main__":
    app.run()
