import glob
import os
from pathlib import Path

Path('out').mkdir(exist_ok=True)

for i, f in enumerate(glob.glob("*.wav")):
	name = f.replace('.wav', '')
	run = 'sndfile-convert -normalize "{}" "./out/{}.sds"'.format(
		f,
		name
	)
	os.system(run)
