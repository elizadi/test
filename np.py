import numpy as np
import random
import time

# time.time()
customer_ids_a = random.sample(range(1000000, 5000000), 1000000)
customer_ids_b = random.sample(range(1000000, 5000000), 1000000)
# print(time.time())

# print(customer_ids_a[:5])
# print(customer_ids_b[:10])

c = np.intersect1d(customer_ids_a, customer_ids_b)
print(len(c)/len(customer_ids_a)*100)