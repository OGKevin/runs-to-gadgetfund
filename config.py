folder_path = "/home/gadgetfund/"

# ENDOMONDO
endomondo_email = ""
endomondo_password = ""

'''
Run the following and paste it's output below:
  source venv/bin/activate
  python authenticate_endomondo.py
  deactivate
'''
endomondo_key = ""

'''
DATABASE
Create a database file by running in terminal 'sqlite3 runs.sqlite3
followed by this :
  CREATE TABLE Runs (
  id INT PRIMARY KEY,
  date DATE NOT NULL,
  distance REAL NOT NULL,
  processed INT NOT NULL);
'''
db_path = "/home/gadgetfund/runs.sqlite3"

# bunq
# get your bunq api key from the bunq app (profile > security > api)
bunq_key = ""

'''
Authenticate bunq and get user_id  with the commands below:
  source venv3/bin/activate
  python authenticate_bunq.py
  python show_users.py
  deactivate
'''
bunq_user_id = 1234

'''
Find the id of the iban you want to send money from by running the following
commands:
  source venv3/bin/activate
  python show_accounts.py
  deactivate
'''
bunq_monetary_account = 1234

# Details of where you send the money to.
bunq_counterparty_name = "My Gadget Fund"
bunq_counterparty_iban = "NL45BUNQ1234"

# How much money in euros do you want to transfer for each kilometer that you
# ran?
ammount_per_km = 1
