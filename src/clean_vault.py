# clean_vault.py
# Main entry point for Destiny 2 Automatic Vault Cleaner

from src.test_pattern_ocr import scan_vault_items
from src.lightgg_scraper import get_god_rolls
import json
import os

DATA_PATH = "data/roll_tiers.json"

def load_roll_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def main():
    print("🔍 Loading god roll data...")
    god_rolls = load_roll_data(DATA_PATH)

    print("📸 Scanning vault...")
    results = scan_vault_items()

    print("🎯 Matching rolls...")
    for item in results:
        weapon_name = item.get('weapon')
        perks = item.get('perks', [])

        if weapon_name in god_rolls:
            for roll in god_rolls[weapon_name]:
                if all(perk in perks for perk in roll):
                    print(f"✅ KEEP {weapon_name} (god roll match: {roll})")
                    break
            else:
                print(f"🗑️ DISMANTLE {weapon_name} (no god roll found)")
        else:
            print(f"⚠️ {weapon_name} not in roll database")

if __name__ == "__main__":
    main()
