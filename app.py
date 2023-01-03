from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

app.route('/about')
def home():
    return render_template('about.html')

@app.route('/contact')
def home():
    return render_template('contact.html')


#create error handler for pages
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
     return render_template("404.html"), 404

#Invalid URL
@app.errorhandler(500)
def internal_server_error(e):
     return render_template("500.html"), 500

if __name__ == '__main__':
    app.run()