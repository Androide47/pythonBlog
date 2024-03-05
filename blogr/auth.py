from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.route('/login')
def login():
    return 'Pagina de login'

@bp.route('/register')
def register():
    return 'Pagina de register'

@bp.route('/profile')
def profile():
    return 'Pagina de profile'
