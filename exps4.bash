#!/bin/bash

#WGEVIA SIMU + REAL TABLE 4
python3 main.py --opcode origin_10 --nT 10 --d 8 --w 4
python3 main.py --opcode origin_12 --nT 10 --d 8 --w 4
#TABLE 4 G2V SIMU+REAL
python3 main.py --opcode 13
python3 main.py --opcode 15
#TABLE 4 POWERgnn SIMU+REAL (later separet)

#TABLE 1-3 FIVENODE
python3 main.py --opcode 1
python3 main.py --opcode 2
python3 main.py --opcode 3
python3 main.py --opcode 4
python3 main.py --opcode 5
python3 main.py --opcode 6
#TABLE 5-6
python3 main.py --opcode 21 --nT 10 --d 8
python3 main.py --opcode 22 --nT 10 --d 8
python3 main.py --opcode 23 --nT 10 --d 8
python3 main.py --opcode 24 --nT 10 --d 8

python3 main.py --opcode 21 --nT 4 --d 8
python3 main.py --opcode 22 --nT 4 --d 8
python3 main.py --opcode 23 --nT 4 --d 8
python3 main.py --opcode 24 --nT 4 --d 8
