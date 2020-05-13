import glob

for i, f in enumerate(glob.glob("*.sds")):
	print(i, f)


