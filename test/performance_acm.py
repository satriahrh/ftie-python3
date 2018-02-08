from memory_profiler import memory_usage
from blocks import acm


def performance_dicreete_25mb():
    machine = acm.ACM(1,1,4201)

    start = time()
    # memory time interval 1 seconds
    # for maximal periods
    memory = memory_usage((a.encryption_map, (2100, ), {}), interval=1)
    time_consumed = time() - start

    return {'memory': memory, 'time': time_consumed}
