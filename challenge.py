import time

def duration_power(nb, puissance):
    start = time.time_ns()

    nb**puissance

    return time.time_ns() - start

print(duration_power(42,84))

print(duration_power(42, 168))

def duration_power_recursif(nb, puissance):
    
    return nb * duration_power(nb, puissance - 1) if puissance >= 1 else 1
    
print(duration_power_recursif(42,168))