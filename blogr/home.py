from flask import Blueprint, render_template

bp = Blueprint('home', __name__)



@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/blog')
def blog():
    return render_template('blog.html')

# @bp.route('/base')
# def auth():
#     return render_template('base.html')

# @bp.route('/post')
# def post():
#     return 'Pagina de post'