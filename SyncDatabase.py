import os
import time
import schedule
import logging
from logger import setup_logger
setup_logger()
def update_database():
    # Simulate database update
    logging.info("Updating database...")
    try:
        os.system("python3 Parser.py")
        logging.info("✅ Database updated successfully.")
    except Exception as e:
        logging.error(f"❌ Error during database update: {e}")
        return

logging.info("⌛ Scheduler is running... Waiting for the next update...")

# Schedule the update every daily
while True:
    schedule.run_pending()
    schedule.every(1).day.do(update_database)