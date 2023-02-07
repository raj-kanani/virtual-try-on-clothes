# import numpy as np
# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# from nltk.corpus import stopwords
# import string
# data = pd.read_csv("Myntra Kurtis.csv")
# print(data.head())
#
# data = pd.read_csv("Myntra Kurtis.csv")
# print(data.tail())
# print(data.describe())
#
# print(data.info())
# print(data.isnull().sum())
# data = data.drop("Image",axis=1)
# data = data.dropna()
# print(data.shape)
# text = " ".join(i for i in data["Brand Name"])
# stopwords = set(STOPWORDS)
# wordcloud = WordCloud(stopwords=stopwords,
#                       background_color="white").generate(text)
# plt.figure( figsize=(15,10))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()  highest_rated = data.sort_values(by=["Product Ratings"],
#                                  ascending=False)
# highest_rated = highest_rated.head(10)
# print(highest_rated[['Product Info', "Product Ratings", "Brand Name"]])
# # score = (n1/(n1+m1) * a1) + (m1/(m1+n1) * m1r)
# Mr = data['Product Ratings'].mean()
# m = data['Number of ratings'].quantile(0.9)
# n = data['Number of ratings']
# a = data['Product Ratings']
# # data["Score"] = (n1 / (n1 + m1) * a1) + (m1 / (m1 + n1) * m1r)
#
# Recommendations = data.sort_values('Score', ascending=False)
# print(recommendations[['Brand Name', 'Product Info',
#                        'Product Ratings', 'Score',
#                        'Selling Cost', 'Discount']].head(10))

########################### dressing room #################3

import cv2
import numpy as np

# Load the clothing image and create a mask
clothing = cv2.imread("000010_1.jpg")
gray = cv2.cvtColor(clothing, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Load the person image and create a mask
person = cv2.imread("000020_1.jpg")
gray = cv2.cvtColor(person, cv2.COLOR_BGR2GRAY)
_, mask_person = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Use the masks to combine the clothing and person images
result = cv2.bitwise_and(person, person, mask=mask_person)
result = cv2.addWeighted(result, 1, clothing, 1, 0)

# Display the final image
cv2.imshow("Virtual Dressing Room", result)
cv2.waitKey(0)
cv2.destroyAllWindows()