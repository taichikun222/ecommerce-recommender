# E-Commerce Product Recommender

## Problem Statement
Recommend products to users based on their past purchase behavior, to help drive
cross-sell and repeat purchases.

- **Task type:** Recommendation system
- **Approach:** Item-based collaborative filtering (products bought by similar
  users), compared against a content-based baseline (similar category/price)
- **Success metric:** Precision@5 - of the top 5 recommended products, how many
  did the user go on to actually buy
- **Business KPI:** Increased cross-sell rate / average order value

### Why a recommender, and not forecasting or clustering?
Demand forecasting predicts *how much* of a product will sell in aggregate - it
doesn't tell you what to show a specific customer. Clustering groups similar
customers but still leaves the question of what to recommend unanswered. A
recommender system directly targets the business goal: surface the right
products to the right person at checkout or on a product page.

This was only feasible because of a repeat-purchase check: **88% of the 2,890
users have placed 2+ orders**, which is enough repeat-purchase signal for
collaborative filtering ("customers like you also bought...") to have data to
work with. If most users only ever ordered once, there would be no purchase
history to find similar users or items from, and a recommender would reduce to
random guessing.

### Why Precision@5, not RMSE/accuracy?
This is a ranking problem, not a regression or classification problem - there's
no single "correct" numeric value to predict, and no fixed set of labels. What
matters is whether the products actually placed in front of the customer are
ones they want. Precision@5 mirrors how the recommendation would actually be
deployed (e.g., a "recommended for you" widget showing ~5 products), and it
answers the practical question directly: **of the 5 products we'd show, how
many did the customer go on to buy?**

### Tying the metric to the business KPI
A higher Precision@5 means a larger share of the recommended slots are products
the customer actually wants - which is what drives the KPI: more of those
recommendations convert into add-on purchases, raising the cross-sell rate and
average order value per transaction. A low Precision@5, by contrast, means the
widget is mostly showing noise, which wastes the placement and doesn't move the
business metric.

## Dataset
10,000 synthetic e-commerce orders, 2,890 users, 500 products.
Source: Kaggle - E-Commerce Orders Dataset
See `data/dataset_source_readme.md` for the original data dictionary.

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

## How to Run
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Open `notebooks/01_eda_and_recommender.ipynb` in VSCode and run the cells top to bottom.
