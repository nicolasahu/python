import time
import os
for i in range(23):
	for j in range(59):
		for k in range(59):
			time.sleep(1)
			if k<10:
				print "0%d:0%d:0%d" %(i, j, k)
			else:
				print "0%d:0%d:%d" %(i, j, k)
