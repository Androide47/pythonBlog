from flask import Blueprint, render_template, request
from models import Post, User

bp = Blueprint('home', __name__)



@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@bp.route('/blog/<url>')
def blog(url):
    post = Post.query.filter_by(url=url).first()
    return render_template('blog.html', post=post)

# @bp.route('/base')
# def auth():
#     return render_template('base.html')

# @bp.route('/post')
# def post():
#     return 'Pagina de post'