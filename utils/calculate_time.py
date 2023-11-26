from timeit import default_timer as timer

time_start = 0
time_done = 0


def init():
    global time_start
    time_start = timer()


def finish():
    global time_done
    time_done = timer() - time_start


def get():
    global time_start
    global time_done
    hours, remainder = divmod(time_done, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
