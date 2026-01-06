from pathlib import Path
import json
from typing import List, Dict

Data_File = Path("..", "data", "products.json")

def load_products() -> List[Dict]:
    if not Data_File.exists():
        return []
    with open(Data_File, "r", encoding="utf-8") as file:
        return json.load(file)

def get_products() -> List[Dict]:
    return load_products()

