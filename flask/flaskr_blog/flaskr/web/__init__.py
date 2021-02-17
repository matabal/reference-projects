from .views.auth import bp_auth
from .views.blog import bp_blog


def register_web_blueprints(app):
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_blog)

