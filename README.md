# ✅ PROJECT-04

This project develops a **predictive model** to evaluate **credit risk** in a **banking institution** by constructing a **classification model** that forecasts the probability of granting credit. The **target variable** is **CreditStatus**, and the model is trained on a dataset representing customers applying for a credit line. Ensuring high accuracy is vital, as extending credit to clients with low repayment capacity can lead to substantial financial losses. For comparative analysis, **Bayesian**, **Neural Network**, and **SVM** algorithms available in **Azure** are assessed.

In parallel, this solution was implemented using both **R** and **Microsoft Azure Machine Learning Studio**. **R** provides a robust environment for **statistical analysis** and **modeling**, while **Azure Machine Learning Studio** offers a **cloud-based** platform for building, deploying, and managing **machine learning** models. This dual approach underscores the project’s **versatility** and **adaptability**, leveraging different tools to meet diverse requirements and preferences.

Keywords: R Language, Microsoft Azure Machine Learning, Big Data, Data Analysis, S.M.O.T, Bayesian, Neural Network, S.V.M, Credit Analysis, Bank Account.

# ✅ PROCESS

**Azure Machine Learning** provides a **cloud-based** platform with **scalable computing** resources and **automated machine learning** capabilities for **model selection** and tuning. It simplifies the management of experiments, **tracking performance**, and **version control**, ensuring **reproducibility** and promoting **collaboration** among team members. With streamlined **model deployment**, **monitoring**, and comprehensive library support, it facilitates efficient development and integration of **machine learning** workflows. Additionally, **Azure Machine Learning** upholds **security** and **compliance** standards, while fostering **knowledge sharing** across teams. Overall, it is a robust platform for creating, deploying, and managing **machine learning** models in the **cloud**.

![image](https://github.com/lucashomuniz/PROJECT-6/assets/123151332/fecbf2d6-48d0-4f51-987f-9bf79add6886)

Initially, the **business problem** is defined, and the **German Credit UCI dataset** is selected. **Data preprocessing** involves converting **categorical variables**, applying **feature engineering** and **quantization** techniques, followed by **exploratory analysis** to understand the dataset’s characteristics. **Dataset balancing** is then performed using **SMOTE** (**Synthetic Minority Oversampling Technique**). The variable **CreditStatus** (the **target** for this **predictive model**) has a skewed distribution, with approximately **70%** labeled **Status 1 “Good”** and **30%** labeled **Status 2 “Bad”**. If left unbalanced, the model may become **biased**, learning substantially more about “Good Payers” than “Bad Payers.” By applying **SMOTE**, the class distribution is more balanced, reducing the likelihood of bias in the **predictive model** and improving its ability to identify both “Good” and “Bad” payers accurately.

![image](https://github.com/lucashomuniz/PROJECT-6/assets/123151332/d5b8f5f9-b2f1-46e1-9ac1-4367dfe73f0e)

Next, **variable selection** and **filter methods** are introduced in parallel using both **R** and **Azure Machine Learning**. Within **Azure**, two approaches—**Filter Based Feature Selection** and **Permutation Feature Importance**—were utilized. A third algorithm, developed in **R** with **Random Forest**, outperformed the Azure methods. Consequently, the **Random Forest** approach in **R** was adopted for subsequent stages of the project.

![1](https://github.com/user-attachments/assets/aa12c51f-25f4-475e-bf98-0ed62c2f1f76)

The **experiment** encompasses four **algorithms** (three in **Azure** and one in **R**). The **Azure Machine Learning** models include **Bayesian**, **Neural Network**, and **SVM**. Each **model** is trained, interpreted, and evaluated using **appropriate metrics** to compare performance. This comparison highlights the **most effective** algorithm for the **credit risk** prediction task.

![image](https://github.com/lucashomuniz/PROJECT-6/assets/123151332/5db634ce-bfa4-4b61-afe4-27ab7c565044)

Initially comparing the **Bayesian Algorithm** (blue line) with the **Neural Network Algorithm** (red line) using the **R.O.C Curve**, the **Bayesian Algorithm** demonstrates superior performance, achieving approximately **68% accuracy**. Next, comparing the **Neural Network Algorithm** (blue line) and the **SVM Algorithm** (red line), the **SVM Algorithm** performs better, reaching **64% accuracy**. Of the three **models**, the best result is obtained by the **Bayesian Algorithm**, while the **Neural Network Algorithm** shows the lowest performance.

![image](https://github.com/lucashomuniz/PROJECT-6/assets/123151332/2037ad27-5730-4ec8-8bcd-2e284ec8bb73)

Finally, an **R** script was developed to build a **machine learning** algorithm, enabling comparison with the models from **Azure Machine Learning**. Following **model training** and **testing**, an accuracy of approximately **77%** was achieved, surpassing the performance of the **Azure**-based algorithms.

# ✅ CONCLUSION

**Experimenting** with multiple **predictive models** simultaneously is a key advantage of using **Azure Machine Learning**. Replicating this process in **R** is more **labor-intensive**, making **Azure** particularly suitable for an initial **experimentation** phase to identify the **best algorithm**. Once the **machine learning** approach is chosen, transitioning to **R** allows for deeper **customization** and **optimization**, refining the final model.

API Key: oOeuSbiEVpCGy0cMWV8+9708W4sMfIFWJKbHjOcnUcjn/SAAeVcvOntroNfcGZRanmg+Wf7K/mVe+AMCoplevA==

# ✅ SOURCE

The **“German Credit Data”** dataset is employed to build and train the **model** in this experiment. Derived from **real data** by a researcher at the **University of Hamburg**, it comprises **1000 observations** and **20 variables** capturing **customer data**, such as **current account status**, **credit history**, **current credit amount**, **employability**, **residence**, and **age**.

Dataset: https://archive.ics.uci.edu/ml/datasets/Statlog+(German+Credit+Data)
