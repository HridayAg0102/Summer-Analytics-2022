# Bias Variance Tradeoff

<strong> Reference videos </strong>
- https://youtu.be/EuBBz3bI-aA
- https://www.youtube.com/watch?v=SjQyLhQIXSM
- https://medium.com/@itbodhi/bias-and-variance-trade-off-542b57ac7ff4

<hr>

- **Bias**: Inability of the ML method to capture the true relationship is called BIAS. `OR` Deviation from 0% error.<br>
- **Variance**: Difference between the Train set Error and Test set Error.
- **Overfitting / High Variance**: when the ML method curve `fits the Training Dataset well` but performs `bad` in `Test dataset`, this is called overfitting.
- **Underfitting / High Bias**: When the ML method curve performs bad even on the Train Dataset.

<p align="center"><img src = "https://user-images.githubusercontent.com/76818035/172215482-4c05bc68-da77-491a-aaa7-6f691d44373e.png" height=300px></p>

Our Target is to find a sweet spot between an underfitting model (SIMPLE MODEL) and an overfitting model (COMPLEX MODEL).

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172217783-66f9a00a-2fbb-4e8f-ab80-3caa8f1d5bee.png" height = 200px></p>

## Graphical Representation of Bias and Variance

<p align="center"> <img src="https://user-images.githubusercontent.com/76818035/172222234-c1b1d5df-e804-4d92-ab49-2f73d982d1e4.png" height=500px></p>

<strong>
High Model Complexity : High Variance , Low Bias <br>
Low Model Complexity : High Bias , Low Variance
</strong>
<br><br>

1. High Variance-High Bias — The model is inconsistent and also inaccurate on prediction
2. Low Variance-High Bias — Models is consistent but low on prediction
3. High Variance-Low Bias — Somewhat accurate but inconsistent on prediction
4. Low Variance-Low Bias — ideal scenario, the model is consistent and highly accurate on prediction

<p align = 'center'><img src="https://user-images.githubusercontent.com/76818035/172227616-ec51a6a1-eb6a-4d61-be4d-37f8b026bb73.png" height="250px"></p>

Generally, You can see a general trend in the examples above:

- **Linear machine learning algorithms** often have a high bias but a low variance. Example:Linear Regression, Logistic Regression <br>
- **Nonlinear machine learning algorithms** often have a low bias but a high variance. Example: Decision Tree, SVM, Neural Networks
