# L1 and L2 Regularization (Part 2 of Notes)

### READ FROM THESE LINKS. (Specially first one)
- <strong>Important (for Reading) [LINK](https://towardsdatascience.com/intuitions-on-l1-and-l2-regularisation-235f2db4c261)</strong>
- Article: [LINK](https://www.analyticssteps.com/blogs/l2-and-l1-regularization-machine-learning?fbclid=IwAR1pkL-RKR0xkKkdXtC1Tjcqm7CRX-FTD64U-nwNZYm_qnP2HEhhUdx0wW8)

A linear regression model that implements L1 norm for regularisation is called **lasso regression**, and one that implements (squared) L2 norm for regularisation is called **ridge regression**. To implement these two, note that the linear regression model stays the same,<br>
but it is the calculation of the loss function that includes these regularisation terms.

<br><br>
<p align="center"><img src="https://user-images.githubusercontent.com/76818035/172478609-91be4d82-6c28-4cfe-925f-9833de9b4fc5.png" height=550px></p>
