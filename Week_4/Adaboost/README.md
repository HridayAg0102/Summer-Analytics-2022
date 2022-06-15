# AdaBoosting

## REFERENCE VIDEO: [LINK](https://youtu.be/LsK-xG1cLYA)


## Comparison of Random Forests with AdaBoosting

|Random Forest |Adaboosting|
|--------------------------------------------|-------------------------------------------|
|In Random Forests where we create complete trees where there is `no maximum limit on depth` ofthe decision trees|in Adaboosting, we create trees with only `1 node and 2 leaf nodes`. **A tree with just 1 node and 2 leaf nodes is called a `STUMP`.**|
|![image](https://user-images.githubusercontent.com/76818035/173907758-a405dad8-a9e2-4976-9874-5d8e15a0b4cc.png)|![image](https://user-images.githubusercontent.com/76818035/173907627-b385560e-0395-4e8c-be6b-5fd1dd9470c6.png)|
|These are comparatively better learners since they take into consideration more number of features.|Weak learners due to consideration of only 1 feature per Stump. Hence these are generally used in combination.|
|All Trees have equal weightage to predict the result.|Some stumps may have more weightage than others, hence unequal weightage.|
|Each decision tree is made independently of each other, hence any tree can be made first.|In contrast, order of formation of Stumps matter here. The error in first stump affects the 2nd one, and that of 2nd affects the 3rd and so on...|

<br><hr> <br><br>

## Procedure to create stumps:
1. Assign sample weights to each entry in dataset. Note that these weights are different from any other weights present in the dataset.
2. Initially, all the weights assigned are same. All weights should add upto `1`
3. Create a stump from all the features present in the dataset and then calculate the `GINI INDEX` for all of them.
4. The stump with the `Lowest Gini Index` becomes our `First Stump`.
5. Now we need to determine the Amount of say this stump has in the final classification. For this we use the below mentioned formula <br> 
$$\Huge \boxed{\text{Amount of say} = \frac{1}{2}log(\frac{1 - \text{Total Error}}{\text{Total Error}})}$$
6. Since all weights add upto 1, the Total Error remains `between 0 and 1`.
7. The amount of say for a less erronious will be a relatively `large positive value`, while the erroniois one will have large `negative value`.
<p align = 'center'><img src = "https://user-images.githubusercontent.com/76818035/173914766-37e73a26-4c3e-4b8a-b3ba-60488635536b.png" height=450px></p> 

8. Now since the first stump did some incorrect classifications, we will `increase the weight` of the `incorrectly classified sample` and `decrease` all other weights. The formula for increment of weight is: <br><br>

<p align = 'center'><img src = "https://user-images.githubusercontent.com/76818035/173915744-335f280c-5c43-4608-8675-43b0c1d7a35d.png" height=50px></p> 

9. Now we need to decrease the sample weights of all other entries using the formula `notice the '-' sign on 'e'`: <br><br>

<p align = 'center'><img src = "https://user-images.githubusercontent.com/76818035/173916530-870b5044-c461-4ce9-97fc-aa4317dac092.png" height=50px></p>

10. Now `Normalize` all the `New Sample Weights` so they add upto `1`.
11. Now we generate a completely new dataset by doing the process explained in this clip:
(https://youtube.com/clip/Ugkx6MVx32XdmidRkWej1YpR_2BZr0IbbsyZ). `NOTE:` We can have `duplicate` entries in this new dataset, representing the greater weightage of that sample. We do this until we get a `new dataset of exactly same size as the original one`.
12. Now assign `equal weights` to all entries in the new dataset.

```
# Finally
==========

-> Repeat the above steps until all stumps are created. (using all the features)
-> Now seperate out the stumps which give different classifications for our prediction data in different groups.
-> Sum up the amounts of say in all the groups and consider the one with the HIGHEST AMOUNT OF SAY.
```
