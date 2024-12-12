# 1. File description
# Project: Demographics and Suicide Rates 
# Author: Musammat Aktar
# Interactive data analysis program for Suicide Rates over years, among age groups, gender,and races.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('data/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv')

# Introduction message
print('Hi there! \nWelcome to this program. \nHere you can investigate suicide rates per 100,000 people over years, gender (coming soon :)), race (coming soon :)), and age.')

# Intro function
def Intro():
    global data  # Ensures that `data` is recognized as a global variable
    while True:  # Loops to keep the program running until the user exits
        print('''\nWhat would you like to know about suicide deaths over the years?
1. Analyze entire dataset
2. Focus on a specific feature
3. Generate visualizations
4. Exit program
''')
        userInput = input('I would like to: ')

        # Analyze entire dataset
        if userInput == 'Analyze entire dataset' or userInput == '1':
            print("\n=== Dataset Statistics Summary ===")
            print(data.describe())  # Displays dataset statistics

        # Focus on a specific feature
        elif userInput == 'Focus on a specific feature' or userInput == '2':
            print("What specific features would you like to focus on? \n1. Female count \n2. Male count \n3. Average age")
            userInputTwo = input('I would like to see the: ')

            if userInputTwo == 'female count' or userInputTwo == '1':
                female_count = data[data['STUB_LABEL'].str.strip().str.lower() == 'female'].shape[0]
                print(f'Total females in the study: {female_count}')

            elif userInputTwo == 'male count' or userInputTwo == '2':
                male_count = data[data['STUB_LABEL'].str.strip().str.lower() == 'male'].shape[0]
                print(f'Total males in the study: {male_count}')

            elif userInputTwo == 'average age' or userInputTwo == '3':
                if 'AGE' in data.columns:
                    # Convert 'AGE' column to numeric, setting errors='coerce' to turn non-numeric values into NaN
                    data['AGE'] = pd.to_numeric(data['AGE'], errors='coerce')
                    
                    # Drop rows where 'AGE' is NaN
                    numeric_ages = data.dropna(subset=['AGE'])
                    
                    if numeric_ages.empty:
                        print("No numeric age data available in the dataset.")
                    else:
                        avg_age = numeric_ages['AGE'].mean()
                        print(f'Average age in the study: {avg_age}')
                else:
                    print("Error: 'AGE' column is missing from the dataset.")
            else:
                print("Invalid input. Please try again.")

        # Generate visualizations
        elif userInput == 'Generate visualizations' or userInput == '3':
            print("What would you like to visualize? \n1. Age and Suicide rates \n2. Years and Suicide rates")
            userInputThree = input('I would like to visualize: ')

            if userInputThree == 'Age and Suicide rates' or userInputThree == '1':
                if 'AGE' in data.columns and 'ESTIMATE' in data.columns:
                    plt.bar(data['AGE'], data['ESTIMATE'])
                    plt.title('Age groups and Suicide rates')
                    plt.xlabel('Age groups')
                    plt.ylabel('Suicide Rate (Death per 100k people)')
                    plt.xticks(rotation=45)
                    plt.show()
                else:
                    print("Error: Required data columns 'AGE' and 'ESTIMATE' are missing.")

            elif userInputThree == 'Years and Suicide rates' or userInputThree == '2':
                if 'YEAR' in data.columns and 'ESTIMATE' in data.columns:
                    # Convert columns to numeric and handle invalid entries
                    data['YEAR'] = pd.to_numeric(data['YEAR'], errors='coerce')
                    data['ESTIMATE'] = pd.to_numeric(data['ESTIMATE'], errors='coerce')
                    # Drop rows with NaN values
                    data = data.dropna(subset=['YEAR', 'ESTIMATE'])
                    if data.empty:
                        print("Error: No valid data available for plotting.")
                    else:
                        data = data.sort_values(by='YEAR')
                        plt.bar(data['YEAR'], data['ESTIMATE'])
                        plt.title('Years and Suicide rates')
                        plt.xlabel('Years')
                        plt.ylabel('Suicide Rate (Death per 100k people)')
                        plt.xticks(rotation=45)
                        plt.show()
                else:
                    print("Error: Required data columns 'YEAR' and 'ESTIMATE' are missing.")

            else:
                print("Invalid input. Please try again.")

        # Exit program
        elif userInput == 'Exit program' or userInput == '4':
            print("Thank you for using the program. Goodbye!")
            break  # Exit the loop

        # Invalid input handling
        else:
            print("Invalid input. Please try again.")

# Run the Intro function
Intro()