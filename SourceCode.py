import numpy as np
import time
from math import sqrt
import unittest

# Fungsi untuk integrasi trapezoid
def trapezoidal_rule(f, a, b, N):
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Loop untuk setiap nilai N dan menghitung integral, galat RMS, dan waktu eksekusi
results = []
for N in N_values:
    start_time = time.time()
    integral_value = trapezoidal_rule(f, 0, 1, N)
    end_time = time.time()
    execution_time = end_time - start_time
    rms_error = sqrt((integral_value - pi_ref)**2)
    
    result = {
        'N': N,
        'approx_pi': integral_value,
        'rms_error': rms_error,
        'execution_time': execution_time
    }
    results.append(result)
    
    print(f'N = {N}')
    print(f'Approximate value of pi: {integral_value}')
    print(f'RMS Error: {rms_error}')
    print(f'Execution time: {execution_time} seconds')
    print('-'*40)

# Testing class using unittest
class TestTrapezoidalRule(unittest.TestCase):
    
    def test_trapezoidal_rule(self):
        for result in results:
            N = result['N']
            approx_pi = result['approx_pi']
            rms_error = result['rms_error']
            
            # Adjust tolerance based on N
            if N == 10:
                self.assertAlmostEqual(approx_pi, pi_ref, delta=0.01,
                                       msg=f'Failed for N = {N}')
            elif N == 100:
                self.assertAlmostEqual(approx_pi, pi_ref, delta=0.001,
                                       msg=f'Failed for N = {N}')
            else:
                self.assertAlmostEqual(approx_pi, pi_ref, places=5,
                                       msg=f'Failed for N = {N}')
            
            # Check if RMS error is within an acceptable range
            self.assertLess(rms_error, 0.01, msg=f'RMS error too high for N = {N}')
            
            # Check if execution time is reasonable (arbitrary limit set here for the sake of testing)
            self.assertLess(result['execution_time'], 1, msg=f'Execution time too long for N = {N}')

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
