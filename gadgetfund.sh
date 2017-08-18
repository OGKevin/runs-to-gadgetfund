#!/bin/sh
. /home/gadgetfund/venv/bin/activate
export PATH="$PATH:/home/gadgetfund"
/home/gadgetfund/venv/bin/python /home/gadgetfund/fetch_runs.py
deactivate
dt=$(date '+%d/%m/%Y %H:%M:%S');
echo "$dt fetched runs";
. /home/gadgetfund/venv3/bin/activate
export PATH="$PATH:/home/gadgetfund"
/home/gadgetfund/venv3/bin/python /home/gadgetfund/process_runs.py
deactivate
dt=$(date '+%d/%m/%Y %H:%M:%S');
echo "$dt processed runs";
