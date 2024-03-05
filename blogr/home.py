from flask import Blueprint

bp = Blueprint('home', __name__)



@bp.route('/')
def index():
    return 'Pagina de inicio'

@bp.route('/blog')
def blog():
    return 'Pagina de blog'

@bp.route('/auth')
def auth():
    return 'Pagina de autenticación'

@bp.route('/post')
def post():
    return 'Pagina de post'