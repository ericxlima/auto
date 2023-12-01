from app.main import bp


@bp.route('/api/')
def index():
    return 'This is The Main Blueprint'
