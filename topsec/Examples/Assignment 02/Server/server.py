# Imports
from flask import Flask
from flask_cors import CORS
from routes import (
    test,
    authRoutes,
    verifyRoutes,
    registeredRoutes,
    adminRoutes,
    postRoutes,
)

# Configuration
app = Flask(
    __name__,
    static_url_path="/public",
    static_folder="public/static",
    template_folder="public/templates",
)
CORS(
    app,
    origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://rchan.sitict.net",
    ],
    supports_credentials=True,
)

# Blueprints
app.register_blueprint(test.router, url_prefix="/api/test")
app.register_blueprint(verifyRoutes.router, url_prefix="/api/verify")
app.register_blueprint(authRoutes.router, url_prefix="/api/auth")
app.register_blueprint(registeredRoutes.router, url_prefix="/api/registered")
app.register_blueprint(postRoutes.router, url_prefix="/api/post")
app.register_blueprint(adminRoutes.router, url_prefix="/api/admin")


# Start server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)