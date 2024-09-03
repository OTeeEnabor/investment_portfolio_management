# Understanding Price, Risk, and Return Relationships & Calculating Returns

These notes introduce the concepts of price, risk, returns and how they are related. 

## What is Price?

The **price** of a stock is what you pay to buy/sell an asset in an open market. It is also known as Market price, market value. This price is usually compared with the intrinsic price and which is the price at which the asset is actually valued - determined by fundamentals such as industry in which stock operates in, company financials, etc.

If market price is higher than intrinsic price - **overvalued**
if market price is lower than intrinsic price - **undervalued**.
**fair value** market price is equal to intrinsic price.


## What is Return?

The return refers to the amount of money mde from an investment, expressed in % terms. 

## What is Risk?
The risk can have different meanings and measures. However, generally in finance, an accepted definition of risk(or type) - `likelihood or value of incurring loss in money (investment)`. 

**Law of one price**, for any 2 stocks that identical in all aspects and have the same expected return, they should have the same price. arbitrage opportunity exits if the prices aren't equal - one can earn money with 0 investment (`risk-free`). 

For example their are two identical stocks:
- **Delta PLC**: `$100/share` (expected return - `12%`, risk-`5%`)
- **Open PlC**: `$120/share` (expected return - `12%`, risk-`5%`)
There exists an opportunity to sell (short), buy (long), do both (hedge).
By this I mean:
- **Sell Open Plc (short)** - because I believe it is overvalued (based on law of one price, Open should be at Delta's price of 100), there for by selling - I believe in the near future Open will drop to $100. 
- **Buy Delta (long)** - Here I believe that Delta is undervalued and its fair price should be the same as Open's $120, so I buy because I believe in the future the price will increase to $120.
- **Hedge (buy and sell)** - here I do the both of the above to spread my risk. 

Another example
There are two stocks that have identical returns - `x%`, however they have different risks - one is more riskier than the other, what should the pricing look like?

I think that the stock with the higher risk should have a lower price because it does not make sense for me to `bet` on a riskier asset when I get no advantage from taking on the risk - i.e, same expected return. 

*Riskier assets are **worth** less than safer assets and vice versa.*
## Important Relationships 
Value and risk are have a negative correlation relationship - as risk increases, the value of  asset should decrease. 

Risk and return (expected) have a proportional relationship, as risk increases, **expected return** should increase - proportionally - positive correlation

**keywords**: price convergence

# What is Shorting?
Selling an asset that **you do not own** and buying it back when the price decreases. The difference between the sell amount and buy back amount is profit. 

Borrow the shares from broker, then sell them at the current price, when share price decreases, buy them back at lower price, return them to the broker, pay interest on loan, profit the rest.
Risks involved - price of share could increase to infinity therefore you would have to buy back the shares at this infinity price. simply put there is no upper bound to how much you can lose when shorting.

# Calculating Stock Returns
Is there a difference between profit and returns? or are they the same thing expressed in **different units**?

**profit without dividends**

$Profit = P_{t+1} - P_{t}$

$return (r) = \frac{P_{t+1} - P_{t}}{P_{t}} \equiv \frac{P_{t+1} }{P_{t}} - 1$


**Profit with dividends**

$profit = SellingPrice + Dividends - PurchasePrice$

**return with dividends**

$r = \frac{P_{t+1} + Div_{t+1} - P_{t}}{P_{t}} \equiv \frac{P_{t+1} + Div_{t+1}}{P_{t}} - 1$





