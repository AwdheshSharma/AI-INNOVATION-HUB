from flask import Blueprint

def register_blueprints(app):
    from .auth.routes import auth_bp
    from .dashboard.routes import dashboard_bp
    from .image_generation.routes import image_bp
    from .audio_transcription.routes import audio_bp
    from .sentiment_analysis.routes import sentiment_bp
    from .document_summary.routes import summary_bp
    from .analytics.routes import analytics_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(audio_bp)
    app.register_blueprint(sentiment_bp)
    app.register_blueprint(summary_bp)
    app.register_blueprint(analytics_bp)
