# Prior Knowledge


Where does the distribution that we use for sampling actually come from?

We assume that our data represents i.i.d. samples from a Gaussian mixture model, so we have

$$\mathbb{P}(x) \sim \sum_{i=1}^{k}\frac{1}{k}\mathcal{N}(\mu_i, \sigma_i)$$

or alternatively

$$\mathbb{P}(x | \mu_i, \sigma_i) = \sum_{i=1}^{k}\frac{1}{k\sqrt(2\pi\sigma_i^2)}exp(-\frac{(x-\mu_i)^2}{\sigma_i^2})$$

The formulation $\mathbb{P}(x | \mu_i, \sigma_i)$ means the density of x given $\mu$ and $\sigma$, so $\mu$ and $\sigma$ are some known values, for example 5 and 10. This formulation is not useful for us as we want to infer $\mu$ and $\sigma$ (we don't know their actual values but we know what our data x is). To solve this, we can use Bayes Rule to rewrite

$$\mathbb{P}(x | \mu_i, \sigma_i) = \frac{\mathbb{P}(\mu_i, \sigma_i | x) \mathbb{P}(\mu_i, \sigma_i)}{\mathbb{P}(x)} \propto \mathbb{P}(\mu_i, \sigma_i | x) \mathbb{P}(\mu_i, \sigma_i)$$

The $\propto$ means *proportional to*. In our formulation we see the data x as fixed, so $\mathbb{P}(x)$ is just some number. As in all our algorithms we only care about relative probability (we only compare whether our proposal is more likely than the current state) the constant factors get canceled out.

<br/><br/>

So now we have the following formulation: $\mathbb{P}(\mu_i, \sigma_i | x) \mathbb{P}(\mu_i, \sigma_i)$. We now assume a distribution on the unknown parameters $\mu$ and $\sigma$. We assume that $\mu \sim \mathcal{N}(0, 10)$, $\sigma \sim \Gamma(1, 1)$ annd $\mu$ and $\sigma$ independent (Sanity check: why did we pick these two distributions?). 

<br/><br/>

If we plug in the Normal and Gamma distributions in the aformentioned density and take the logarithm we actually get the distribution that you used to sample. You could now use different distributions, for example a Normal Distribution with a lower/ higher variance for the mean. This would change the sampling method. To implement this you would have to calculate the new resulting density and replace the old density with it. You probably want to do that on a piece of paper. Please note that this is quite complicated (at least for me) so don't hesitate to ask Paul if you have any questions. 