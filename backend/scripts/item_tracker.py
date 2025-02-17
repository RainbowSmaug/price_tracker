import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get database credentials from .env
DB_URL = os.getenv("DATABASE_URL")

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()
    print("✅ Connected to the database.")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    exit(1)


def search_items(search_term):
    """Search items using fuzzy matching and display results (broader, case-insensitive)."""
    try:
        cursor.execute(
            """
            SELECT id, name, tracked, similarity(name, %s) AS score
            FROM items
            WHERE name ILIKE %s OR similarity(name, %s) > 0.2
            ORDER BY score DESC
            LIMIT 20;
        """,
            (search_term, f"%{search_term}%", search_term),
        )

        results = cursor.fetchall()
        if results:
            print("\n🔍 Search Results:")
            for item_id, name, tracked, score in results:
                status = "✅ Tracked" if tracked else "❌ Not Tracked"
                print(f"[{item_id}] {name} - {status} (Score: {score:.2f})")
        else:
            print("\n⚠️ No items found.")
    except Exception as e:
        print(f"❌ Search failed: {e}")

        print(f"❌ Search failed: {e}")


def update_tracked_status(item_ids):
    """Update the tracked status for selected items."""
    try:
        if not item_ids:
            print("⚠️ No items selected.")
            return

        cursor.execute(
            """
            UPDATE items
            SET tracked = TRUE
            WHERE id = ANY(%s);
        """,
            (item_ids,),
        )

        conn.commit()
        print(f"✅ Successfully tracked items: {item_ids}")
    except Exception as e:
        print(f"❌ Update failed: {e}")


def untrack_items(item_ids):
    """Update the tracked status for selected items to FALSE (untrack)."""
    try:
        if not item_ids:
            print("⚠️ No items selected.")
            return

        cursor.execute(
            """
            UPDATE items
            SET tracked = FALSE
            WHERE id = ANY(%s);
        """,
            (item_ids,),
        )

        conn.commit()
        print(f"✅ Successfully untracked items: {item_ids}")
    except Exception as e:
        print(f"❌ Untrack failed: {e}")


def show_tracked_items():
    """Display all currently tracked items."""
    try:
        cursor.execute("""
            SELECT id, name 
            FROM items 
            WHERE tracked = TRUE 
            ORDER BY name;
        """)
        results = cursor.fetchall()

        if results:
            print("\n✅ Currently Tracked Items:")
            for item_id, name in results:
                print(f"[{item_id}] {name}")
        else:
            print("\n⚠️ No items are currently being tracked.")
    except Exception as e:
        print(f"❌ Failed to retrieve tracked items: {e}")


def interactive_mode():
    """Interactive console to search, select, track, or untrack items."""
    while True:
        print("\nOptions:")
        print("1️⃣ Add Items to track")
        print("2️⃣ Currently tracked items")
        print("4️⃣ Exit")

        choice = input("\nSelect an option (1/2/3): ").strip()

        if choice == "1":
            search_term = input("\nEnter item search term: ").strip()
            search_items(search_term)
            item_ids = input(
                "\nEnter item IDs to track (comma-separated) or press Enter to skip: "
            ).strip()
            if item_ids:
                item_ids = [int(id.strip()) for id in item_ids.split(",")]
                update_tracked_status(item_ids)

        elif choice == "2":
            show_tracked_items()
            item_ids = input(
                "\nEnter item IDs to untrack (comma-separated) or press Enter to skip: "
            ).strip()
            if item_ids:
                item_ids = [int(id.strip()) for id in item_ids.split(",")]
                untrack_items(item_ids)

        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    interactive_mode()
