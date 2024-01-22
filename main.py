N = 1000
import numpy
def find_pi(N):
    summand = numpy.array([8/((4*n+1)*(4*n+3)) for n in range(N+1)])
    pi_N = numpy.sum(summand)
    return pi_N

print(find_pi(100))
print(find_pi(1000))
print(find_pi(10000))

def error(N):
    error = numpy.abs(numpy.pi - find_pi(N))
    return error

print(error(100))
print(error(1000))
print(error(10000))

N = 100000
while error(N)>= 10**(-7):
    N += 1
print(N)