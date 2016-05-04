from flask import Flask, render_template, request

app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/survey_results', methods=['POST'])
def survey_results():

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template('/survey_results.html', name=name, location=location, language=language, comment=comment)
app.run(debug=True) # run our server
