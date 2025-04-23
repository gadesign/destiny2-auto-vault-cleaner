# Destiny 2 Automatic Vault Cleaner

An intelligent and fully automated tool that helps Destiny 2 players clean up their vaults by:
- 🧹 Automatically identifying duplicate or weak weapons
- 🧠 Preserving god rolls and meta-tier gear
- 🧪 Extracting patterns and dismantling redundant items

## 🎥 Demo

See it in action:

![Vault Cleaner Demo](assets/demo.gif)

## ⚙️ Features

- Supports S/A/B-tier roll filtering
- Pattern extraction check before dismantle
- Easy integration with curated god roll lists
- Click automation support for quick scanning

## 🚀 Getting Started

### Requirements

- Python 3.9+
- `pyautogui`, `requests`, and other standard libs
- A JSON file with god roll definitions

### Setup

```bash
git clone https://github.com/gadesign/destiny2-auto-vault-cleaner.git
cd destiny2-auto-vault-cleaner
pip install -r requirements.txt
```

### Run

```bash
python src/clean_vault.py
```

## 🧠 How It Works

1. Scans vault using screen click positions
2. Reads perks and compares them against god roll definitions
3. Dismantles weak/duplicate weapons and saves patterns

## 🛡️ Disclaimer

This tool interacts with your Destiny 2 game interface via automation. Use responsibly and at your own risk. This is a fan-made project not affiliated with Bungie.

## 📬 Feedback

Feel free to open issues or feature requests!

## 🧾 License

This project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
Commercial use is not permitted.

---

## ☕ Support

If you found this tool helpful, you can support me on Ko-fi:

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/smithvr)
