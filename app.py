
import streamlit as st
import pandas as pd

# Load data
user_item_matrix = pd.read_pickle("user_item_matrix.pkl")
user_similarity_df = pd.read_pickle("user_similarity_df.pkl")

# Recommender logic
def get_recommendations(user_id, n=10):
    if user_id not in user_item_matrix.index:
        return ["❌ User ID not found. Try another ID."]

    # Identify similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    similar_users = similar_users.drop(user_id)  # exclude self
    top_similar = similar_users.head(5).index

    # Aggregate ratings
    similar_user_ratings = user_item_matrix.loc[top_similar]
    average_ratings = similar_user_ratings.mean(axis=0)

    # Filter out books already rated
    already_rated = user_item_matrix.loc[user_id]
    rated_books = already_rated[already_rated > 0].index
    new_books = average_ratings.drop(rated_books)

    return new_books.sort_values(ascending=False).head(n)

# ─────────────────────────────────────
# Streamlit App UI
# ─────────────────────────────────────

st.set_page_config(page_title="Group Book Recommender", page_icon="📚")
st.title("📖 Personalized Book Recommender")

user_id = st.number_input("🔢 Enter User ID", min_value=0, step=1)
num_recs = st.slider("🎯 Number of recommendations", min_value=1, max_value=15, value=5)

if st.button("🔍 Get Recommendations"):
    st.subheader("📘 Top Picks for You:")
    output = get_recommendations(user_id, num_recs)

    if isinstance(output, list):
        st.warning(output[0])
    else:
        for idx, (book, score) in enumerate(output.items(), start=1):
            st.markdown(f"**{idx}.** {book} — _Score: {score:.2f}_")
