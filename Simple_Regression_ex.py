import matplotlib.pyplot as plt
import numpy as np
import polars as pl
df_test = pl.read_csv("datasets/test.csv", try_parse_dates=True)

def hennsasekiwa(df,params1,params2):
    hennsasekiwa_expr = ((pl.col(params1) - pl.col(params1).mean()) * (pl.col(params2) - pl.col(params2).mean())).sum()
    return df_test.select(hennsasekiwa_expr).item()

Sxy = hennsasekiwa(df_test,"x","y")
Sxx = hennsasekiwa(df_test,"x","x")
Syy = hennsasekiwa(df_test,"y","y")

beta1 = Sxy/Sxx
beta0_expr = pl.col("y").mean() - beta1 * pl.col("x").mean()
beta0 = df_test.select(beta0_expr).item()
print(beta1)
print(beta0)

x = np.arange(1,7)
y = beta0 + beta1 * x
plt.plot(x,y,color = "blue")

plt.plot(df_test["x"],df_test["y"],'.')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('pyplot interface')
plt.show()


