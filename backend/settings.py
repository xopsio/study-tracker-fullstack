import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'db', 'study_tracker.sqlite3')}"
