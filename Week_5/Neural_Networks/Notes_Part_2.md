# Notes Continued from [here](https://github.com/HridayAg0102/Summer-Analytics-2022/blob/main/Week_5/Neural_Networks/README.md)

## Backpropagation Intuition [video 9.3]

```py

First understand the intuition behind Forward Propagation 

```

![image](https://user-images.githubusercontent.com/76818035/176033991-f14e4d8d-fd58-4968-afab-58b089811a70.png)

## Correction:

- the notations $\Huge \Theta_{10}, \Theta_{11}, \Theta_{12}$  must be  $\Huge \Theta_{20}, \Theta_{21}, \Theta_{22}$

```py
NOTE

K => Number of output units
m => Number of training examples
```

![image](https://user-images.githubusercontent.com/76818035/176225995-e8cbc0ae-953e-405a-b82e-adef7bc3f872.png)

```
.


Here, there is only 1 OUTPUT UNIT so, K = 1 
Also, Regularization term is ignored, and only single training example is considered
Hence, m = 1

.
```
