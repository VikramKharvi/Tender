from flask import Flask, request, render_template #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/')
def home():
    return render_template("hello.html")

@app.route('/form-example')
def form_example():
    language = request.args.get('firstname')
    print language
    return "OK"

@app.route('/json-example')
def json_example():
    return 'Todo...'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

