# ROC and AUC

Reference links:
1. Statquest Video : [LINK](https://www.youtube.com/watch?v=4jRBRDbJemM)
2. Blog : [LINK](https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/?fbclid=IwAR3NiyvLoVEQxRCerb5A3YVU8Qtuf9fpnG5ERWGLBQsfKbpvfuccI-7DI7U)

<br>
<hr>

**Receiver Operating Characterstics (ROC)** : This method provides us an easy way to summarize the performaces of classification models
at various threshold points. For Eg., we generally take a threshold of 0.5 for Logistic regression 
(=> x > 0.5 implies positive classification else negative.). But sometime, threshold of 0.8 or 0.1 can work better than the threshold of 0.5, 
and this is where ROC helps.

**Area Under the Curve (AUC):** It represents the area under the ROC curves of different options of methods to apply to get idea which one is better.
Greater the Area, the better is the model's functioning.

### LEARN MORE ABOUT THEM BY WATCHING THE ABOVE VIDEO AND READING THE BLOG

<div style = 'font-size:25px'>
Note that with Roc and Auc curve method, we use <b>predict_proba()</b> instea of <b>predict()</b>. Read more about these here: <a href="https://discuss.analyticsvidhya.com/t/what-is-the-difference-between-predict-and-predict-proba/67376">LINK</a>
</div>