#print gpu usage
import subprocess
while True:
    print(subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader']))