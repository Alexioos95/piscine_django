#!/bin/bash

LOG_FILE="my_script.log"

python3 -m venv venv
source venv/bin/activate

echo "Using pip version:" | cat >> $LOG_FILE
pip --version | cat >> $LOG_FILE

if [ -d "./local_lib" ]; then
	echo "Removing existing 'local_lib' folder..." | cat >> $LOG_FILE
	rm -rf ./local_lib
fi

if [ -d "./my_folder" ]; then
	echo "Removing existing 'my_folder' folder..." | cat >> $LOG_FILE
	rm -rf ./my_folder
fi

mkdir -p ./local_lib
cd ./local_lib

echo "Cloning path.py from GitHub..." | cat >> ../$LOG_FILE
git clone https://github.com/jaraco/path.py.git >> ../$LOG_FILE 2>&1

cd path.py

echo "Installing path.py..." | cat >> ../../$LOG_FILE
pip install . --upgrade 2>&1 | cat >> ../../$LOG_FILE

echo "Installation finished." | cat >> ../../$LOG_FILE

echo "Launching script..." | cat >> ../../$LOG_FILE
cd ../..
python3 ./my_program.py

deactivate
