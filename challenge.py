import time

def duration_power(nb, puissance):
    start = time.time()

    nb**puissance

    return time.time() - start

print(duration_power(42,84))

print(duration_power(42, 168))