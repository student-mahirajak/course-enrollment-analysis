import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('enrollment_data.csv')
print(df)


course_enrollments = df.groupby('Course')['Enrollments'].sum()
print("\nCourse-wise Enrollments:\n", course_enrollments)


city_enrollments = df.groupby('City')['Enrollments'].sum()
print("\nCity-wise Enrollments:\n", city_enrollments)

course_enrollments.plot(kind='bar', title='Enrollments by Course', color='skyblue')
plt.xlabel('Course')
plt.ylabel('Total Enrollments')
plt.grid(True)
plt.show()

city_enrollments.plot(kind='pie', title='Enrollments by City', autopct='%1.1f%%')
plt.ylabel('')
plt.show()

