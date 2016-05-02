from pymc import DiscreteUniform, Exponential, deterministic, Poisson, Uniform
import numpy as np

'''

Model:

    Claim: advertising on the tube increased the rate of conversions.

    (Conversions_t | start_t, before_rate, after_rate)  ~ Poisson(rate_t)

    start_t ~ DiscreteUniform(first_period, last_period)  //can be any period with equal probability

    rate_t = ( before_rate ... //start_t // .. after_rate)

'''

conversions_data = np.array([1, 2, 1, 2, 3, 4, 1, 2, 3, 5, 7, 3, 8, 7, 4, 5, 7])
start_t = DiscreteUniform("start_t", lower=0, upper=len(conversions_data))

before_mean = Exponential('before_mean', beta=1.)
after_mean = Exponential('after_mean', beta=1.)


@deterministic(plot=False)
def rate(start_period=start_t, before_period_mean=before_mean, after_period_mean=after_mean):
    output = np.empty(len(conversions_data))
    output[:start_period] = before_period_mean
    output[start_period:] = after_period_mean
    return output


conversions = Poisson("conversions", mu=rate, value=conversions_data, observed=True)
