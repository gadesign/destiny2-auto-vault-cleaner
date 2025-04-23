# lightgg_scraper.py
import requests
from bs4 import BeautifulSoup
import json
import time

# List of weapon URLs to scrape from light.gg
weapon_urls = {
    "Beloved": "https://www.light.gg/db/items/691578979/beloved/",
    "IKELOS_SMG_v1.0.3": "https://www.light.gg/db/items/3866356643/ikelos-smg-v103/",
    "The Immortal (Adept)": "https://www.light.gg/db/items/3461377698/the-immortal-adept/"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

roll_tiers = {}

for name, url in weapon_urls.items():
    print(f"Scraping {name}...")
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch {name}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        
        god_rolls = []
        # Attempt to find god roll perk combinations from community section (highly dependent on site layout)
        for div in soup.find_all("div", class_="roll-name"):
            roll_text = div.get_text(strip=True)
            if "god roll" in roll_text.lower():
                perks = [s.get_text(strip=True) for s in div.find_next("div", class_="perks").find_all("div", class_="perk")]
                if len(perks) >= 2:
                    god_rolls.append(perks[:2])  # Take top 2 perks as roll

        if god_rolls:
            roll_tiers[name] = {"S": god_rolls, "A": [], "B": []}
        else:
            print(f"No god rolls found for {name}")
        time.sleep(1)  # Respectful delay

    except Exception as e:
        print(f"Error scraping {name}: {e}")

# Save to roll_tiers.json
with open("roll_tiers.json", "w") as f:
    json.dump(roll_tiers, f, indent=4)

print("✅ roll_tiers.json created!")
