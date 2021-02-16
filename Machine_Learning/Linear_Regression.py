import numpy
from scipy import stats

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

x = numpy.median(speed)

print(x)

x = numpy.median(speed)

print(x)

x = stats.mode(speed)

print(x)

print((x)[0])
#index mode with numpy.mode(x)[0]


# What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
      return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print(r)

