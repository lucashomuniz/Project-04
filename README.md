# ✅ PROJECT-06

In this project, we address the rising incidence of **liver disease**, driven by factors such as excessive **alcohol** consumption, exposure to **harmful gases**, ingestion of contaminated food, and the use of **drugs** and **anabolic steroids**. our primary objective is to develop a **machine learning** model that predicts whether a patient will develop **liver disease**, thus aiding **doctors**, **hospitals**, and **governments** in planning **health budgets** and implementing effective **prevention policies**. the desired outcome is a **classification** of “yes” or “no.”

to achieve this, we employ **supervised classification** techniques, creating multiple versions of the model using different **algorithms**. we present the **end-to-end** pipeline, encompassing model building, training, **evaluation**, and selection. throughout this project, we discuss which methods to apply, in what sequence, and with which tools. finally, we compare five distinct **algorithms** to determine the optimal approach for this **classification** task.

Keywords: Python Language, Data Analysis, Machine Learning, Classification Model, Supervised Learning, Logistic Regression, Random Forest, KNN, Decision Tree, SVM, Liver Diseases, Health Budget.

# ✅ PROCESS

Based on the **business problem** definition and **dataframe** analysis, it is often challenging to identify the ideal **algorithm** for a **machine learning** model. therefore, we adopt an **experimentation** approach, testing multiple **algorithms** with various **hyperparameters** to generate different model versions and compare their **performance**. similarly, the best **preprocessing** techniques are not always clear at the outset, so we also experiment to determine the most effective approach. indeed, the **data scientist** relies on systematic **experimentation** to select the best **algorithm**, technique, and overall strategy.

we begin with **exploratory analysis** immediately after loading the data. this involves **data cleaning** (removing **duplicates**, handling **missing values**) and applying specific transformations if needed. the focus is on understanding the **dataframe**, examining **numerical** and **categorical** variables, exploring their distributions, and identifying **outliers** via **boxplots**, descriptive tables, and **frequency counts**. ensuring there are no duplicate rows or columns is critical to prevent bias in the **model**. the goal is to achieve a **generalizable** solution.

![Screenshot 2025-03-06 at 20 41 31](https://github.com/user-attachments/assets/e6e074bf-3ca2-4eb1-b25a-fb4d6e8abcc6)

Next is **attribute engineering**, where deeper transformations may be performed, including creating or modifying variables. at this stage, **feature selection** can be employed to choose the most relevant variables for the **machine learning** process. additionally, constructing a **correlation table** helps uncover relationships (positive or negative) between variables and detect possible **multicollinearity**.

After that, we move on to **preprocessing**, converting any remaining text-based variables to numeric formats and finalizing the **machine learning** pipeline, which includes **label encoding**, **normalization**, **standardization**, and **data scaling**. a common practice is to split the **dataframe** into **training** and **testing** sets, ensuring the model learns from the **training** set and is evaluated on fresh **test** data. using the same data for both **training** and **testing** is inadvisable, as the model would already be familiar with it. thus, evaluating the model on new data—with known outcomes—provides an accurate measure of its **performance**.

![Figure_1](https://github.com/user-attachments/assets/169fc349-cfdf-4041-8d33-ec358f925b32)

# ✅ CONCLUSION

The analysis of the results reveals key insights into the performance of the regression models on the liver disease dataset. The correlation heatmap further highlights high correlations between features like Total_Bilirubin and Direct_Bilirubin (0.87), indicating potential multicollinearity, and weak correlations between the target and features, which explains the models' limited predictive power. The Random Forest model outperforms the others, achieving the lowest MAE (0.34041) and RMSE (0.41184), and the highest R² (0.17228), indicating it explains 17.23% of the target variance, followed closely by GBM with a slightly better MAE (0.33509) but lower R² (0.12654). KNN performs the worst, with the highest RMSE (0.44599) and lowest R² (0.02934), explaining only 2.93% of the variance. However, the overall low R² values (all below 0.18) and the clustering of predictions around 0.0 and 1.0 in the scatter plots suggest that regression is not ideal for this dataset, as the target variable is fundamentally binary (originally 1 and 2, converted to 1.0 and 0.0), making a classification approach more suitable. 

![Figure_3](https://github.com/user-attachments/assets/1d7600f2-386f-4835-9ad1-2d820d95da4f)

In conclusion, while Random Forest emerges as the best regression model due to its superior metrics across MAE, RMSE, and R², the overall poor performance of all models underscores the need for a different approach. Switching to a classification framework, addressing multicollinearity through feature selection or PCA, and tuning hyperparameters could significantly enhance results, better aligning with the dataset's binary nature and improving predictive accuracy.

![Figure_2](https://github.com/user-attachments/assets/78f41c6e-b5ac-45ae-8dbf-0917e8e90a78)

There are multiple **machine learning** algorithms applicable to various **problems**. below is an overview of **logistic regression**, **random forest**, **knn**, **decision tree**, and **svm**, outlining their main **advantages** and **disadvantages**.

**Logistic Regression**: a simple and fast algorithm especially suited for **binary classification**. it offers a probabilistic interpretation of predictions and evaluates the influence of each **variable**. however, it may struggle with **complex decision boundaries** and **imbalanced classes**.

**Random Forest**: an ensemble of **decision trees**, robust against **overfitting** and effective at handling **unbalanced data**. it also identifies the most **important variables**. while powerful, training a large number of trees can be **computationally expensive**, and results can be harder to interpret.

**KNN (k-nearest neighbors)**: a **non-parametric** approach that makes no assumptions about the data distribution. it can handle **complex decision boundaries** effectively. however, it may degrade with **high-dimensional** datasets and can be slow during prediction due to the neighbor search process.

**Decision Tree**: an intuitive algorithm that is easy to interpret and visualize, handling both **categorical** and **numeric variables** efficiently. it can be prone to **overfitting** and may require careful tuning to find an optimal **tree** structure.

**SVM (support vector machines)**: well-suited for **complex decision boundaries** and **high-dimensional** data, used in both **classification** and **regression** tasks. it is less susceptible to **overfitting**, but choosing the right **kernel** and **hyperparameters** can be challenging, and interpreting the **model** is often more difficult compared to other algorithms.

The choice of **algorithm** depends on the **context**, **data characteristics**, and **project objectives**. careful experimentation is recommended to assess **performance** before selecting a final approach. After evaluating the five **algorithms**, **random forest** achieved the best **performance** using the **auc score**. despite these results, there are additional **optimization** possibilities, such as incorporating more **relevant variables**, tuning different **hyperparameters**, extending **training time**, and revisiting **data preprocessing**. 

**Machine learning** is an iterative process, allowing repeated cycles of improvement from the initial **analysis** phase. Once the **best model** is chosen, it can be used to generate **predictions** for multiple **patients** simultaneously by loading their data from a **.csv** file. after **standardization**, the **results** can be saved in a new **spreadsheet** and provided to the **business** team for **decision-making** purposes.
