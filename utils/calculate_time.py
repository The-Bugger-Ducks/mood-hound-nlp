import time

time_start = 0
time_done = 0


def init():
    global time_start
    time_start = time.time()


def finish():
    global time_done
    time_done = time.time() - time_start


def get():
    global time_start
    global time_done
    return time.strftime("%H:%M:%S", time.gmtime(time_done))
