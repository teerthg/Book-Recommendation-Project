# Book-Recommendation-Project

This project is a **Collaborative Filtering-based Book Recommendation System** built using Python and Streamlit. It recommends books to users based on similarity with other users using a User-Item Matrix and Cosine Similarity.

---

## 🚀 Demo
🔗 [Live Streamlit App](https://your-streamlit-app-link.streamlit.app)

---

## 📂 Project Structure

```
📁 book-recommender/
├── app.py                    # Streamlit web application
├── user_item_matrix.pkl     # Pickled User-Item Matrix
├── user_similarity_df.pkl   # Pickled User Similarity Matrix
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```

---

## 📊 Features

- Takes **User ID** as input
- Recommends top N books not yet read by the user
- Uses **Cosine Similarity** to find similar users
- Clean and interactive UI with **Streamlit**
- Deployable on **Streamlit Cloud**

---

## 🧠 Recommendation Logic

1. Generate a **User-Item Matrix** from ratings.
2. Compute **Cosine Similarity** between users.
3. For a given User ID:
   - Identify top similar users.
   - Aggregate books those users rated.
   - Filter out books already rated by the current user.
   - Recommend top N books based on average ratings.

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Dependencies

```txt
streamlit
pandas
numpy
```

---

## 🧪 Example Input

- Enter `User ID` = 276729
- Select top N = 5
- Output:
  ```
  1. A Walk to Remember — Score: 8.6
  2. The Notebook — Score: 8.2
  ...
  ```

---

## 🙋‍♀️ Authors

- Teerth Gupta  

---

## 📬 Contact

📧 teerthgupta@email.com 

---

## 📄 License

This project is for academic and personal use only.
