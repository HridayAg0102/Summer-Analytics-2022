Logistic Regression Blog:
-[Blog link](https://towardsdatascience.com/everything-you-need-to-know-about-linear-regression-b791e8f4bd7a)

Important Point Regarding Gradient Descent:
![image](https://user-images.githubusercontent.com/76818035/171456982-f6fc06d1-b970-42d9-8379-315058d27b35.png)

### What will happen in 1 step of Gradient Descent of one of the parameters of cost function is already at local minimum?
### Answer:
It will remain unchanged, since at local minima: Del (j) / Del (Theta 1) will be = 0;
hence, the assignment would be like 
		```Theta_1 := Theta_1 + Del (j) / Del (Theta 1)
		=> Theta_1 := Theta_1 + 0
		Hence, no change...```
		
