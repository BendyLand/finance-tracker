import numpy as np
import pandas as pd

np.random.seed(42)

student_ids = np.arange(1, 11)
math_scores = np.random.randint(50, 101, size=10)
english_scores = np.random.randint(50, 101, size=10)
science_scores = np.random.randint(50, 101, size=10)
data = np.column_stack((student_ids, math_scores, english_scores, science_scores))

print(f"NumPy Array:\n{data}")

columns = ["StudentID", "Math", "English", "Science"]
df = pd.DataFrame(data, columns=columns)
print(df)

