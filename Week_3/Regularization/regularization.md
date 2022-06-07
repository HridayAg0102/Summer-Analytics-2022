# Regularization <br>
Reference Links:
- [Videos 7.1 to 7.4](https://youtu.be/u73PU6Qwl1I)

<hr>

### Ways to Address Overfitting:
1. Reduce Number of Features.
  - Manually select which features to keep.
  - `Model Selection` algorithms.
  
2. Regularization
  - Keep all the features, but reduce magnitude/values of parameters $\large \theta_j$
  - Works well if we have lots of features, each of which contributes a bit in predicting `y` (output)

## Regularization 
In regularization, we try to penalize the parameters within the cost function with some high values so that when we <br>
miniize the value of <strong>J($\theta$)</strong>, we get the effect of those parameters reduced.

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172408291-cd0d6891-7a75-4427-abc4-3205742c9265.png" height=100></p>

<br>

In this formula, $\Huge \lambda$ refers to `Regularization Parameter`.

### What Happens when we choose Extremely High value of Lambda ?

<p align="center"><img src = "https://user-images.githubusercontent.com/76818035/172409978-df3cb791-a81c-4f70-8a7e-9a179e2de71d.png" height=300></p>

Thus, for very large value of $\Large \lambda$, we almost neglect the effect of panalized parameters which may <br>
lead to Underfitting Model predictions.
<hr>

<strong> 👉 We Don't panalize $\Huge \theta_0$ by convention. Though, even if it is panalized, it puts negligibly small effect on the trained model </strong>

<hr>
<br><br>

## ▶️ Regularization in Linear Regression

### 1. In Gradient Descent

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172419509-986bcc7e-2380-4ec6-b6f9-9704e32f6b18.png" height=230></p>

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172422684-9e8903a1-989e-4e1a-abec-4951f8e49ccc.png" height=60></p>
<br><br>

<p align="center">The Term $\Huge \left( 1-\alpha\frac{\lambda}{m} \right)$ < 1 </p>

    
### 2. In Normal Equation Method
<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172427720-2b693a83-8673-4d97-a374-b516572193f0.png" height=200></p>
<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172429226-f8bfd48f-9205-4faa-9b00-9bd6a213d683.png" height=400></p>

<br><br>

### :star: Problem of Non Invertibility in Normal Equation Method (Doesn't occur while using Regularization)
<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172431435-b1651c9c-432f-447c-b877-673025fcbf0f.png" height=400></p>

<hr>

<br><br>

## ▶️ Regularization in Logistic Regression

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172439449-53c06f77-f2bd-4dc8-940e-2614ef9e6ea5.png" height=400></p>
<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172443253-5dfcdd30-43c9-43f7-bdac-033814cbb14f.png" height=400></p>

### Examples of Regularization:
- K-means: Restricting the segments for avoiding redundant groups.
- Neural networks: Confining the complexity (weights) of a model.
- Random Forest: Reducing the depth of tree and branches (new features)

<hr>

#  ⏭️ [L1 and L2 Regularization](./L1_and_L2_regularization.md) {Part 2 of these notes. are present at this link.}

