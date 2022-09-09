from playsound import playsound
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
import time

playsound('outro.mp3')

print("Shutting down in 15")
for i in range(14):
  countdown = 14 - i
  print("Shutting down in",countdown)
  i+=1
  time.sleep(1)

nullptr = POINTER(c_int)()

windll.ntdll.RtlAdjustPrivilege(
    c_uint(19), 
    c_uint(1), 
    c_uint(0), 
    byref(c_int())
)

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B), 
    c_ulong(0), 
    nullptr, 
    nullptr, 
    c_uint(6), 
    byref(c_uint())
)