import flask

def create_app():

    app = flask.Flask(__name__)
    app.config.from_object('warp.config')

    from . import db
    db.init(app)

    from . import view
    app.register_blueprint(view.bp)

    from . import xhr
    app.register_blueprint(xhr.bp)

    from . import auth
    from . import auth_mellon
    if 'AUTH_MELLON' in app.config \
       and 'MELLON_ENDPOINT' in app.config \
       and app.config['AUTH_MELLON']:
        app.register_blueprint(auth_mellon.bp)
    else:
        app.register_blueprint(auth.bp)

    return app
