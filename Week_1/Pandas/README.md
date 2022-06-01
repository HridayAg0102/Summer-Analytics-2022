# Some General Errors
1. when we use `Dataframe.drop('column_name', inplace = True)` and if we run that cell again after running it first time, it will show an error that the `<column name>` doesn't exist.
This happens since the column was natively removed from the dataframe, and hence, you are trying to drop an `UNAVAILABLE COLUMN`.
