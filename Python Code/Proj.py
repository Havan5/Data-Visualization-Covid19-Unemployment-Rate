import matplotlib.pyplot as plt
from numpy import size
import seaborn as sns
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np


# df = pd.read_csv("UNRATE.csv")

# # sns.set_context('talk')
# # plt.figure(figsize=(50,10))

# plt.title('USA Unemployment Rate')
# ax = sns.lineplot( x = "Date", y = "Value", data = df[(df['Date'] > "2004-01-01") & (df['Date'] < "2021-12-31")])
# ax.set_xlabel("Date", fontsize = 10)
# ax.set_ylabel("Unemployment Rate %", fontsize = 10)
# plt.xticks(["2005-01-01", "2006-01-01","2007-01-01","2008-01-01","2009-01-01","2010-01-01",
#             "2011-01-01","2012-01-01","2013-01-01","2014-01-01","2015-01-01","2016-01-01",
#             "2017-01-01","2018-01-01","2019-01-01","2020-01-01","2021-01-01"],rotation="90", size=10)
# plt.show()



# df2 = pd.read_csv("Unemployment Race.csv")
# df2.plot(x="Race", y="Value", kind="bar")
# plt.title('USA Unemployment Rate By Race')
# plt.xticks(rotation="90", size=8)
# plt.show()


df3 = pd.read_csv("Unemployment Men.csv")
df4 = pd.read_csv("Unemployment Women.csv")

# plt.title('USA Unemployment Rate By Gender')
# ax = sns.lineplot( x = "Date", y = "Men",label="Men", data = df3[(df3['Date'] > "2004-01-01") & (df3['Date'] < "2021-12-31")])
# ax = sns.lineplot( x = "Date", y = "Women",label="Women", data = df4[(df4['Date'] > "2004-01-01") & (df4['Date'] < "2021-12-31")])
# ax.legend()
# ax.set_xlabel("Date", fontsize = 10)
# ax.set_ylabel("Unemployment Rate %", fontsize = 10)
# plt.xticks(["2005-01-01", "2006-01-01","2007-01-01","2008-01-01","2009-01-01","2010-01-01",
#             "2011-01-01","2012-01-01","2013-01-01","2014-01-01","2015-01-01","2016-01-01",
#             "2017-01-01","2018-01-01","2019-01-01","2020-01-01","2021-01-01"],rotation="90", size=10)
# plt.show()

df5 = pd.read_csv("Unemployment rate by sex, race and Hispanic ethnicity.csv")
N = 5
ind = np.arange(N)

width = 0.3 
plt.bar(ind, df5['Women'] , width, label='Women')
plt.bar(ind + width, df5['Men'], width, label='Men')
plt.xticks(ind + width / 2, ('Total','White','Black','Asian','Hispanic'))

# df5.plot(x="Race", y="Men", kind="bar")
# df5.plot(x="Race", y="Women", kind="bar")
plt.title('USA Unemployment Rate By Sex and Race 2020')
plt.xticks(rotation="90", size=8)
plt.legend(loc='best')
plt.show()