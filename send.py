import sys
import glob
import os
from pathlib import Path
from time import sleep
import subprocess

hw = sys.argv[1]
script_path=os.path.dirname(os.path.realpath(__file__))
bin_path = script_path + "/send-sds/send-sds"

for i, f in enumerate(glob.glob("*.sds")):
	run = [f'{bin_path}',  f'{hw}', "0",  f'{i}', f'{f}']
	runs = 5
	while runs > 0:
		result = subprocess.run(run, capture_output=True)
		print(result.returncode)
		if result.returncode == 217:
			runs = runs - 1
		else:
			break
	
	sleep(0.5)

