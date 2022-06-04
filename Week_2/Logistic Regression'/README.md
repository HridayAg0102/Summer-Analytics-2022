Logistic Regression Hypothesis function:

$$ h_\theta (x) = \frac{1}{1+e^{-(\theta^Tx)}}$$

As the prediction is a classification, the result can only be 0 or 1.

hence:

y = 1 :=> $\theta^Tx >= 0$

y = 0 :=> $\theta^Tx < 0$

### Example
![image](https://user-images.githubusercontent.com/76818035/172016831-7ce94fa5-724f-460d-ba5e-932ed5208676.png)

<hr>

<br><br>

### Cost in Logistic Regression
$$Cost(h_\theta x, y) = -y*log(h_\theta (x)) - (1-y)*log(1 - h_\theta (x))$$
