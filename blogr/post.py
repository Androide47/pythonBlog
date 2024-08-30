from flask import Blueprint, request, flash, redirect, url_for, g, render_template
from .auth import login_required
from .models import Post
from blogr import db

bp = Blueprint('post', __name__, url_prefix='/post')



@bp.route('/post')
@login_required
def posts():
    posts = Post.query.all()
    return render_template('admin/posts.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        url = request.form.get('url')
        url = url.replace(' ', '-')
        title = request.form.get('title')
        info = request.form.get('info')
        content = request.form.get('ckeditor')

        post = Post(g.user.id, url, title, info, content)
        
        error = None

        # Verificar si el blog ya existe
        post_url = Post.query.filter_by(url=url).first()
        if post_url is None:
            db.session.add(post)
            db.session.commit()
            flash(f'Blog {title} creado con exito')
            return redirect(url_for('post.posts'))
        else:
            error = 'El blog ya existe'
            flash(error)

    return render_template('admin/create.html')


@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    post = Post.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form.get('title')
        post.info = request.form.get('info')
        post.content = request.form.get('ckeditor')

        db.sesion.commit()
        flash(f'Blog {post.title} actualizado con exito')
        return redirect(url_for('post.posts'))
    return render_template('admin/update.html', post=post)
