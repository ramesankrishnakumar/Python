import pandas as pd

# Read the two CSV files into two separate dataframes
e2e_df_leads = pd.read_csv('~/Downloads/e2e-leads.csv')
prod_df_leads = pd.read_csv('~/Downloads/prd-leads.csv')

# Merge the two dataframes on the 'intuitUserId' column and only include the 'intuitUserId' column
merged_df = pd.merge(e2e_df_leads['intuitUserId'], prod_df_leads['intuitUserId'], on='intuitUserId', how='outer')

# Get the unique set of 'intuitUserId'
leads_unique_ids_count = len(set(merged_df['intuitUserId'].tolist()))


e2e_df_static_insights = pd.read_csv('~/Downloads/e2e-static-insights.csv')
prod_df_static_insights = pd.read_csv('~/Downloads/prd-static-insights.csv')

merged_df = pd.merge(e2e_df_static_insights['intuitUserId'], prod_df_static_insights['intuitUserId'], on='intuitUserId', how='outer')

static_insights_unique_ids_count = len(set(merged_df['intuitUserId'].tolist()))


e2e_df_customer_insights = pd.read_csv('~/Downloads/e2e-customer-insights.csv')
prod_df_customer_insights = pd.read_csv('~/Downloads/prd-customer-insights.csv')

merged_df = pd.merge(e2e_df_customer_insights['intuitUserId'], prod_df_customer_insights['intuitUserId'], on='intuitUserId', how='outer')

customer_insights_unique_ids_count = len(set(merged_df['intuitUserId'].tolist()))


print(f"unique_lead_users_count: {leads_unique_ids_count}, unique_static_insights_users_count: {static_insights_unique_ids_count} unique_customer_insights_users_count: {customer_insights_unique_ids_count}")
