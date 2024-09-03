## State Contingent Expected Returns

The mean based Expected Return is limited by the fact that is based entirely on historic data/information. The historic performance of a stock is not a solid indicator that it will continue with that performance in the future. 

**State Contingent Expected Returns** are used to overcome this limitation. The **expected returns** are estimated based on the condition of **future events/states** occurring.
This method is only as good as the accuracy of:
* anticipated returns, and
* probabilities of future events occurrences.

**Example**
Analysts at **Open Delta Consulting** have a 1 year forecast for the returns of Ethereum (ETH) as follows:
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

**Generalised Asset Pricing Model**
$$
    E[r_{jt}] = \alpha + \beta_{j}F_t + \epsilon_t
$$

**where**:

$E[r_{jt}]$ = Expected return on a stock j at time t

$F_t$ = Factor that impacts the expected return of j at time t

$\alpha$ = Intercept term (value of $E[r_j]$ when F = 0)

$\beta_j$ = Slope (impact of expected return when F changes)


**Capital Asset Pricing Model (CAPM)**

In CAPM, the return of an asset is solely based on its relationship with the market (JSE, NYSE, etc). This model will ignore other sentimental influences such as - asset culture, values, prospects or any other asset specific element that relies on "feelings".The model simply relies on the "power of diversification". The CAPM is interested in the expected return and excess return, which is the additional return that you get above the risk free return. Simply, the return you get for taking risk. 

$\alpha$ and $\epsilon_t$ are set to zero because the CAPM model says that the expected return is dependent on the assets relationship with the market. 


$$
    E[r_j] = r_f + \beta_j(E[r_m] - r_f )
$$
**Where**:

$E[r_jt]$ = Expected return on a stock j

$E[r_m]$ = Expected return on the market

$r_f$ = Risk free rate (e.g. Yield of Treasury bills or Treasury bonds)

$\beta_j$ = Systematic risk (market risk) of stock j

Other AP models work on the assumption that a stock's return is impacted by 2 or more factors and not just the market portfolio. Look up the **Arbitrage Pricing Theory for AP models** - think of it is as a multi-linear regression (return) model. 

Other multi-factor models

- Fama French 3 Factor Model - stock returns are affected by the following factors
    - market portfolio
    - size of the firm
    - value vs growth firm

$$
    E[r_j] = r_f + \beta_j(E[r_m] - r_f ) + \beta_{2}SMB + \beta_{3}HML
$$
**Where**:
SMB = Returns of small firms minus returns of big firms ('size factor')
HML = Returns of high book-to-market ("value") firms minus returns of low book-to-market ("growth") firms ("value premium")

- Cahart 4 Factor Model
The 4-factor model is just addition to the 3-factor model
$$
    E[r_j] = r_f + \beta_j(E[r_m] - r_f ) + \beta_{2}SMB + \beta_{3}HML + \beta_{4}GP
$$
**Where**:
WML = Returns "winner" firms minus returns of "loser" firms (momentum portfolio / factor , aka MOM factor) 

- Fama French 5 Factor Model 

Calculates the return by taking into account company profitability (gross profitability)
$$
    E[r_j] = r_f + \beta_j(E[r_m] - r_f ) + \beta_{2}SMB + \beta_{3}HML + \beta_{4}WML + \beta_{5}GP
$$
**Where**:
GP = Returns of "high gross profit" firms minus returns of "low gross profit" firms ("probability portfolio / factor")

MRP = $E[r_{m}] - r_f$
