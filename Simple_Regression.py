
import matplotlib.pyplot as plt
import numpy as np
import polars as pl

df_csv = pl.read_csv("datasets/weight-height.csv", try_parse_dates=True)

male_df = df_csv.filter(pl.col("Gender") == "Male")
female_df = df_csv.filter(pl.col("Gender") == "Female")

def hennsasekiwa(df,params1,params2):
    hennsasekiwa_expr = ((pl.col(params1) - pl.col(params1).mean()) * (pl.col(params2) - pl.col(params2).mean())).sum()
    return df.select(hennsasekiwa_expr).item()

#maleの計算
Sxx = hennsasekiwa(df_csv.filter(pl.col("Gender") == "Male"),"Height","Height")
Sxy = hennsasekiwa(df_csv.filter(pl.col("Gender") == "Male"),"Height","Weight")
Syy = hennsasekiwa(df_csv.filter(pl.col("Gender") == "Male"),"Weight","Weight")

beta1 = Sxy/Sxx
beta0_expr = pl.col("Weight").mean() - beta1 * pl.col("Height").mean()
beta0 = df_csv.filter(pl.col("Gender") == "Male").select(beta0_expr).item()
print(beta1)
print(beta0)

x = np.arange(55,80)
y = beta0 + beta1 * x
plt.plot(x,y,color = "blue")

#femaleの計算
Sxx = hennsasekiwa(df_csv.filter(pl.col("Gender") == "Female"),"Height","Height")
Sxy = hennsasekiwa(df_csv.filter(pl.col("Gender") == "Female"),"Height","Weight")
Syy = hennsasekiwa(df_csv.filter(pl.col("Gender") == "Female"),"Weight","Weight")

beta1 = Sxy/Sxx
beta0_expr = pl.col("Weight").mean() - beta1 * pl.col("Height").mean()
beta0 = df_csv.filter(pl.col("Gender") == "Female").select(beta0_expr).item()
print(beta1)
print(beta0)

x = np.arange(55,80)
y = beta0 + beta1 * x
plt.plot(x,y,color = "orange")

plt.scatter(male_df["Height"],male_df["Weight"],marker='1')
plt.scatter(female_df["Height"],female_df["Weight"],marker='2')

plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('male of height and weight')
plt.show()