from OOH import tube_model
from pymc import MCMC
from pylab import hist, show
from pymc.Matplot import plot

M = MCMC(tube_model)
M.sample(iter = 10000, burn = 1000, thin = 10)
# hist(M.trace("after_mean")[:])
# hist(M.trace("before_mean")[:])
# show()

plot(M)
show()