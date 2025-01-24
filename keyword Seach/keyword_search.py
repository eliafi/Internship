import pandas as pd

words = ["buy","soft","prices","cheap","custom","expensive"]

products = ["sofas","covertible sofas","love seats","recliners","sofa beds"]


keywords = []

for word in words:
    for product in products:
        keywords.append([ product, word + " " + product])
        keywords.append([product, product + " " + word ])



# print(keywords)


keywords_df = pd.DataFrame(keywords, columns= ["Ad Group", "Keyword"])
print(keywords_df)

keywords_df["Campaign"] = "SEM_Sofas"
keywords_df["Criterion Type"] = "Exact"

print(keywords_df)

keywords_df.to_csv("keywords.csv", index=False)