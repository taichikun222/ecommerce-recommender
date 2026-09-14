"""Collaborative-filtering recommender: loading and inference logic.

Reuses the same approach as notebooks/01_eda_and_recommender.ipynb (Step 4),
backed by the similarity matrix saved to models/item_similarity_cf.pkl.
"""
import pickle
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "ecommerce_orders_10k_updated.csv"
MODEL_PATH = BASE_DIR / "models" / "item_similarity_cf.pkl"


def load_recommender():
    """Load the user-item purchase matrix and the saved item-item similarity matrix."""
    df = pd.read_csv(DATA_PATH)
    user_item = pd.crosstab(df["user_id"], df["product_id"])
    user_item = (user_item > 0).astype(int)

    with open(MODEL_PATH, "rb") as f:
        item_sim_df = pickle.load(f)

    return df, user_item, item_sim_df


def recommend_products(user_id, user_item, item_sim_df, n=5):
    """Recommend n products for a user based on items similar to what they've already bought."""
    if user_id not in user_item.index:
        return []
    bought = user_item.loc[user_id]
    bought_products = bought[bought > 0].index.tolist()

    scores = item_sim_df[bought_products].sum(axis=1)
    scores = scores.drop(labels=bought_products, errors="ignore")
    return scores.sort_values(ascending=False).head(n).index.tolist()


def explain_recommendation(recommended_product, bought_products, item_sim_df, top_k=3):
    """Show which past purchase(s) drove a given recommendation, and how similar they are."""
    sims = item_sim_df.loc[recommended_product, bought_products].sort_values(ascending=False)
    return [(product, round(score, 3)) for product, score in sims.head(top_k).items()]
