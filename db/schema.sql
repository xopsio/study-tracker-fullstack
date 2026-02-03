-- Luodaan taulu opintokohteille
CREATE TABLE IF NOT EXISTS studies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  progress INTEGER DEFAULT 0
);
