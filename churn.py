import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
churn_data = pd.read_csv(r"C:\Users\Ilyas\OneDrive\Bureau\data analysis projects\Telco Customer Churn\WA_Fn-UseC_-Telco-Customer-Churn.csv")
#Converting TotalCharges column to numeric values so that we can perform calculations on it 
churn_data['TotalCharges'] = pd.to_numeric(churn_data['TotalCharges'], errors= 'coerce')
churn_data_with_phone_service = churn_data.loc[churn_data['PhoneService'] == 'Yes']
churn_data_with_internet_service = churn_data.loc[churn_data['InternetService'] != 'No']
#Calculating important metrics
total_churn_retention_rate = (churn_data['Churn'] == 'Yes').sum() / churn_data['Churn'].count() 
total_money_lost = churn_data['TotalCharges'].where(churn_data['Churn'] == 'Yes').sum()
churn_retention_rate_tenure_less_than_a_year = ((churn_data['tenure'] < 12) & (churn_data['Churn'] == 'Yes')).sum() /(churn_data['tenure'] < 12).sum()
churn_retention_rate_tenure_between_a_year_and_three = ((churn_data['tenure'] > 12) & (churn_data['Churn'] == 'Yes') & (churn_data['tenure'] < 36)).sum() /((churn_data['tenure'] > 12) & (churn_data['tenure'] < 36)).sum()
churn_retention_rate_tenure_more_than_3_years = ((churn_data['tenure'] > 36) & (churn_data['Churn'] == 'Yes')).sum() /(churn_data['tenure'] > 36).sum()
churn_retention_rate_of_senior_citizens = ((churn_data['SeniorCitizen'] == 1) & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['SeniorCitizen'] == 1).sum()
churn_retention_rate_of_non_senior_citizens = ((churn_data['SeniorCitizen'] == 0) & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['SeniorCitizen'] == 0).sum()
churn_retention_rate_of_citizens_with_dependents = ((churn_data['Dependents'] == 'Yes') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['Dependents'] == 'Yes').sum()
churn_retention_rate_of_citizens_with_no_dependents = ((churn_data['Dependents'] == 'No') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['Dependents'] == 'No').sum()
churn_retention_rate_with_phone_service = ((churn_data['PhoneService'] == 'Yes') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['PhoneService'] == 'Yes').sum()
churn_retention_rate_with_phone_service_multiple_lines = ((churn_data_with_phone_service['MultipleLines'] == 'Yes') & (churn_data_with_phone_service['Churn'] == 'Yes')).sum() / (churn_data_with_phone_service['MultipleLines'] == 'Yes').sum()
churn_retention_rate_with_phone_service_no_multiple_lines = ((churn_data_with_phone_service['MultipleLines'] == 'No') & (churn_data_with_phone_service['Churn'] == 'Yes')).sum() / (churn_data_with_phone_service['MultipleLines'] == 'No').sum()
churn_retention_rate_with_DSL_internet_service = ((churn_data['InternetService'] == 'DSL') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['InternetService'] == 'DSL').sum()
churn_retention_rate_with_fiber_optic_internet_service = ((churn_data['InternetService'] == 'Fiber optic') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['InternetService'] == 'Fiber optic').sum()
churn_retention_rate_with_no_internet_service = ((churn_data['InternetService'] == 'No') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['InternetService'] == 'No').sum()
churn_retention_rate_internet_service_with_online_security = ((churn_data_with_internet_service['OnlineSecurity'] == 'Yes') & (churn_data_with_internet_service['Churn'] == 'Yes')).sum() / (churn_data_with_internet_service['OnlineSecurity'] == 'Yes').sum()
churn_retention_rate_internet_service_with_online_backup = ((churn_data_with_internet_service['OnlineBackup'] == 'Yes') & (churn_data_with_internet_service['Churn'] == 'Yes')).sum() / (churn_data_with_internet_service['OnlineBackup'] == 'Yes').sum()
churn_retention_rate_internet_service_with_device_protection = ((churn_data_with_internet_service['DeviceProtection'] == 'Yes') & (churn_data_with_internet_service['Churn'] == 'Yes')).sum() / (churn_data_with_internet_service['DeviceProtection'] == 'Yes').sum()
churn_retention_rate_internet_service_with_tech_support = ((churn_data_with_internet_service['TechSupport'] == 'Yes') & (churn_data_with_internet_service['Churn'] == 'Yes')).sum() / (churn_data_with_internet_service['TechSupport'] == 'Yes').sum()
churn_retention_rate_internet_service_with_streaming_tv = ((churn_data_with_internet_service['StreamingTV'] == 'Yes') & (churn_data_with_internet_service['Churn'] == 'Yes')).sum() / (churn_data_with_internet_service['StreamingTV'] == 'Yes').sum()
churn_retention_rate_internet_service_with_streaming_movies = ((churn_data_with_internet_service['StreamingMovies'] == 'Yes') & (churn_data_with_internet_service['Churn'] == 'Yes')).sum() / (churn_data_with_internet_service['StreamingMovies'] == 'Yes').sum()
churn_retention_rate_with_paperless_billing = ((churn_data['PaperlessBilling'] == 'Yes') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['PaperlessBilling'] == 'Yes').sum()
churn_retention_rate_with_no_paperless_billing = ((churn_data['PaperlessBilling'] == 'No') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['PaperlessBilling'] == 'No').sum()
churn_retention_rate_payment_method_electronic_check = ((churn_data['PaymentMethod'] == 'Electronic check') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['PaymentMethod'] == 'Electronic check').sum()
churn_retention_rate_payment_method_mailed_check = ((churn_data['PaymentMethod'] == 'Mailed check') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['PaymentMethod'] == 'Mailed check').sum()
churn_retention_rate_payment_method_bank_transfer = ((churn_data['PaymentMethod'] == 'Bank transfer (automatic)') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['PaymentMethod'] == 'Bank transfer (automatic)').sum()
churn_retention_rate_payment_method_credit_card = ((churn_data['PaymentMethod'] == 'Credit card (automatic)') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['PaymentMethod'] == 'Credit card (automatic)').sum()
churn_retention_rate_contract_month_to_month = ((churn_data['Contract'] == 'Month-to-month') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['Contract'] == 'Month-to-month').sum()
churn_retention_rate_contract_one_year = ((churn_data['Contract'] == 'One year') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['Contract'] == 'One year').sum()
churn_retention_rate_contract_two_year = ((churn_data['Contract'] == 'Two year') & (churn_data['Churn'] == 'Yes')).sum() / (churn_data['Contract'] == 'Two year').sum()
#Metrics dictionary for easier data manipulation
# Collect all metrics into a dictionary
metrics_dict = {
    'Overall Churn Rate': total_churn_retention_rate,
    'Total Money Lost ($)': total_money_lost,
    
    # Tenure groups
    'Churn Rate: tenure < 1 year': churn_retention_rate_tenure_less_than_a_year,
    'Churn Rate: tenure 1-3 years': churn_retention_rate_tenure_between_a_year_and_three,
    'Churn Rate: tenure > 3 years': churn_retention_rate_tenure_more_than_3_years,
    
    # Demographics
    'Churn Rate: demographics Senior Citizens': churn_retention_rate_of_senior_citizens,
    'Churn Rate: demographics Non-Senior Citizens': churn_retention_rate_of_non_senior_citizens,
    'Churn Rate: demographics Has Dependents': churn_retention_rate_of_citizens_with_dependents,
    'Churn Rate: demographics No Dependents': churn_retention_rate_of_citizens_with_no_dependents,
    
    # Phone service
    'Churn Rate: Has Phone Service': churn_retention_rate_with_phone_service,
    'Churn Rate: Multiple Lines': churn_retention_rate_with_phone_service_multiple_lines,
    'Churn Rate: No Multiple Lines': churn_retention_rate_with_phone_service_no_multiple_lines,
    
    # Internet service type
    'Churn Rate: DSL Internet': churn_retention_rate_with_DSL_internet_service,
    'Churn Rate: Fiber Optic Internet': churn_retention_rate_with_fiber_optic_internet_service,
    'Churn Rate: No Internet': churn_retention_rate_with_no_internet_service,
    
    # Internet add-ons (among those with internet)
    'Churn Rate: adds Has Online Security': churn_retention_rate_internet_service_with_online_security,
    'Churn Rate: adds Has Online Backup': churn_retention_rate_internet_service_with_online_backup,
    'Churn Rate: adds Has Device Protection': churn_retention_rate_internet_service_with_device_protection,
    'Churn Rate: adds Has Tech Support': churn_retention_rate_internet_service_with_tech_support,
    'Churn Rate: adds Has Streaming TV': churn_retention_rate_internet_service_with_streaming_tv,
    'Churn Rate: adds Has Streaming Movies': churn_retention_rate_internet_service_with_streaming_movies,
    
    # Billing
    'Churn Rate: Paperless Billing': churn_retention_rate_with_paperless_billing,
    'Churn Rate: No Paperless Billing': churn_retention_rate_with_no_paperless_billing,
    
    # Payment method
    'Churn Rate: Payment - Electronic Check': churn_retention_rate_payment_method_electronic_check,
    'Churn Rate: Payment - Mailed Check': churn_retention_rate_payment_method_mailed_check,
    'Churn Rate: Payment - Bank Transfer': churn_retention_rate_payment_method_bank_transfer,
    'Churn Rate: Payment - Credit Card': churn_retention_rate_payment_method_credit_card,

    # Contract type
    'Churn Rate: Contract Month-to-Month': churn_retention_rate_contract_month_to_month,
    'Churn Rate: Contract One Year': churn_retention_rate_contract_one_year,
    'Churn Rate: Contract Two Year': churn_retention_rate_contract_two_year,
}
#analysis and data visualization
metrics_series = pd.Series(metrics_dict)
tenure_group_rates = metrics_series[metrics_series.index.str.contains('tenure')]
contract_rates = metrics_series[metrics_series.index.str.contains('Contract')]
internet_service_rates = metrics_series[metrics_series.index.str.contains('Internet')]
billing_rates = metrics_series[metrics_series.index.str.contains('Billing')]
payment_method_rates = metrics_series[metrics_series.index.str.contains('Payment')]
demographics_rates = metrics_series[metrics_series.index.str.contains('demographics')]
adds_on_rates = metrics_series[metrics_series.index.str.contains('adds')]


print(metrics_series.apply(lambda x: f"{x:.1%}" if x < 1 else f"${x:,.0f}"))
#Bar chart of churn rate by contract type
bar_chart_contract_type = sns.barplot(x=['Month-to-month', 'One year', 'Two year'],
                                    y=contract_rates.values )
bar_chart_contract_type.yaxis.set_major_formatter(PercentFormatter(xmax=1))
bar_chart_contract_type.set_title('Bar chart of churn rate by contract type')
bar_chart_contract_type.set_xlabel('Contract Type Period')
bar_chart_contract_type.set_ylabel('Churn Rate(%)')
plt.tight_layout()
plt.show()
#Bar chart of churn rate by Internet service type
bar_chart_internet_type = sns.barplot(x = ['DSL','Fiber Optic','No Internet'], y = internet_service_rates.values)
bar_chart_internet_type.yaxis.set_major_formatter(PercentFormatter(xmax=1))
bar_chart_internet_type.set_xlabel('Internet Service Type')
bar_chart_internet_type.set_ylabel('Churn Rate(%)')
bar_chart_internet_type.set_title('Bar chart of churn rate by Internet service type')
plt.tight_layout()
plt.show()
#Bar chart of churn rate by tenure group 
bar_chart_tenure_type = sns.barplot(x = ['tenure < 1 year','tenure 1-3 years','tenure > 3 years'], y = tenure_group_rates.values)
bar_chart_tenure_type.yaxis.set_major_formatter(PercentFormatter(xmax=1))
bar_chart_tenure_type.set_xlabel('Tenure groups')
bar_chart_tenure_type.set_ylabel('Churn Rate(%)')
bar_chart_tenure_type.set_title('Bar chart of churn rate by tenure group')
plt.tight_layout()
plt.show()
#Bar chart of churn rate by billing type
bar_chart_billing_type = sns.barplot(x = ['Paperless Billing','No Paperless Billing'], y = billing_rates.values)
bar_chart_billing_type.yaxis.set_major_formatter(PercentFormatter(xmax=1))
bar_chart_billing_type.set_xlabel('Billing Type')
bar_chart_billing_type.set_ylabel('Churn Rate(%)')
bar_chart_billing_type.set_title('Bar chart of churn rate by billing type')
plt.tight_layout()
plt.show()
#Bar chart of churn rate by payment method
bar_chart_payment_method = sns.barplot(x = ['Electronic Check','Mailed Check','Bank Transfer','Credit Card'], y = payment_method_rates.values)
bar_chart_payment_method.yaxis.set_major_formatter(PercentFormatter(xmax=1))
bar_chart_payment_method.set_xlabel('Payment Method')
bar_chart_payment_method.set_ylabel('Churn Rate(%)')
bar_chart_payment_method.set_title('Bar chart of churn rate by payment method')
plt.tight_layout()
plt.show()
#Bar chart of churn rate by demographics_rates
bar_chart_demographics_group = sns.barplot(x = ['Senior Citizens','Non-Senior Citizens','Has Dependents','No Dependents'], y = demographics_rates.values)
bar_chart_demographics_group.yaxis.set_major_formatter(PercentFormatter(xmax=1))
bar_chart_demographics_group.set_xlabel('Demographics Type')
bar_chart_demographics_group.set_ylabel('Churn Rate(%)')
bar_chart_demographics_group.set_title('Bar chart of churn rate by demographics')
plt.tight_layout()
plt.show()
#Bar chart of adds on 
bar_chart_adds_on = sns.barplot(y = ['Online Security','Online Backup','Device Protection','Tech Support','Streaming TV','Streaming Movies'], x= adds_on_rates.values)
bar_chart_adds_on.xaxis.set_major_formatter(PercentFormatter(xmax=1))
bar_chart_adds_on.set_xlabel('Churn Rate(%)')
bar_chart_adds_on.set_ylabel('Adds On Type')
bar_chart_adds_on.set_title('Bar chart of churn rate by Adds On')
plt.tight_layout()
plt.show()
