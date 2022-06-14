# Assignment Week 3: Some points to note

1. I have mentioned Names and Passenger ID like columns to `Categorical Columns`, which actually donnot belong there.<br>
  My predictions weren't affected since I had dropped all columns with unique features greater than 25 later in the notebook.
  
2. For getting `X_train and X_test` devoid of `target column: transported`, and getting it assigned to `y_train and y_test`,<br>
   we need `NOT` to do this 👇
   
```py
   
X = df.copy().drop(df[['Transported']], axis=1)
y = pd.Series(df['Transported']).values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=2022)
```

Rather, we can directly do:
```py
X_train, X_test, y_train, y_test = train_test_split(df.drop(['transported'], axis=1), df['transported], test_size=0.15, random_state=2022)
```
