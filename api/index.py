from app import app

# Export the Flask app for Vercel
# Vercel will automatically detect and serve the Flask app
__all__ = ['app']

