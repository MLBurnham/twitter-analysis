# we import render_template in addition to flask so that we can use templates
# url_for allows us to use custom styles with css
from flask import Flask, render_template, url_for
app = Flask(__name__)
# This is dummy data we will show on our app.
posts = [
    {
        'author': 'Mike Burnham',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
            'author': 'Jane Doe',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
# in this return statement you can render all of the HTML for the entire Page
# this is cumbersom and inefficient though. instead we will render a template

# the post = posts sets the argument post equal to the dummy data posts defined
# above. this allows us to incorporate the data in posts into the html template
# we are setting the variable post in our template equal to the data posts in
# our python script
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)
