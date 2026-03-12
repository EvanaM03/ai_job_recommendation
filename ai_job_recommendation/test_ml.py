# test_ml.py
import pandas as pd
import numpy as np
from django.db.backends import mysql
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Connect to MySQL (Directly, not via Django ORM)
# This allows you to test data fetching without loading the whole Django environment
conn = mysql.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='job_recommender_db'
)

# 2. Load Data into Pandas
query = "SELECT id, title, description FROM jobs"
jobs_df = pd.read_sql(query, conn)

# 3. Prepare Data for Cosine Similarity
# Combine title and description into one text column
jobs_df['text'] = jobs_df['title'] + " " + jobs_df['description']

# 4. Vectorize Text (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(jobs_df['text'])

# 5. Calculate Similarity
# Let's say we want to find jobs similar to Job ID 1
job_id = 1
job_index = jobs_df[jobs_df['id'] == job_id].index[0]

# Calculate cosine similarity between this job and all others
similarities = cosine_similarity(tfidf_matrix[job_index], tfidf_matrix)

# 6. Get Top 5 Recommendations
similar_indices = similarities[0].argsort()[-5:][::-1]

print(f"Jobs similar to Job ID {job_id}:")
for i in similar_indices:
    if i != job_index:
        print(f"- {jobs_df.iloc[i]['title']} (Score: {similarities[0][i]})")

conn.close()