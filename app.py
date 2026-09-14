"""Local demo app for the product recommender (Step 8 - optional local deployment).

Run with: python app.py
Then open http://127.0.0.1:5000
"""
from flask import Flask, render_template, request

from src.recommender import explain_recommendation, load_recommender, recommend_products

app = Flask(__name__)

df, user_item, item_sim_df = load_recommender()
valid_user_ids = set(user_item.index)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    user_id_input = ""

    if request.method == "POST":
        user_id_input = request.form.get("user_id", "").strip()
        try:
            user_id = int(user_id_input)
        except ValueError:
            error = "Please enter a numeric user ID."
        else:
            if user_id not in valid_user_ids:
                error = f"User {user_id} not found (valid range: {min(valid_user_ids)}-{max(valid_user_ids)})."
            else:
                bought = user_item.loc[user_id]
                bought_products = bought[bought > 0].index.tolist()
                recs = recommend_products(user_id, user_item, item_sim_df, n=5)

                if not recs:
                    error = "No recommendations available for this user (cold-start: no purchase history)."
                else:
                    explanations = {
                        rec: explain_recommendation(rec, bought_products, item_sim_df)
                        for rec in recs
                    }
                    result = {
                        "user_id": user_id,
                        "bought_products": bought_products,
                        "recommendations": recs,
                        "explanations": explanations,
                    }

    return render_template(
        "index.html", result=result, error=error, user_id_input=user_id_input
    )


if __name__ == "__main__":
    app.run(debug=True)
