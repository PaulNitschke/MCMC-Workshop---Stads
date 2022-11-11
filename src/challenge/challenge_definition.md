# Welcome to the Challenge of the MCMC Course!

## Gaussian Mixture Model

A common model in Machine Learning is the *Gaussin Mixture Models (GMM)*. A GMM is the sum of multiple normal distributions $\mathcal{N}(\mu, \sigma)$ and its density is:

$$p(x) = \sum_{i=1}^{k}\frac{p_i}{\sqrt(2\pi\sigma_i^2)}exp(-\frac{(x-\mu_i)^2}{\sigma_i^2}$$

For example, the density of a GMM consisting of two Normal Distributions with means at -2 and 2 and unit variance looks like this:

![GMM](gmm_example.png "Title")

## Challenge Definition

We have generated samples from a GMM with two modes (saved in samples_1.csv). Your task will be to calculate the respective means and standard deviations of the distributions. For simplicity, we assume that the GMM consists of *two* Normal Distributions.

## Getting Started

We have defined a baseline [model](run_me.ipynb) to help you get started. This model should run on your computer without any changes. Your task will be to improve the existing model. You can also find some hints in the notebook but feel free to change whatever you want.

## Evaluation

At the end of the challenge, every team submits their model. We will run it on the same computer (so that each team has the same hardware performance). Whichever team has the highest Effective Sample Size per Second wins. Please be aware that we run the model on data from another GMM so don't hardcode anything!

## Submission Details

Please submit a .py file which takes as input a samples file (identical to samples_1.csv) and returns the Effective Sample Size per Second (ESS/ Second). We have already written a [base file](submission_example.py). Please don't get funny with things like *ESS = 2 * ESS*, we will check your code. Also please try to avoid the excessive use of non-standard libraries; we want to run your code and not spend ages getting it to run. Apart from the already imported libraries you do not need any libraries to achieve good results.