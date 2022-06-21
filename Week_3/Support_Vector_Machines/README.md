# Support Vector Machines

```
NOTE for ipynb notebook
The limitation of SVC is compensated by SVM non-linearly. 
And that's the difference between SVM and SVC. 
If the hyperplane classifies the dataset linearly then the algorithm we call it as SVC 
and the algorithm that separates the dataset by non-linear approach then we call it as SVM.
```

<strong> Reference Links </strong>

- [Codebasics Video](https://www.youtube.com/watch?v=FB5EdxAGxQg)
- [Article](https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/)

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

## Inverse Regularization

**`INVERSE` Regularization parameter is also represented as `C` in scikit-learn** <br>
![image](https://user-images.githubusercontent.com/76818035/174887926-0fe6dc43-273e-47c2-b6f9-05fa29bdec2d.png)
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

```
The SVM kernel is a function that takes low dimensional input space and transforms it to a higher dimensional space i.e.
it converts not separable problem to separable problem.
```

## Pros and Cons of using SVMs


Pros:

- It works really well with a clear margin of separation
- It is effective in high dimensional spaces.
- It is effective in cases where the number of dimensions is greater than the number of samples.
- It uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Cons:

- It doesn’t perform well when we have large data set because the required training time is higher
- It also doesn’t perform very well, when the data set has more noise i.e. target classes are overlapping
- SVM doesn’t directly provide probability estimates, these are calculated using an expensive five-fold cross-validation. It is included in the related
SVC method of Python scikit-learn library.
