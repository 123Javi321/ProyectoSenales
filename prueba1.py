#import playsound
from thinkdsp import *
from IPython.display import Audio
import os

cos_sig = CosSignal(freq=440, amp=1.0, offset=0)

mix = cos_sig
mix.plot()



