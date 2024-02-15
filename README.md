# Project-1
a shared repo for project 1 for CU-VIRT-DATA
Project 1: An Analysis of Maternal Health Outcomes in America
by Group 7: Mia Metni, Khadija Collymore and Christopher Wiggs
1. Research Question
Are maternal mortality rates of women in America highest among black women (as opposed to women with other racial backgrounds)?
2. Hypothesis
The elevated maternal mortality rates among black women in the United States compared to other racial groups stem from a complex interplay of factors:
healthcare disparities,
socio-economic factors,
systemic biases,
limited access to quality healthcare,
economic inequality,
racial biases within healthcare systems
Conclusion: Our linear regression model demonstrates that there exists a positive linear relationship having a very strong correlation between the two variables (rate of incidence and time). Thus, we can assert with confidence that, in accordance with the data over the past half decade, the rate of incidence of maternal mortality is increasing over time. Correlation coefficient (r): 0.9876323129145643. We accept the alternate hypothesis. There is a strong relationship between the rate of incidence of maternal mortality or morbidity and race. Black women in the united states (u.s.) disproportionately experience adverse pregnancy outcomes, including maternal mortality, compared to women of other racial and ethnic groups
Given our analysis, we can conclude that…
BLACK WOMEN ARE MORE SUSCEPTIBLE TO EXPERIENCING NEGATIVE HEALTH OUTCOMES RELATED TO PREGNANCY AND/OR OBSTETRIC CARE than any other racial and ethnic group
THIS INCREASED SUSCEPTIBILITY IS OBSERVED TO BE, IN PART, DUE TO THE IMPACT OF IMPLICIT BIAS, GENETIC SUSCEPTIBILITY, AND SDOH ON THE RATE OF INCIDENCE OF MATERNAL MORTALITY AND MORBIDITY
WHILE NOT ALL FACTORS OF INFLUENCE COULD BE IDENTIFIED AS CAUSAL FACTORS, THE identification and evaluation of factors contributing to racial disparities is crucial to informing and implementing prevention strategies that will effectively reduce disparities in pregnancy-related mortality, including strategies to improve women's health and access to quality care in all maternal phases: preconception, pregnancy, and postpartum.
Methodology: Crawled the web key words: maternal health, maternal mortality, live births, race, urban v. rural health outcome, Downloaded csvs from CDC and created dataframes from the associated data , Filtered rows where race demographic is ‘black/african american’, Removed extraneous rows like "Mother's Single Race Code", "Notes", "Mother's Education Code", etc.,Renamed column names when appropriate, Replace NaN values with 0, Leveraged matplotlib to create visualizations.
