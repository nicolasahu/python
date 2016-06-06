finish = False
t = time.time()
Min = 0
while not finish:
	Seg = time.time() - t + 55
	if Seg >= 60:
		Min = Seg/60
	MinSeg = "%02d:%4.2f" %(Min, Seg%60)
	sys.stdout.write('\r' + MinSeg)
