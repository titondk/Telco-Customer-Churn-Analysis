# Telco Customer Churn Analysis

## Project Overview
This project analyzes customer churn for a telecommunications company using the **Telco Customer Churn** dataset. The goal is to identify key drivers of churn and provide actionable business recommendations. The analysis includes data cleaning, metric calculation, and data visualization using Python (pandas, seaborn, matplotlib).

## Key Findings (Executive Summary)

- **Overall churn rate is 26.5%** – meaning more than one in four customers leave.
- **Contract type is the strongest predictor** of churn:
  - Month-to-month contracts churn at **42.7%**.
  - One-year contracts: **11.3%**.
  - Two-year contracts: only **2.8%**.
- **Payment method matters significantly**:
  - Electronic check customers churn at **45.3%**.
  - Automatic methods (bank transfer, credit card) have churn rates below 17%.
- **New customers are high risk**:
  - Tenure < 1 year: **48.3%** churn.
  - Tenure 1–3 years: **25.7%** churn.
  - Tenure > 3 years: **11.9%** churn.
- **Fiber optic internet customers churn more** (41.9%) compared to DSL (19.0%) or no internet (7.4%).
- **Add‑on services reduce churn** (among internet customers):
  - Online Security: 14.6% churn.
  - Tech Support: 15.2% churn.
  - Without these services, churn is higher.
- **Demographics**:
  - Senior citizens churn at 41.7% vs. 23.6% for non‑seniors.
  - Customers with dependents churn less (15.5%) than those without (31.3%).
- **Paperless billing** is associated with higher churn (33.6%) than paper billing (16.3%).

## Visualizations Included

The project contains the following bar charts (all with percentage axes):

1. **Churn Rate by Contract Type** – Month‑to‑month is the highest.
2. **Churn Rate by Payment Method** – Electronic check is the worst.
3. **Churn Rate by Tenure Group** – Very high for new customers.
4. **Churn Rate by Internet Service Type** – Fiber optic leads churn.
5. **Churn Rate by Add‑on Services** – Online Security and Tech Support lower churn.
6. **Churn Rate by Demographics** – Seniors and no‑dependents groups churn more.
7. **Churn Rate by Billing Type** – Paperless billing shows higher churn.

Each chart is properly labeled, uses a percent formatter, and includes a clear title.

## Business Recommendations

Based on the analysis, the company should:

- **Convert month‑to‑month customers** to longer contracts with incentives (e.g., discounts, free add‑ons).
- **Discourage electronic check** by offering small discounts for automatic payment methods.
- **Target new customers** with onboarding campaigns (e.g., welcome calls, setup assistance) to reduce early churn.
- **Promote add‑on services** (Online Security, Tech Support) to internet customers – they significantly reduce churn.
- **Review fiber optic service quality** – it has the highest churn among internet types.
- **Address senior citizen concerns** – they churn at a much higher rate. Offer senior‑specific support or plans.

## Technologies Used

- Python 3.x
- pandas – data manipulation
- numpy – numerical operations
- seaborn & matplotlib – data visualization
- VS Code

## How to Run the Project

1. Clone this repository.
2. Install required libraries:
   ```bash
   pip install pandas numpy seaborn matplotlib
