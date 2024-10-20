#!/usr/bin/env bash
source /home/codespace/venv/bin/activate
#append it to bash 
echo 'source /home/codespace/venv/bin/activate' >> ~/.bashrc
make install-tensorflow
