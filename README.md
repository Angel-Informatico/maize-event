# 🎮 Pokémon Maize Event Giveaway Website

> A Flask web application for generating event codes to receive special Pokémon in [Pokémon Maize](https://github.com/huderlem/maize), a ROM hack of Pokémon Red Version.

![Pokémon Maize](https://img.shields.io/badge/Pokémon-Maize-red?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=flat-square&logo=flask)

## 📖 About

This is the source code for the **Pokémon Maize Event Giveaway** website. Originally hosted on [Heroku](https://www.heroku.com/), this application generates unique 13-number codes that players can enter in-game to receive special event Pokémon.

[**Pokémon Maize**](https://github.com/huderlem/maize) is a ROM hack of Pokémon Red Version that features an in-game system where players can enter codes to receive special Pokémon. The website takes a player's Trainer ID and generates a personalized code that can be redeemed at the Agate City PokéCenter.

✨ **All event Pokémon are shiny!** ✨

## 🎁 Available Event Pokémon

The website now supports **5 different event Pokémon**, each with unique characteristics:

### ⚡ Flying/Surfing Pikablue
- **Pokémon**: Shiny Pikachu (Pikablue)
- **Level**: 5
- **Moves**: Fly or Surf (random), Thundershock, Growl
- **Special**: Can learn Fly or Surf, making it a unique Pikachu variant!

### 😎 Sunglasses Squirtle
- **Pokémon**: Shiny Squirtle with sunglasses
- **Level**: 5
- **Moves**: Bubblebeam, Surf, Skull Bash
- **Special**: Alternate sprite with cool sunglasses!

### 😎 Sunglasses Wartortle
- **Pokémon**: Shiny Wartortle with sunglasses
- **Level**: 16
- **Moves**: Surf, Skull Bash, Hydro Pump
- **Special**: Alternate sprite with cool sunglasses!

### 😎 Sunglasses Blastoise
- **Pokémon**: Shiny Blastoise with sunglasses
- **Level**: 36
- **Moves**: Surf, Hydro Pump, Skull Bash
- **Special**: Alternate sprite with cool sunglasses!

### 🎀 Headband Electrode
- **Pokémon**: Shiny Electrode with headband
- **Level**: 30
- **Moves**: Thunder, Explosion, Self-Destruct
- **Special**: Alternate sprite with a stylish headband!

## 🚀 How It Works

1. **Enter your Trainer ID** (found on your trainer card in-game, between 0-65535)
2. **Select the Pokémon** you want from the dropdown menu
3. **Get your code** - a unique 13-number code will be generated
4. **Redeem in-game** - Talk to the NPC in Agate City's PokéCenter and enter the numbers in order

## 💻 Desktop Application

For ease of use, this project can also be run as a standalone desktop application for **Windows, MacOS, and Linux**. This version works offline and does not require any installation or a separate web browser.

You can download the latest version for your operating system from the **[Releases page](https://github.com/Angel-Informatico/maize-event/releases)**.

## 🛠️ Setup & Installation

### Requirements
- Python 3.x
- Flask 3.0.3
- Flask-WTF 1.2.1
- WTForms 3.1.2

### Local Development

```bash
# Clone the repository
git clone <repository-url>
cd maize-event

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

The application will be available at `http://127.0.0.1:5000`

### Building the Desktop App

You can also build the desktop application from source.

1.  **Install additional dependencies**:
    ```bash
    pip install pyinstaller pywebview
    ```

2.  **Build with PyInstaller**:
    *   **On Windows**:
        ```bash
        pyinstaller --onefile --windowed --name "MaizeEventApp" --add-data "app/static;app/static" --add-data "app/templates;app/templates" --hidden-import "webview" --hidden-import "config" --icon="icon.ico" desktop.py
        ```
    *   **On macOS**:
        ```bash
        pyinstaller --onefile --windowed --name "MaizeEventApp" --add-data "app/static:app/static" --add-data "app/templates:app/templates" --hidden-import "webview" --hidden-import "config" --icon="icon.icns" desktop.py
        ```
    *   **On Linux**:
        ```bash
        pyinstaller --onefile --windowed --name "MaizeEventApp" --add-data "app/static:app/static" --add-data "app/templates:app/templates" --hidden-import "webview" --hidden-import "config" --icon="icon.png" desktop.py
        ```
    The executable will be created in the `dist/` folder.

### Deployment

This project can be deployed to various platforms:

#### Vercel

The project can be deployed to [Vercel](https://vercel.com/):

1. **Install Vercel CLI** (optional):
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```
   
   Or connect your GitHub repository directly in the Vercel dashboard.

3. **Configuration**: The project includes `vercel.json` and `api/index.py` for Vercel compatibility.

**Note**: Vercel automatically detects Python projects and uses the `@vercel/python` runtime. The Flask app is served through the `api/index.py` entry point.

#### Other Platforms

This Flask application can also be deployed to other platforms like:
- **Heroku** (original hosting platform)
- **Railway**
- **Render**
- **PythonAnywhere**
- Any platform that supports Python/Flask applications

## 📝 Technical Details

The code generation algorithm:
- Uses XOR encryption with the Trainer ID for security
- Generates checksums to validate the code
- Creates a unique 13-number code for each Trainer ID and Pokémon combination

## 🎨 Features

- ✅ Support for 5 different event Pokémon
- ✅ Shiny Pokémon generation
- ✅ Alternate sprite support
- ✅ Randomized moves (for Pikablue)

## 👥 Credits

### Original Author
**[Marcus Huderle](https://github.com/huderlem)** (2015) - Original creator of the Pokémon Maize Event Giveaway website and the [Pokémon Maize ROM hack](https://github.com/huderlem/maize).

### Special Thanks
- **[CalentadasTCG](https://www.youtube.com/@CalentadasTCG)** - Introduced me to this amazing ROM hack and helped test the new code implementations! 🎮

### Improvements
This version includes:
- ✨ Multi-Pokémon support (originally only supported Pikachu)
- 🔧 Updated dependencies for modern Python versions
- 🎨 Enhanced UI with Pokémon selection
- 🐛 Fixed internal Pokémon IDs for correct code generation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Original code** (2015) by [Marcus Huderle](https://github.com/huderlem). This version includes modifications and extensions to support multiple Pokémon, updated dependencies, and enhanced functionality.

---

**Note**: This was originally a Heroku-hosted application. The code has been updated to work with modern Python and Flask versions while maintaining compatibility with the original Pokémon Maize ROM hack.
