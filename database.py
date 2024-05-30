entries = []

def add_entry(entry_body, entry_date):
  entries.append({"entry_body": entry_body, "entry_date": entry_date})

def get_entries():
  return entries