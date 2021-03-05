import multiprocessing
import time
import random
import math


def throw_dart():
	pt = math.pow(random.random(),2) + math.pow(random.random(),2)
    #EQUAÇÃO DA CIRCUNFERENCIA QUE RETORNA O RAIO:
	if (math.pow(random.random(),2) + math.pow(random.random(),2) ) <= 1: return 1
	else: return 0

def monte_pi(rand_seed, num_tests):
	random.seed(rand_seed)
	num_hits = 0
	
	for i in range(int(num_tests)):
		num_hits += throw_dart()
		
	return [num_hits, num_tests]


def worker(procnum, return_dict, tests_per_task ):
    """worker function"""
    py = []
    pi = monte_pi(random.random(),tests_per_task);
    print(str(procnum) + " worker!")
    return_dict[procnum] = pi


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []

    start_time = time.time()
    for i in range(8):
        p = multiprocessing.Process(target=worker, args=(i, return_dict, 4000000))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict.values())

    num_hits = 0
    num_tests = 0

    for points in return_dict.values():
        num_hits += points[0]
        num_tests += points[1]


    end_time = time.time()
    pi_estimate = 4.0 * float(num_hits)/num_tests

    print(("Estimate of pi:", pi_estimate))
    print(("Estimate error:", abs(pi_estimate-math.pi)))
    print(("Total time:", str(end_time-start_time)))
