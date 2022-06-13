# Summer-Analytics-2022 course
[Link to the course](https://iitg.ac.in/sa/caciitg/sa22/course/)

```
Some Tools and Technologies for ML model:
1. for creating UI of model - Gradio
2. for hosting ML model - Higging Faces (majorly used for NLP, but can be used here... read more on its website)
and many more .... still dicovering :)
```

# Some Questions I came across the course:

1. In Pandas dataframe, why we use `df[exp1 |/& exp2]` instead of `df[exp1 or/and exp2]`? <br>
Ans. -[ See this question](https://stackoverflow.com/questions/21415661/logical-operators-for-boolean-indexing-in-pandas)
<hr>

2. How to use pyplot.imshow() in pandas? <br>
Ans. -[Link to Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)
<hr>

3. <strong>How to see documentation in Jupyter notebook itself?</strong> <br>
Ans. in the function parthesis `()`, press `SHIFT + TAB`. on pressing it `4` times, <br>
this will a complete seperate page for the complete docs.
<hr>

4. Why do we regularize all parameters in the same way?
 For eg.
 in the image below: 
<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172717818-5c174ea7-7539-4df6-8b39-af808f2b8d8c.png" height=300></p>

if we want that effect of parameters, $\theta_1$ and $\theta_2$ isn't neglected, how can we handle that? since in the [orginal formula](https://user-images.githubusercontent.com/76818035/172408291-cd0d6891-7a75-4427-abc4-3205742c9265.png), we multiply $\lambda$ with all the weights from $\theta_1$ to $\theta_n$ (where n is the number of features.), How to handle that? <br><br>
Ans: 
- Read here 👉 [LINK](https://stats.stackexchange.com/questions/230013/why-regularize-all-parameters-in-the-same-way)
- Regularization Folder [Link](./Week_3/Regularization)
<hr>

5. If we are getting parameters of higher power like $x^2$ or above in the Hypothesis of Linear Regression, how is it linear? <br>
Ans: For increasing the complexity of model, or to increase the effects of parameters, we apply higher degrees to them like $x^2$, $x^3$ ...
Those are inserted in the model as : <br>
$X_0$,  <br> $X_1$, <br>   $X_2 = X_0^2$,  <br>   $X_3 = X_1^4$ <br>   etc.

So, the new hypothesis may actually represent something like: <br>

![image](https://user-images.githubusercontent.com/76818035/172721718-9680bc9c-2a13-48ab-ae24-3c88fd31d581.png)

<hr>

6. When should we use `.predict()` and `.predict_proba()` in Scikit-learn? <br>
Ans: 
- predict_proba will give out the probabilities while predict will give the class value.
- Class value can be used wherever the evaluation metric is accuracy, recall, precision etc
- Whereas probabilities can be used wherever the evaluation metric is AUC, ROC_AUC, MSE, MAE, RMSE etc

<hr>

7. Is Logistic Regression Classification Based algorithm or Regression based algorithm? <br>
Ans: 
- It is a classification type algorithm.
- The name regression is there due to the similar underlying technique of Linear regression applied in it.
```
Note: We cannot use the evealuation metrics of classification based algorithms on Regression based algorithms.
```
> READ MORE [HERE](https://github.com/HridayAg0102/Summer-Analytics-2022/blob/main/Week_3/Various%20Evaluation%20Metrics/README.md) 
