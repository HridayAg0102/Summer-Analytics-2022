### Logistic Regression Hypothesis function:

$$\huge h_\theta (x) = \frac{1}{1+e^{-(\theta^Tx)}}$$

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

  NOTE: The equation for gradient descent in Logistic regression looks IDENTICAL to that of linear regression !!! But there is a difference:
  
The <a href = "#logistic-regression-hypothesis-function"> HYPOTHESIS </a> of Gradient Descent of Logistic Regression is different from that of Liear regression Hypothesis (i.e., $\large h_\theta (x) = \theta_1 * x + \theta_0$)
