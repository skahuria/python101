import time
epc=time.time()
print(epc)
localtime = time.localtime(epc)
print(localtime)
print(localtime.tm_year)


print(time.ctime(epc))