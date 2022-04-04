#switch audio output to speaker
import sounddevice as sd
print(sd.query_devices())
audiosOutputs = sd.query_devices()

# switch to the 8th device
sd.default.device = 8
