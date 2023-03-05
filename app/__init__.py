from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.config.config import Config
    app.config.from_object(Config)
    from app.modules.home.routes.home import home
    from app.modules.about.routes.about import about
    from app.modules.sleep_spell.routes.sleep_spell import sleep_spell
    from app.modules.film_scrobbler.routes.film_scrobbler import film_scrobbler
    app.register_blueprint(home)
    app.register_blueprint(about)
    app.register_blueprint(sleep_spell)
    app.register_blueprint(film_scrobbler)
    return app
