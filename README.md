# 📊 Dark and Darker Price Tracker — README

A project designed to track item prices from *Dark and Darker* over time using Python and PostgreSQL. This project is a work-in-progress and focuses on building a database and CLI tool for managing tracked items.I am leveraging the API provided by [darkerdb](https://darkerdb.com/) to get the item list and prices in real time!

## 🛠️ What I’m Trying to Do:
- Track item prices over time from the *Dark and Darker* marketplace.
- Store item information and price history in a PostgreSQL database.
- Provide a CLI tool for searching, tracking, and untracking items.
- Eventually build a web interface using FastAPI (backend) and React (frontend).

## 🚀 What I Have Done So Far:
### ✅ **Database:**
- Set up a **PostgreSQL database** with two tables:
  - **items** (for all known items, imported from `items_list.txt`)
  - **item_prices** (for price records over time)
- Imported over 1,800 items from the game into the database.

### ✅ **CLI Tool:**
- Built a Python CLI (`item_tracker.py`) to:
  - Search for items (with fuzzy search)
  - Track or untrack items
  - View all currently tracked items

### ✅ **Project Directory:**
```
price_tracker/
├── backend/
│   └── scripts/
│       └── item_tracker.py  # CLI tool
├── data/
│   └── items_list.txt       # Item list from the game
└── README.md                # Project overview
```

## 🧩 What’s Next:
- [ ] Collect real price data from the API (via a cron job)
- [ ] Build a FastAPI backend for API access
- [ ] Develop a React frontend for browsing price trends

## 💬 Feedback Welcome!
I’m sharing this with the Discord community to get feedback. If you see any mistakes or have suggestions, please let me know!


