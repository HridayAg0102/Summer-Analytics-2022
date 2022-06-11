# ROC and AUC

<details open>
<summary>Reference links:</summary>

1. Statquest Video : [LINK](https://www.youtube.com/watch?v=4jRBRDbJemM)
2. Blog : [LINK](https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/?fbclid=IwAR3NiyvLoVEQxRCerb5A3YVU8Qtuf9fpnG5ERWGLBQsfKbpvfuccI-7DI7U)
  
</details>

<hr>

**Receiver Operating Characterstics (ROC)** : This method provides us an easy way to summarize the performaces of classification models
at various threshold points. For Eg., we generally take a threshold of 0.5 for Logistic regression 
(=> x > 0.5 implies positive classification else negative.). But sometime, threshold of 0.8 or 0.1 can work better than the threshold of 0.5, 
and this is where ROC helps.

```
ROC curve is plotted between True Positive Rate (TPR or Sensitivity) and False Positive Rate (FPR or {1 - specificity}) 
but often, replacing Precision with FPR gives better results.
```

### :star: The Model has been implemented in .ipynb file in this folder

| ROC Curve for Binary Classification | ROC Curve for MultiClass Classification |
| ------------------------------------| --------------------------------------- |
| <img src = ./ROC.png>               | <img src="./Multiclass ROC.png">

<br>
<hr>


**Area Under the Curve (AUC):** It represents the area under the ROC curves of different options of classification methods to apply to get idea which one is better.
Greater the Area, the better is the model's functioning.
