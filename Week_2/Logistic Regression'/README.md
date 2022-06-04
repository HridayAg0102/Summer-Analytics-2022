Logistic Regression Hypothesis function:

$$ h_\theta (x) = \frac{1}{1+e^{-(\theta^Tx)}}$$

As the prediction is a classification, the result can only be 0 or 1.

hence:

	y = 1 :=> $\theta^Tx >= 0$
	y = 0 :=> $\theta^Tx < 0$