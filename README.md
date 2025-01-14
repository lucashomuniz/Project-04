# ✅ PROJECT-20

This data analysis project aims to provide strategic answers to key business questions for a supermarket undergoing modernization. Using data recently captured by a new storage tool, the project seeks to transform this information into insights that guide investment decisions, resource optimization, and customer service improvement.

The choice of SQL and Power BI tools is central to ensuring the efficiency and clarity of the analytical process. SQL, widely recognized for its robustness and flexibility in handling large datasets, will be used to manipulate and organize the data. This approach not only structures the information logically and reliably but also ensures traceability and efficiency in executing complex operations. SQL's ability to integrate and consolidate data from different tables and correct inconsistencies is essential for building a solid foundation for subsequent analyses.

The project's focus is on addressing critical business questions, such as identifying the best product lines for investment, understanding customer behavior patterns, and optimizing human resources in operations. This question-driven approach ensures that data is used practically and purposefully, generating measurable value for the company. Furthermore, the integrated use of SQL and Power BI enhances process reliability and the quality of the insights, establishing an efficient and results-oriented workflow.

**Keywords**: SQL, PowerBI, PowerQuery, DAX, Google Cloud Platform, Business Analytics, BigQuery, Data Visualization, Data Analysis.

# ✅ PROCESS

In **Phase 1**, data transformations and manipulations are performed using SQL in the Google Cloud Platform (GCP) environment. The first step addresses the date column in the “Fato_Vendas” table, correcting inconsistencies caused by a system issue that recorded all dates as 2019. These dates will be updated to 2022 while preserving the original days and months. Next, a new column, “vlr_margem_bruta,” will be created, calculated based on “vlr_preco_total,” which combines unit price and tax. Before this, null values in the “vlr_preco_unitario” column will be corrected using the average price of the last 20 days, segmented by gender, product line, and branch. Once corrected, the gross margin calculation will be completed. Finally, a table will be generated to distribute a monthly investment of R$ 10,000 per branch, based on the number of products sold per product line and month. This table will include details on relative participation and the exact investment value.

**Phase 2** focuses on creating visualizations and analyses in Power BI, directly connecting to the GCP-treated tables. Initially, the most promising product line for investment in 2023 will be identified, considering variables such as monthly sales growth, consumer gender, and overall performance. Additionally, critical hours for allocating outsourced employees during peak times in branches will be evaluated using hourly sales patterns to pinpoint high-demand periods. Lastly, customer satisfaction by branch will be analyzed, identifying potential differences in service patterns and uncovering characteristics that may explain any issues.

# ✅ CONCLUSION

**Phase 1**: The datasets “fato_vendas,” “dim_produto,” and “dim_margem_bruta_perc” were uploaded to the Google Cloud Platform (GCP), enabling the entire data processing workflow to occur in BigQuery. This managed, high-performance environment streamlined the handling of large data volumes, simplified infrastructure maintenance, and facilitated future integrations, such as direct connections to Power BI. Data cleaning and standardization tasks — including date corrections, filling missing values, and calculating key indicators — created a reliable and traceable foundation for advanced analyses. BigQuery's distributed architecture ensured fast query processing, while the decision to centralize everything in GCP eliminated the need for manual pipelines, accelerating dashboard development and updates in Power BI for increased productivity.

**Phase 1A**: To enhance the organization and readability of database adjustments, Common Table Expressions (CTEs) were utilized. This strategy divided logic into modular, named steps, enabling the reuse of intermediate results without duplicating complex SQL segments. The primary focus was correcting sales dates and unit price values while creating a new gross margin column. In “STEP A,” incorrectly recorded dates from 2019 were adjusted to 2022 using the CTE “base_data,” which applied DATE_ADD to shift the year forward by three years.

**Phase 1B**: In “STEP B1,” null values in “vlr_preco_unitario” were corrected by calculating the average price from the last 20 days based on customer gender, product line, and branch, using the CTE “average_prices.” These results were applied in the CTE “corrected_prices” to fill missing values, though some remained due to insufficient historical data. In “STEP B2,” the “vlr_margem_bruta” column was created by combining tax values from the “dim_produtos” table with the gross margin percentage from “dim_margem_bruta_perct.” This process finalized adjustments to dates, prices, and margin calculations.

**Phase 1C**: The goal was to distribute a monthly investment of R$10,000 per branch based on the quantity of products sold by product line and month. The CTE “vendas_resumidas” calculated product quantities sold per branch, month, and product line, while “produtos_totais” determined total sales for each branch and month, enabling the calculation of relative participation in “participacao_produtos.” Finally, the CTE “investimentos_calculados” distributed investment values proportionally, and “final_table” joined with “dim_produtos” to display product names alongside the corresponding investment amounts.

**Phase 2**: A dashboard was developed in Power BI to clearly present the results extracted from BigQuery. Leveraging GCP's scalable architecture, most data transformations were performed at the source, reducing Power Query overhead. This streamlined model adjustments and enabled near-real-time updates. The dashboard was structured into tabs dedicated to each business question, allowing users to navigate segmented metrics and visuals for detailed exploration.

**Phase 2A**: A DAX measure, “m_faturamento,” was created to calculate revenue by multiplying sold quantities by unit prices (using SUMX). A parameter was implemented to let users select the primary metric (Revenue, Unit Price, or Product Quantity) for each visualization. Revenue analysis highlighted the growth of PRODUCT 6 among female customers, increasing from R$57,000 in January to R$152,000 in March. Similarly, PRODUCT 3 showed comparable growth for male customers, rising from R$42,000 to R$151,000 in the same period. These insights confirmed the strategic value of these products for maximizing financial returns within each gender segment.

![Screenshot 2025-01-14 at 17 00 38](https://github.com/user-attachments/assets/430a94a5-43c0-44c2-8e17-7ad73299ef76)

FASE 2B:

A calculated column named “periodo_venda” was created to group sales times into one-hour intervals. Using the same parameter logic, the primary metric can be filtered, and revenue analysis reveals that the 7:00 PM to 8:00 PM time slot generates R$342,170 across all branches, making it the peak period for Branch B and one of the highest for Branch A. In contrast, for Branch A, the 12:00 PM to 1:00 PM slot stands out, while for Branch C, the most profitable period is between 10:00 AM and 11:00 AM. Consequently, allocating outsourced staff between 7:00 PM and 8:00 PM addresses critical demand in most branches, with 12:00 PM to 1:00 PM and 10:00 AM to 11:00 AM also warranting attention.

![Screenshot 2025-01-14 at 17 00 55](https://github.com/user-attachments/assets/af232891-0007-4f24-b6d6-279e03cc0610)

FASE 2C:

This analysis examined variables such as “num_avaliacao,” “nom_filial,” and other characteristics to identify potential satisfaction issues. Overall, all branches exhibit relatively similar score distributions, with Branch C standing out positively for having the highest number of 10-rated evaluations and the lowest incidence of 2-rated scores. While differences exist, such as the predominance of "member" or "normal" clients and variations in the most evaluated products, no significant dissatisfaction was detected. Branch C demonstrates stronger engagement and evaluation results, presenting an opportunity to share its best practices with other units rather than focusing on isolated shortcomings.

![Screenshot 2025-01-14 at 17 01 05](https://github.com/user-attachments/assets/48530221-fbde-424c-ab9d-79e0939b022b)

