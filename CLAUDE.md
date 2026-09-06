# Project Context for Claude Code

## What This Is
A capstone assignment (100 points total) applying the full ML lifecycle to a
real-world problem. Domain chosen: **eCommerce - Recommend products to users**.

## Problem Statement
- **Task type:** Recommendation system
- **Approach:** Item-based collaborative filtering (products bought by similar
  users), compared against a content-based baseline (category/price similarity)
- **Success metric:** Precision@5 - of the top 5 recommended products, how many
  did the user go on to actually buy
- **Business KPI:** Increased cross-sell rate / average order value
  (relevant since the user runs a distribution + ecommerce business)

## Dataset
- File: `data/ecommerce_orders_10k_updated.csv`
- Source: Kaggle - E-Commerce Orders Dataset (10K synthetic transactions)
- 10,000 orders, 2,890 unique users, 500 unique products
- Columns: order_id, user_id, product_id, category, price, qty, total_price,
  order_date, country, customer_segment (Low/Mid/High-Value)
- Full data dictionary: `data/dataset_source_readme.md`
- 88% of users have 2+ orders - enough repeat-purchase signal for collaborative filtering

## Decisions Already Made (don't relitigate without discussion)
- Went with recommendation over demand forecasting or clustering - confirmed
  feasible based on repeat-purchase rate check.
- Chosen metric is Precision@5, not RMSE/accuracy (this is not a regression/classification task).
- First model built: item-based collaborative filtering using cosine similarity
  on a user-item purchase matrix. Lives in `notebooks/01_eda_and_recommender.ipynb`.

## Project Structure
```
ecommerce-recommender/
├── data/            # raw dataset + source readme
├── notebooks/       # exploration + modeling notebooks
├── src/             # reusable python scripts (loading, recommender logic)
├── models/          # saved model artifacts
├── requirements.txt
└── README.md
```

## Assignment Requirements & Grading Rubric (100 pts total)
Keep every deliverable below in mind - this is graded against a rubric, not
just "does it run."

| Step | Deliverable | Points | What "Outstanding" looks like |
|---|---|---|---|
| 1. Problem Framing | Problem statement + task type + target metric | 10 | Strong business + data science framing, task type justified, metrics measurable and tied to business KPI |
| 2. Data Understanding | Dataset overview + data dictionary | 10 | Source cited, missing values/outliers/distributions covered, complete data dictionary |
| 3. Preprocessing/EDA/Feature Engineering | EDA + Feature Engineering report, reproducible code | 10 | Documented cleaning, insightful EDA with visuals, creative feature engineering, at least one feature selection AND one dimensionality reduction method (e.g. PCA), both justified |
| 4. Model Implementation | Trained models, metrics, comparison | 20 | Multiple approaches implemented and tuned (e.g. collaborative filtering AND content-based), metrics compared, saved model artifacts in `models/`, clear reasoning for final choice |
| 5. Ethics & Bias Auditing | Bias & Fairness Analysis section | 20 | Explainability applied (SHAP/LIME/PDP/ICE where relevant), limitations discussed (imbalance, leakage, overfitting, cold-start users), fairness checked across groups (country, customer segment) WITH fairness metrics, concrete mitigations proposed |
| 6. Final Presentation | Two slide decks: technical + business | 10 | Technical deck for peers (methodology, metrics, visuals); business deck for executives (ROI, risk, strategy); 8–12 slides each, polished |
| 7. GitHub Upload | Public repo, structured like open source project | 15 | src/, notebooks/, data/, models/ present; README + requirements.txt + final report; clean commit history |
| Bonus | Creativity / polish | +5 | Goes beyond expectations in design, clarity, or innovation |
| Optional Step 8 | Local deployment (Flask/FastAPI/Dash) + MLOps | - | Not required for the core grade, but demo of the recommender as a running app is worth it if time allows |
| Optional Step 9 | Document GenAI usage | - | Note that Claude was used for planning, code scaffolding, and this project setup - required if this step is attempted |

## What's Still Needed (as of last session)
- [ ] Build content-based recommender as a comparison baseline (currently only collaborative filtering exists)
- [ ] Add feature selection + dimensionality reduction step (not yet done - required for full Step 3 credit)
- [ ] Add explainability discussion (SHAP/LIME are less standard for CF recommenders - need to think through what's appropriate here, e.g. explaining *why* a product was recommended)
- [ ] Expand the bias/fairness check already started in the notebook into a full write-up with fairness metrics
- [ ] Save model artifacts (similarity matrix, etc.) to `models/`
- [ ] Write the EDA + Feature Engineering report (currently just notebook cells, needs a narrative writeup)
- [ ] Build two slide decks (technical + business)
- [ ] Set up GitHub repo and push
- [ ] (Optional) Flask/FastAPI demo app
- [ ] (Optional) Document GenAI usage if claiming Step 9

## Working Style Preferences
- Keep explanations simple and non-jargon-heavy - the user is not a full-time data scientist, they run a distribution + ecommerce business and are learning this for a course.
- Prefer small, clear code changes over large rewrites.
- Confirm before making big structural decisions (e.g. switching modeling approach).
