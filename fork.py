# コメント挿入

import os
import time

pid = os.fork()
if pid:
    print('\nppid=', os.getpid())
    os.waitpid(pid, 0)
else:
    print(' pid=', os.getpid())
    time.sleep(1000)

