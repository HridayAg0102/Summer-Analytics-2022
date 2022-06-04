# Logistic Regression
<strong><a href = "https://www.youtube.com/watch?v=t1IT5hZfS48&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN&index=33">Reference Videos 6.1 to 6.7</a></strong>

<strong><a href = "https://towardsdatascience.com/introduction-to-logistic-regression-66248243c148">Reference Blog</a></strong>


<br>

## Contents:

<a href="#logistic-regression-hypothesis-function">Logistic Regression Hypothesis function </a>

<a href="#cost-in-logistic-regression-and-gradient-descent"> Cost in Logistic Regression and Gradient Descent </a>

<a href="#multiclass-classifier"> Multi-Class Classification </a>

<br><br>

### Logistic Regression Hypothesis function:

$$\Huge h_\theta (x) = \frac{1}{1+e^{-(\theta^Tx + \theta_0)}}$$
$$\huge \text{here, } \theta_0 \text{ is generally taken as 1}$$
As the prediction is a classification, the result can only be 0 or 1.

hence:

y = 1 :=> $\theta^Tx >= 0$

y = 0 :=> $\theta^Tx < 0$

### Example
![image](https://user-images.githubusercontent.com/76818035/172016831-7ce94fa5-724f-460d-ba5e-932ed5208676.png)

<hr>

<br><br>

### Cost in Logistic Regression and Gradient Descent
![image](https://user-images.githubusercontent.com/76818035/172019061-f061a4c9-8d3b-4f14-8707-c52678063963.png)

- NOTE: The equation for gradient descent in Logistic regression looks IDENTICAL to that of linear regression !!! But there is a difference:
  
- The <a href = "#logistic-regression-hypothesis-function"> HYPOTHESIS </a> of Gradient Descent of Logistic Regression is different from that of Liear regression Hypothesis (i.e., $\large h_\theta (x) = \theta_1 * x + \theta_0$, where $\large \theta_0$ is generally taken as `1`)

- This function is also known as <strong>Sigmoid Function</strong> or <strong> Logistic Function </strong>


<hr> <br><br>

### Multiclass Classifier

![image](https://user-images.githubusercontent.com/76818035/172022537-e061c7f6-352f-4bc6-b474-de504df1aba5.png)
![image](https://user-images.githubusercontent.com/76818035/172022721-39f65633-e741-4599-9929-ea0273c215e3.png)

This says, on testing a new input on all the three models we trained seperately, <br>
we'll choose the one, which gives the highest probability of `y = i`
