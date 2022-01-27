#print the cpu usage
import psutil
while True:
    print(psutil.cpu_percent())
    #print gpu usage
    