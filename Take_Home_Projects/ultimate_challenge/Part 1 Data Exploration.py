# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib as plt


# %%
logins = pd.read_json('../logins.json', orient='values')


# %%
logins.head()


# %%
logins['login_count'] = 1


# %%
logins.set_index(pd.to_datetime(logins['login_time']), inplace=True)


# %%
logins_15 = logins.resample('15min').sum()


# %%
logins_15.head()


# %%
logins_15.reset_index(inplace=True)


# %%
logins_15.head()


# %%
logins_15['month'] = logins_15['login_time'].dt.month
logins_15['day'] = logins_15['login_time'].dt.day
logins_15['hour'] = logins_15['login_time'].dt.hour
logins_15['minute'] = logins_15['login_time'].dt.minute


# %%
logins_15.head()


# %%
logins_15.plot(x='login_time', y='login_count')


# %%
logins_15[logins_15['login_count'] >= 50].head(100)


# %%
logins_15.describe()


# %%
logins_15_month = logins_15[logins_15['month'] == 3]


# %%
logins_15_month.head()


# %%
logins_15_month.describe()


# %%
logins_15_week = logins_15_month[logins_15_month['day'] >= 1]
logins_15_week = logins_15_month[logins_15_month['day'] <= 7]


# %%
logins_15_week.head()


# %%
logins_15_week.describe()


# %%
logins_15_day = logins_15_month[logins_15_month['day'] == 5]


# %%
logins_15_day.head(100)


# %%
logins_15_day.describe()


# %%
logins_15_day_weekend = logins_15_month[logins_15_month['day'] == 8]


# %%
logins_15_day_weekend.head(100)


# %%
logins_15_day_weekend.describe()


# %%
logins_15_month.plot(x='login_time', y='login_count')
logins_15_week.plot(x='login_time', y='login_count')
logins_15_day.plot(x='login_time', y='login_count')
logins_15_day_weekend.plot(x='login_time', y='login_count')


# %%
