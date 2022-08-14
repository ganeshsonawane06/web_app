from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/gcp_services
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.get('/gcp_services')
def getGCPServices():
    return jsonify({
        'gcp_services': {
            'with_server': ['Compute Engine', 'Kubernetes Engine'],
            'serveless': ['App Engine(Standard, Flexible)', 'Cloud Run', 'Cloud Function']
        }})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use POST
# on the terminal type: curl http://127.0.0.1:5000/multiply/10
# this returns 100 (square of 10)
@app.post('/multiply/<int:num>')
def multiply_post(num):
    return jsonify({
        "square": num**2
    })


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000/multiply/10
# this returns 100 (square of 10)
@app.get('/multiply/<int:num>')
def multiply_get(num):
    return jsonify({
        "square": f'Square of {num} is {num ** 2} !!'
    })


# driver function
if __name__ == '__main__':
    app.run(debug=True)
