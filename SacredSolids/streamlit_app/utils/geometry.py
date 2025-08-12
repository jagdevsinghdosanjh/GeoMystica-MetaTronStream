import json
from pathlib import Path

SYMBOLS_PATH = Path("assets/symbols/platonic_symbols.json")

def load_symbol_data():
    with open(SYMBOLS_PATH, "r") as f:
        return json.load(f)

def get_solid_info(solid_name):
    symbols = load_symbol_data()
    return symbols.get(solid_name, {
        "element": "Unknown",
        "symbol": "❓",
        "color": "#7f8c8d",
        "meaning": "No data available"
    })

SOLID_MAP = {
    "tetrahedron": {"faces": 4, "element": "Fire"},
    "cube": {"faces": 6, "element": "Earth"},
    "octahedron": {"faces": 8, "element": "Air"},
    "dodecahedron": {"faces": 12, "element": "Ether"},
    "icosahedron": {"faces": 20, "element": "Water"},
}

def get_solid_info(name):
    return SOLID_MAP.get(name, {})
