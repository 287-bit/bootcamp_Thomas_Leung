# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
To minimize the risk of a porfolio that has two stocks. When an investor has a portfolio that has two stocks, he may be interested to know how should he distribute the weightings between two stocks so that he can minimize the porfolio's risk.

## Stakeholder & User
-Who decides: Investors  
-Who uses the output: Investors  
-Timing & workflow context: Monthly, Quarterly, or Annually

## Useful Answer & Decision
-Descriptive: This model will determine the outcome based on the historical data of two stocks that the investors selected.  
-Metric: Portfolio returns and asset allocation  
-Artifact to Deliver: The model will present the Efficient Frontier Chart and the optimal asset allocation to the investors. 

## Assumptions & Constraints
-Data Availability: This model assumes that daily closing prices of the two stocks are readily available.  
-Capacity: This model assumes minimal storage and operational capacity.  
-Constraints: This model is limited to long strategy.

## Known Unknowns / Risks
-Risks: A portfolio with only two stocks might have high correlation. Also, hisotical data such as stock prices may be distorted due to certain historical events.  
-How to test: To check any potential risks, we will utilize statistical tools to examine the two stocks' correlation and check for data outliers to identify significant movements. 

## Lifecycle Mapping
Goal → Stage → Deliverable
- <Goal A> → Problem Framing & Scoping (Stage 01) → <Deliverable X>
- ...
## Repo Plan
data/, src/, notebooks/, docs/ ; cadence for updates