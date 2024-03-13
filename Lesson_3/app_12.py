from flask import Flask, jsonify, render_template
from Lesson_3.models_05 import Post, db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../../instance/mydatabase.db"
db.init_app(app)


@app.route("/")
def index():
    return 'Hi!'


@app.route('/data/')
def get_data():
    return 'Your data!'


@app.route('/users/')
def get_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)

@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content, 'create_id': post.create_id} for post in posts]
        )
    else:
        return jsonify({'error': 'Posts not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)