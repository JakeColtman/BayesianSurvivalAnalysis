from OOH import tube_model
from pymc import MCMC
from pylab import hist, show, bar, plot
import numpy as np
#from pymc.Matplot import plot

M = MCMC(tube_model)
M.sample(iter = 100000, burn = 1000, thin = 10)
# hist(M.trace("after_mean")[:])
# hist(M.trace("before_mean")[:])
# show()

#plot(M)
#show()

before_mean_samples = M.trace("before_mean")[:]
after_mean_samples = M.trace("after_mean")[:]
start_time_samples = M.trace("start_t")[:]

N = start_time_samples.shape[0]

expected_conversions_per_day = np.zeros(16)

for day in range(0, 16):
    ix = day < start_time_samples
    expected_conversions_per_day[day] = ((before_mean_samples[ix].sum()) + (after_mean_samples[~ix].sum())) / N
print(expected_conversions_per_day)
plot(list(range(16)), expected_conversions_per_day)
show()