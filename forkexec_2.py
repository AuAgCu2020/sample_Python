import os
import time

pid = os.fork()
if pid:
  print('ppid=', os.getpid())
  os.waitpid(pid, 0)
else:
  print(' pid=', os.getpid())
  os.execl("/bin/ls", "/bin/ls")
