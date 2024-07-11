## State Contingent Expected Returns

The mean based Expected Return is limited by the fact that is based entirely on historic data/information. The historic performance of a stock is not a solid indicator that it will continue with that performance in the future. 

State Contingent Expected Returns are used to overcome this limitation. The expected returns are estimated based on the condition of future events/states occurring.
This method is only as good as the accuracy of:
* anticipated returns, and
* probabilities of future events occurrences.

Example
Analysts at Open Delta Consulting have a 1 year forecast for the returns of Ethereum (ETH) as follows:
- best case scenario: 18% return with a likelihood of 25%
- mid case scenario: 6.5% return with a likelihood of 55%
- worst case scenario: -9% return with a likelihood of 20%

What is the expected return?

Notice that the probability sum of all the scenarios - sums up to 1.
$$
    E[r_j] = \sum_i^s= r_{ji} \; \times \; p_i
$$

Where:

$E[r_j] $ = Expected Return on a stock $j$

$r_{ji}$ = Anticipated return on stock $j$ in state $i$

$p_i$ = Probability of state $i$ occurring

$s$  = Number of possible states

*Practical Considerations*
- Where to source return and likelihood data for a particular stock?

## Asset Pricing Models
Asset Pricing Models remove some of the subjective issues involved in the estimation of expected returns. APMs are tools that use math and logic to determine the expected return of financial securities. The APMs rely on :
* **linearity**: equation of a straight line or regression
* **perfect information**: assumes that all investors have the access to the same information. 
* **efficient markets**: all information is immediately reflected in the prices of securities.


$$
    E[r_j] = r_f + \beta_j(E[r_m] - r_f )
$$
**Where**:

$E[r_jt]$ = Expected return on a stock j

$E[r_m]$ = Expected return on the market

$r_f$ = Risk free rate (e.g. Yield of T-bills or T-bonds)

$\beta_j$ = Systematic risk (market risk) of stock j