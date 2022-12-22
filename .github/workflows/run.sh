# adding a shebang '
# It is used to specify the interpreter that should be used to execute the script

#!/usr/bin/env bash

#Installing required packages 

python3 -m pip install --upgrade pip #Using python3 using module pipm upgrade pip
python3 -m pip install -r ../../requirements.txt

#Run the code from main.py with the given arugments 

python main.py dommedump/ danish --padding --unknown
