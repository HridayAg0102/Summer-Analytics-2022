# Support Vector Machines

<strong> Reference Links </strong>

- [Codebasics Video](https://www.youtube.com/watch?v=FB5EdxAGxQg)
- 

<br>
<hr>

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172891764-b6f5befc-8b9e-4633-8da9-7af956437d6b.png" height=350></p>

In this image, both the lines act as classifiers, but the one with the higher distance to the nearest neighbouring points is a better classifier.

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172892133-68db77c1-0fbd-4a3a-98c4-9a006b85d021.png" height=350></p>

The boundaries between different dimensional model is different. That boundary is called `Hyperplane`

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172892600-125b2b50-b54d-46fc-88af-be7d7845aa0e.png" height=350></p>

The SVM draws the `Hyperplane` for `n Dimensional` model. 

<br>
<hr>

## Gamma

It refers to the consideration of number of datapoints in deciding the decision boundary.

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172893688-ab271501-3a7a-4a1e-a36c-eeb8aa783da4.png" height=300></p>

- **High Gamma:** It refers to the consideration of nearer points only for getting the decision boundary. This may lead to model `Overfitting`.
- **Low Gamma** It refers to the condideration of majority of the datapoints in deciding the decision boundary. This `avoids overfitting`

<br>
<hr>

## Regularization

**Regularization parameter is also represented as `C` in scikit-learn**
<strong> Read from [Regularization Notes](../Regularization) </strong>
  
<br>
<hr>
  
## Sample Approach
  
|The original Model| Converted Model|
|------------------|----------------|
|![image](https://user-images.githubusercontent.com/76818035/172895578-dc4b70e4-dbd5-4a3d-97ff-1eb7184c0f1a.png)|![image](https://user-images.githubusercontent.com/76818035/172895733-97fabf8e-91be-4189-9811-bc78e47fadb9.png)|
|This model is the original model| This model is created by adding a 3rd parameter `z`. It can be visualised as a vertical paraboloid shape. Yellow line is the decision boundary.|

<br><br>

- The `z` here is called the `Transformation Kernel`
- The top view of the seperation boundary will look something like this:

<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172897366-e434c319-f661-485a-b1de-d2be3a55f13d.png" height=500></p>

