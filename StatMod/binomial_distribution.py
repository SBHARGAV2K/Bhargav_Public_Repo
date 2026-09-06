import scipy.stats as stats
from statisics import statistics

class BinomialDistribution:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def pmf(self, k):
        return stats.binom.pmf(k, self.n, self.p)

    def cdf(self, k):
        return stats.binom.cdf(k, self.n, self.p)