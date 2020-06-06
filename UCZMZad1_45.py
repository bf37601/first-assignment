import pandas as pd
import matplotlib.pyplot as plt

df_schema = pd.read_csv('survey_results_schema.csv')
df_public = pd.read_csv('survey_results_public.csv',
                        usecols=['Respondent', 'YearsCodePro', 'WorkWeekHrs', 'Gender'],
                        index_col='Respondent')

df_public.dropna(inplace=True)

# replace string values
df_public.replace(to_replace='Less than 1 year', value='0', inplace=True)
df_public.replace(to_replace='More than 50 years', value='50', inplace=True)

# delete unreal week hours (grater than 24 * 7)
df_public = df_public[df_public['WorkWeekHrs'] <= 168]

# df_public['YearsCodePro'] = pd.to_numeric(df_public['YearsCodePro'],errors='coerce')
df_public['YearsCodePro'] = df_public['YearsCodePro'].astype(float)

df_public_man = df_public[df_public['Gender'] == 'Man']
df_public_woman = df_public[df_public['Gender'] == 'Woman']
df_public_other = df_public[(df_public['Gender'] != 'Man') & df_public['Gender'] != 'Woman']

plt.plot(df_public['YearsCodePro'], df_public['WorkWeekHrs'], 'ro', markersize=0.3)
plt.xlabel('YearsCodePro')
plt.ylabel('WorkWeekHrs')
plt.title('All')
plt.show()

plt.plot(df_public_man['YearsCodePro'], df_public_man['WorkWeekHrs'], 'ro', markersize=0.3)
plt.xlabel('YearsCodePro')
plt.ylabel('WorkWeekHrs')
plt.title('Men')
plt.show()

plt.plot(df_public_woman['YearsCodePro'], df_public_woman['WorkWeekHrs'], 'ro', markersize=0.3)
plt.xlabel('YearsCodePro')
plt.ylabel('WorkWeekHrs')
plt.title('Women')
plt.show()

plt.plot(df_public_other['YearsCodePro'], df_public_other['WorkWeekHrs'], 'ro', markersize=0.3)
plt.xlabel('YearsCodePro')
plt.ylabel('WorkWeekHrs')
plt.title('Other')
plt.show()
