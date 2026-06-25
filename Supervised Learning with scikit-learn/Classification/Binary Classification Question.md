# Binary Classification

There are two types of supervised learning—classification and regression. Binary classification is used to predict a target variable that has only two labels, typically represented numerically with a zero or a one.

The `.head()` of a dataset, `churn_df`, is shown below. You can expect the rest of the data to contain similar values.

```text
   account_length  total_day_charge  total_eve_charge  total_night_charge  total_intl_charge  customer_service_calls  churn
0             101             45.85             17.65                9.64               1.22                       3      1
1              73             22.30              9.05                9.98               2.75                       2      0
2              86             24.62             17.53               11.49               3.13                       4      0
3              59             34.73             21.02                9.66               3.24                       1      0
4             129             27.42             18.75               10.11               2.59                       1      0
```

Looking at this data, which column could be the target variable for binary classification?

### Answer the question (50XP)

**Possible Answers**
*Select one answer:*

1. "customer_service_calls"
2. "total_night_charge"
3. "churn"
4. "account_length"
