#print gpu usage
import subprocess
import time
while True:
    gpuUsage = subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader'])    
    #print just the number in the gpuUsage string (remove the b'')
    gpuUsageTwo = gpuUsage.decode('utf-8')[:-2]
    #take only the ints from the string
    gpuUsageThree = ''.join(filter(str.isdigit, gpuUsageTwo))
    print(gpuUsageThree)
    time.sleep(1)