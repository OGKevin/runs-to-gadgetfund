# Runs to gadgetfund

## What does it do?
![graphical overview](https://github.com/KReusen/runs-to-gadgetfund/raw/master/overview.jpg "Graphical overview")

This script will convert the kilometers you run and track with endomondo, into payments from (eg.) your savings account to (eg.) a gadget fund to incentivise yourself to run more!

## Requirements
- python 2.7
- and python 3.6
- endomondo
- a bunq premium bank account (bunq.com)
- sqlite3 installed on your machine

## Setup
First clone this repository to your computer or server
```
git clone git@github.com:KReusen/runs-to-gadgetfund.git
```

We're going to use a custom python api created by Github user `isoteemu`. To be able to make use of it, cd into the `runs-to-gadgetfund` folder and run:

```
git clone --depth 1 git@github.com:isoteemu/sports-tracker-liberator.git endomondo
```

The endomondo api sdk is written in Python 2.7, whereas the bunq api is written in Python 3.6. Time to create two seperate virtual environments. Cd into the `runs-to-gadgetfund` folder and run:

```bash
virtualenv venv
```
```bash
python3 -m venv venv3
```

Temporarily activate the python 3.6 environment to install the bunq sdk:
```bash
source venv3/bin/activate
pip install bunq_sdk --upgrade
deactivate
```

Open `config.py`, change the folder_path and follow the instructions over there to complete the setup. 

Then open `gadgetfund.sh` and change the paths to the path on your machine. 

Lastly, make `gadgetfund.sh` executable:
```bash
chmod +x gadgetfund.sh
```

# Running it
In order to run the script, simply use the following command:

```bash
sh gadgetfund.sh
```

This will automatically acitvate and deactivate a python 2.7 environment that executes `fetch_runs.py` and will afterwards activate and deactivate a python 3.6 environment that executes `process_runs.py`.

## Running it every 15 minutes
Open crontab:
```bash
sudo crontab -e
```

and paste the following line at the bottom. Change the path with the path on your machine.

```
*/15 * * * * /home/gadgetfund/gadgetfund.sh >> /home/gadgetfund/log.log $
```

If you want to test if the cron is working, you can initially replace the 15 in the line above with 1 to make it execute every minute. You can find the execution logs in log.log