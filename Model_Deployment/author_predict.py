from flask import Flask,request,render_template
from joblib import load

model = load('author_model.joblib')

app = Flask(__name__,template_folder='.')

@app.route('/')
def home():
    return render_template("Author_Model_HtmlPage.html")

@app.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form["auth"]
    res = model.predict([text])
    return res[0]
    
    
app.run(debug=True)