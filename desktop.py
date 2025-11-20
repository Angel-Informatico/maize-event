import webview
import threading
import sys
from app import app  # Import the Flask app instance

# --- Configuration ---
URL = "http://127.0.0.1:5000"
TITLE = "Pokémon Maize Event Giveaway"
# -------------------

def run_flask():
    """Function to run Flask in a separate thread."""
    try:
        app.run(host='127.0.0.1', port=5000, debug=False)
    except Exception as e:
        print(f"Error starting Flask: {e}")
        # In a real app, you might want to log this to a file

def main():
    """Main function to start the application."""
    # 1. Start the Flask server in a background thread.
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # 2. Create and show the pywebview window.
    try:
        window = webview.create_window(TITLE, URL, width=1280, height=720, resizable=True)
        webview.start(debug=False) # debug=False para producción
    except Exception as e:
        print(f"Error al crear la ventana de la aplicación: {e}")
    finally:
        # Ensure the program exits correctly
        sys.exit()

if __name__ == '__main__':
    main()
