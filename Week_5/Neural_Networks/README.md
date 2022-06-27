# Neural Networks

### Reference Link:
- [Videos 8.1 to 9.8](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)



## Representation of Neural Networks  [Videos 8.1 to 8.4]<br><br>

![image](https://user-images.githubusercontent.com/76818035/175895433-3308fb0b-ae37-479d-8cdc-9bdca61682ba.png)

![image](https://user-images.githubusercontent.com/76818035/175895976-7cf50f4b-f2b7-4d84-89fd-c43f78d485d8.png)

![image](https://user-images.githubusercontent.com/76818035/175896691-281d5a64-b729-476c-be33-85b978e39a2b.png)

![image](https://user-images.githubusercontent.com/76818035/175969431-512e63d1-9600-42cc-aee4-1d675c6b18bf.png)

<br><br>

### NOTE: 
- Here $\Huge \mathbb{R}^n$ represents a `n-Dimensional` Vector
- We generally take  $\Huge a_0 $ to be = `1`

```py
This method is known as FORWARD PROPAGATION
```
<hr>

## Examples and Intuitions [videos 8.5 to 8.6] <br><br>

```
Video 8.5 : Implementation of Logic Functions (AND, OR, NOT)

Video 8.6 : Combining previously derived logic functions to create a Neural Network for XNOR
```
#### Value of the sigmoid function for different values on X-axis. <br><br>
![image](https://user-images.githubusercontent.com/76818035/175979514-cb7d2450-63cc-4b97-b37a-1247cceb51d2.png)


![image](https://user-images.githubusercontent.com/76818035/175979380-cf2324a8-8d6f-425d-a385-8e842874c1f1.png)

<br><br><hr>

## Multi-Class Classification [Video 8.7]

```py
The Multiclass Classification is just a n extension of One-Vs-All Classification.
```

![image](https://user-images.githubusercontent.com/76818035/175981966-9e56155b-fc1b-4317-a781-741459721ead.png)

![image](https://user-images.githubusercontent.com/76818035/175982236-c94010f8-5b17-4eef-8e88-75e3b7cec06b.png)

<br><br><hr>

## Cost Function in Neural Networks [Video 9.1]

![image](https://user-images.githubusercontent.com/76818035/175983816-8bd9584e-f125-4815-a068-a3867bb4bec4.png)

![image](https://user-images.githubusercontent.com/76818035/175986815-8ef99151-4714-4d37-bf2b-04ea750b6751.png)

```

We generally don't regularize bias terms, 

though, even if we regularize them, there is no significant difference in
the model's performance
```
<br><br><hr>

## :star: Backpropagation [Videos 9.2 and 9.3]

### - Gradient Computation

![image](https://user-images.githubusercontent.com/76818035/176029557-e479c239-b286-4299-956e-dbe7cf0a3bc3.png)

```
To minimize the cost function, we can use Gradient Decent and some other advanced techniques.

Gradient decent needs Cost function, and Derivative of Cost function as inputs.

Lecture 9.2 focusses more on computation of derivative part, since cost function is already known to us
```

![image](https://user-images.githubusercontent.com/76818035/176023718-269339c0-f187-49be-aab4-084416256f11.png)
![image](https://user-images.githubusercontent.com/76818035/176025500-a55bc72a-aee4-4f0e-9a48-958c65715948.png)
![image](https://user-images.githubusercontent.com/76818035/176029685-2b16fadd-8493-46ea-bd96-28af1caa16f6.png)

<br><br>
- $\Huge \triangle_{ij}$ are used to compute $\Huge \frac{\partial}{\partial \Theta^{(l)}_{ij}} \mathtt{J} \Theta$, <br>
  they are the cumulators which are going to slowly add things in order to compute $\Huge J(\Theta)$

- $\Huge \mathtt{D_{i,j}}$ represents the derivative : $\Huge \frac{\partial}{\partial \Theta^{(l)}_{ij}} \mathtt{J}(\Theta)$ , 
  (AS HIGHLIGHTED IN IMAGE ABOVE)$
  
- This part represents the vectorized format of computation: 
  <p align = 'center'> <img src = 'https://user-images.githubusercontent.com/76818035/176031687-bd8106a8-ac08-486f-bb26-181f9adacd46.png' height = 50px></p>
  
  Here `T` represents `Transpose` of the vector. (required for element wise multiplication [see matrix multiplication rules])
  
  
<br><br><hr><hr>

========================================================================================
# 🌟 [CONTINUED IN Notes_Part_2.md](https://github.com/HridayAg0102/Summer-Analytics-2022/blob/main/Week_5/Neural_Networks/Notes_Part_2.md)
========================================================================================



