import random
import math

random.seed(0)   
lst_normal = [random.gauss(10, 0.5) for _ in range(50)]

lst_uniform = [random.uniform(-20, 20) for _ in range(50)]

def verify_Chebyshev_ineq(lst, k):
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    sd = math.sqrt(variance)
    
    count_within_range = sum(1 for x in lst if mean - k * sd < x < mean + k * sd)
    probability = count_within_range / len(lst)
    
    return probability

# Testcases
k = 1
cnt = verify_Chebyshev_ineq(lst_normal, k)
print(f"Probability of |X-u| = {cnt:.2f} ; 1-1/(k^2) = {1 - 1 / k ** 2}")
print(f"When k = {k} , P(|X-u| < k*sd) >= 1-1/k^2 is {cnt >= 1 - 1 / k ** 2}")

k = 2 ** 0.5
cnt = verify_Chebyshev_ineq(lst_normal, k)
print(f"Probability of |X-u| = {cnt:.2f} ; 1-1/(k^2) = {1 - 1 / k ** 2}")
print(f"When k = {k} , P(|X-u| < k*sd) >= 1-1/k^2 is {cnt >= 1 - 1 / k ** 2}")

k = 1.5
cnt = verify_Chebyshev_ineq(lst_normal, k)
print(f"Probability of |X-u| = {cnt:.2f} ; 1-1/(k^2) = {1 - 1 / k ** 2}")
print(f"When k = {k} , P(|X-u| < k*sd) >= 1-1/k^2 is {cnt >= 1 - 1 / k ** 2}")

k = 2
cnt = verify_Chebyshev_ineq(lst_normal, k)
print(f"Probability of |X-u| = {cnt:.2f} ; 1-1/(k^2) = {1 - 1 / k ** 2}")
print(f"When k = {k} , P(|X-u| < k*sd) >= 1-1/k^2 is {cnt >= 1 - 1 / k ** 2}")

k = 3
cnt = verify_Chebyshev_ineq(lst_normal, k)
print(f"Probability of |X-u| = {cnt:.2f} ; 1-1/(k^2) = {1 - 1 / k ** 2}")
print(f"When k = {k} , P(|X-u| < k*sd) >= 1-1/k^2 is {cnt >= 1 - 1 / k ** 2}")
