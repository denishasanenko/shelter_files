def init_app(app):
    from .files import files_bp
    app.register_blueprint(files_bp)