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





