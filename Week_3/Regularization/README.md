# Regularization <br>
Reference Links:
- [Videos 7.1 to 7.4](https://youtu.be/u73PU6Qwl1I)


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

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172408291-cd0d6891-7a75-4427-abc4-3205742c9265.png" height=300></p>

<br>
In this formula, $\Large \lambda$ refers to `Regularization Parameter`
