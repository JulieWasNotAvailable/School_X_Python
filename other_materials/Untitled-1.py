# %%
%pip install --upgrade pip
%pip install -Uq rich pandas numpy scipy 
%pip install -Uq matplotlib seaborn plotly

# %%
import math

from rich import print
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats as st

# %%
rides = pd.read_csv('rides_go.csv')
subscriptions = pd.read_csv('subscriptions_go.csv')
users = pd.read_csv('users_go.csv')

# %%
rides['date'] = pd.to_datetime(rides['date'])

# %%
px.histogram(rides, x='duration', marginal='box')

# %%
px.histogram(rides, x='distance', marginal='box')

# %%
for city in users.city.value_counts().index:
    print(
        f"{city:>15}: {users.query('city == @city').shape[0] / users.city.shape[0]:.2%} " +
        f"({users.query('city == @city').shape[0]}/{users.city.shape[0]})"
    )

# %%
px.histogram(
    users, 
    x='age', 
    marginal='box'
)

# %%
users.subscription_type.value_counts()

# %%
data = users.merge(rides, on='user_id')
data['date_month'] = data['date'].dt.month

# %%
px.histogram(data, x='distance', color='subscription_type')

# %%
data_free = data.query('subscription_type == "free"')
data_ultra = data.query('subscription_type == "ultra"')

# %%
data_cd = data
data_cd.duration = data_cd.duration.apply(np.ceil)
#ceiledduration

# %%
users_pivot = pd.pivot_table(
    data_cd, 
    index=['user_id', 'date_month'],
    #columns=['subscription_type'],
    values=['distance', 'duration'], 
    aggfunc={
        'distance': 'sum',
        'user_id': 'count',
        'duration': 'sum',
    }
)
users_pivot.columns = ['month_distance', 'month_duration', 'month_rides']
users_pivot['subscription_type'] = \
    users_pivot.apply(lambda x: users[users.user_id == x.name[0]].iloc[0][-1], axis=1)

# %%
import warnings

def calculate_month_income(series: pd.Series) -> int:
    user_id: int = series.name[0]
    duration: int = np.ceil(series.month_duration)
    rides_count: int = series.month_rides
    subscription_type: str = series.subscription_type

    type_prices = subscriptions[subscriptions.subscription_type == subscription_type]
    
    # тут использую инты для ускорения работы, так как тут всё равно неоткуда появиться
    # дробям в нынешней итерации - всё слишком округлённое по заданию
    # но в идеале бы всё во float
    total_income: int = int(type_prices.subscription_fee)
    total_income += int(rides_count * type_prices.start_ride_price)
    total_income += int(duration * type_prices.minute_price)
    return total_income

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    users_pivot['month_income'] = users_pivot.apply(calculate_month_income, axis=1)

users_pivot.head()

# %% [markdown]
# ##Домашка
# 
# **ttest_ind**
# 
# Calculate the T-test for the means of two independent samples of scores.
# 
# This is a test for the null hypothesis that 2 independent samples have identical average (expected) values. This test assumes that the populations have identical variances by default.
# 
# **ttest_ind_from_stats**
# 
# T-test for means of two independent samples from descriptive statistics.
# 
# This is a test for the null hypothesis that two independent samples have identical average (expected) values.
# 
# **ttest_rel**
# 
# Calculate the t-test on TWO RELATED samples of scores, a and b.
# 
# This is a test for the null hypothesis that two related or repeated samples have identical average (expected) values.
# 
# Examples for use are scores of the same set of student in different exams, or repeated sampling from the same units. The test measures whether the average score differs significantly across samples (e.g. exams).
# 
# **ttest_1samp**
# 
# Calculate the T-test for the mean of ONE group of scores.
# 
# This is a test for the null hypothesis that the expected value (mean) of a sample of independent observations a is equal to the given population mean, popmean.
# 

# %% [markdown]
# Будет ли помесячная выручка от пользователей с подпиской по месяцам выше, чем выручка от пользователей без подписки? <br>
# 
# $H_0$: По месяцам выручка от пользователей с подпиской будет такой же, как выручка от пользователей без подписки <br> 
# $H_1$: По месяцам выручка от пользователей с подпиской будет выше, как выручка от пользователей без подписки

# %%
alpha = 0.05

ultra_sub_mi = users_pivot[users_pivot.subscription_type == "ultra"].month_income
free_sub_mi = users_pivot[users_pivot.subscription_type == "free"].month_income

print (f"Среднеквадратичное отклонение у пользователей с подпиской: {st.tstd(ultra_sub_mi)}")
print (f"Среднеквадратичное отклонение у пользователей без подписки: {st.tstd(free_sub_mi)}")

#This test (ttest_ind) assumes that the populations have identical variances by default. А у нас отклонения разные!
# => нужон другой тест, используем ttest_ind_from_stats

# results = st.ttest_ind(
#     users_pivot[users_pivot.subscription_type == "ultra"].month_income,
#     users_pivot[users_pivot.subscription_type == "free"].month_income,
#     alternative="greater"
# )
#пивалю такая:  4.227438894541133e-29

results = st.ttest_ind_from_stats(
    ultra_sub_mi.mean(),
    st.tstd(ultra_sub_mi),
    ultra_sub_mi.shape[0],
    free_sub_mi.mean(),
    st.tstd(free_sub_mi),
    free_sub_mi.shape[0]
)

if results.pvalue < alpha:
    print ("Отвергаем нулевую гипотезу")
else:
    print ("Нет оснований отвергнуть нулевую гипотезу")

print ("пивалю такая: ", results.pvalue)

# %% [markdown]
# Среднее количество поездок в месяц пользователей с подпиской больше, чем у пользователей без подписки? <br>
# 
# $H_0$: Количество поездок в месяц *одинаковое* для пользователей с подпиской и без подписки <br>
# $H_1$: Количество поездок в месяц *больше* у пользователей с подпиской (чем без)

# %%
ultra_sub = users_pivot[users_pivot.subscription_type == "ultra"].month_rides
free_sub = users_pivot[users_pivot.subscription_type == "free"].month_rides

print (f"Среднеквадратичное отклонение у пользователей с подпиской: {st.tstd(ultra_sub)}")
print (f"Среднеквадратичное отклонение у пользователей без подписки: {st.tstd(free_sub)}")

# Разница в отклонениях в сравнении со средним значением 1.471872931833223 составила 12%
# Снова используем ttest_ind_from_states

# results = st.ttest_ind(
#         users_pivot[users_pivot.subscription_type == "ultra"].month_rides,
#         users_pivot[users_pivot.subscription_type == "free"].month_rides,
#         alternative="greater"
# )
#пивалю такая:  1.0

results = st.ttest_ind_from_stats(
    ultra_sub.mean(),
    st.tstd(ultra_sub),
    ultra_sub.shape[0],
    free_sub.mean(),
    st.tstd(free_sub),
    free_sub.shape[0]
)

if results.pvalue < alpha:
    print ("Отвергаем нулевую гипотезу")
else:
    print ("Нет оснований отвергнуть нулевую гипотезу")

print ("пивалю такая: ", results.pvalue)


# %% [markdown]
# Средняя дистанция поездки "холодные" месяца (с октября по март) отличается от "тёплых"?<br>
# 
# $H_0$: Средняя дистанция поездки в "холодные" месяца (с октября по март) от "тёплых" *не отличается* <br>
# $H_1$: Средняя дистанция поездки в "холодные" месяца (с октября по март) от "тёплых" *отличается*

# %%
warm_months_mask = [False if x in [1,2,3,10,11,12] else True\
                    for x in users_pivot.index.get_level_values("date_month")]

users_pivot["warm_month"] = warm_months_mask

warm = users_pivot[users_pivot["warm_month"] == True].month_distance
cold = users_pivot[users_pivot["warm_month"] == False].month_distance

#средние 3046.1597189227314 3034.31049218464, почти одинаковые, разность незначительна можно ttest_ind
#rel не используем, потому что у нас разные сеты людей - кто-то катался весной, кто-то нет

results = st.ttest_ind(
    users_pivot[users_pivot["warm_month"] == True].month_distance,
    users_pivot[users_pivot["warm_month"] == False].month_distance,
    alternative="two-sided"            
)

if results.pvalue < alpha:
    print ("Отвергаем нулевую гипотезу")
else:
    print ("Нет оснований отвергнуть нулевую гипотезу")

print ("пивалю такая: ", results.pvalue)


# %% [markdown]
# Среднее время езды на самокате - 30 минут?<br>
# 
# $H_0$: Среднее время езды на самокате *равняется 30 минутам* <br>
# $H_0$: Среднее время езды на самокате *не равняется 30 минутам*

# %%
target_value = 30

results = st.ttest_1samp(
    data.duration,
    target_value,
    alternative="two-sided"
)

if results.pvalue < alpha:
    print ("Отвергаем нулевую гипотезу")
else:
    print ("Нет оснований отвергнуть нулевую гипотезу")

print ("пивалю такая: ", results.pvalue)


