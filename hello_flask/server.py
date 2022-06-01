from flask import Flask, render_template, redirect, url_for  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index(home):
    return render_template("index.html", phrase="hello, times=5")  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"
    
@app.route('/success')
def success():
    return "Seccess"

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(name):
    print(name)
    return "Hi, " + name

@app.route('/dashboard/repeat/<string:num>/<string:word>')
def repeat(num, word):
    return (word * int(num))

@app.route('/admin')
def admin():
    return redirect(url_for("home"))

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# """Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):

#     localhost:5000/repeat/35/hello - have it say "hello" 35 times
#     localhost:5000/repeat/80/bye - have it say "bye" 80 times
#     localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
# """
