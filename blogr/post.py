from flask import Blueprint

bp = Blueprint('post', __name__, url_prefix='/post')



@bp.route('/post')
def post():
    return 'Pagina de login'

@bp.route('/create')
def create():
    return 'Pagina de register'

@bp.route('/update')
def update():
    return 'Pagina de profile'
