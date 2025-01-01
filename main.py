# File description
# Project: Demographics and Suicide Rates 
# Author: Musammat Aktar
# Interactive data analysis program for Suicide Rates over years, among age groups, gender,and races.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('data/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv')

# Introduction message
print('Hi there! \nWelcome to this program. \nHere you can investigate suicide rates per 100,000 people over years, gender, race, and age.')

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
            print("What specific features would you like to focus on? \n1. Female count \n2. Male count \n3. Average age \n4. Race break down")
            userInputTwo = input('I would like to see the: ')
         # Females death count
            if userInputTwo == 'female count' or userInputTwo == '1':
                female_count = data[data['STUB_LABEL'].str.strip().str.lower() == 'female'].shape[0]
                print(f'Total females deaths per 100k {female_count}')
        # Male death count
            elif userInputTwo == 'male count' or userInputTwo == '2':
                male_count = data[data['STUB_LABEL'].str.strip().str.lower() == 'male'].shape[0]
                print(f'Total males deaths per 100k {male_count}')
         # Average age of death
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
          # Race and death rates
            elif userInputTwo == 'Race break down' or userInputTwo == '4':
                # White
                if 'STUB_LABEL' in data.columns:
                     # Function to count occurrences of the word "white"
                    def count_white_people(data):
                        count = 0
                        for row in data['STUB_LABEL']:
                            count += str(row).lower().count("white")  # case-insensitive search for "white"
                        return count
                    # Call the function
                    white_count = count_white_people(data)
                    print(f"There are {white_count} White people that die per 100k people.")
                # Black
                if 'STUB_LABEL' in data.columns:
                     # Function to count occurrences of the word "black"
                    def count_black_people(data):
                        count = 0
                        for row in data['STUB_LABEL']:
                            count += str(row).lower().count("black")  # case-insensitive search for "black"
                        return count
                    # Call the function
                    black_count = count_black_people(data)
                    print(f"There are {black_count} Black people that die per 100k people.")
                # Hispanic
                if 'STUB_LABEL' in data.columns:
                     # Function to count occurrences of the word "hispanic"
                    def count_hispanic_people(data):
                        count = 0
                        for row in data['STUB_LABEL']:
                            row = str(row).lower()  # case-insensitive search for "hispanic"
                            if 'hispanic' in row and 'not hispanic' not in row:
                                count += 1
                        return count
                    # Call the function
                    hispanic_count = count_hispanic_people(data)
                    print(f"There are {hispanic_count} Hispanic people that die per 100k people.")
                # Native America
                if 'STUB_LABEL' in data.columns:
                     # Function to count occurrences of the word "American Indian"
                    def count_AmericanIndian_people(data):
                        count = 0
                        for row in data['STUB_LABEL']:
                            row = str(row).lower()
                            if "american indian" in row or "alaska native" in row:  # case-insensitive search for "American Indian"
                                count += 1
                        return count
                    # Call the function
                    AmericanIndian_count = count_AmericanIndian_people(data)
                    print(f"There are {AmericanIndian_count} American Indian people that die per 100k people.")
                # Asian
                if 'STUB_LABEL' in data.columns:
                     # Function to count occurrences of the word "asian"
                    def count_asian_people(data):
                        count = 0
                        for row in data['STUB_LABEL']:
                            count += str(row).lower().count("asian")  # case-insensitive search for "white"
                        return count
                    # Call the function
                    asian_count = count_asian_people(data)
                    print(f"There are {asian_count} asian people that die per 100k people.")
                
                else:
                    print("Column 'STUB_LABEL' not found in the data.")        
        # Invalid input
            else:
                print("Invalid input. Please try again.")

        # Generate visualizations
        elif userInput == 'Generate visualizations' or userInput == '3':
            print("What would you like to visualize? \n1. Age and Suicide rates \n2. Years and Suicide rates \n3. Race and Suicide Rates \n4. Gender and Suicide Rates")
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
            # Graph: Year v. Suicide rate
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
            # Graph: Race v. Sucide rate
            elif userInputThree == 'Race and Suicide Rates' or userInputThree == '3':
                if 'STUB_LABEL' in data.columns:
                    race_keywords = {
                        'White': 'white',
                        'Black': 'black',
                        'Hispanic': 'hispanic',
                        'American Indian/Alaska Native': ['american indian', 'alaska native'],
                        'Asian': 'asian',
                    }
                    # Initialize a dictionary to hold counts
                    race_counts = {race: 0 for race in race_keywords}
                    # Count occurrences for each race
                    for row in data['STUB_LABEL']:
                        row_lower = row.lower()  # Convert row to lowercase for case-insensitive matching
                        if 'not hispanic' in row_lower:  # Exclude rows mentioning "not hispanic"
                            continue #skip this row
                        for race, keywords in race_keywords.items():
                            if isinstance(keywords, list):
                                if any(keyword in row_lower for keyword in keywords):
                                    race_counts[race] += 1
                            elif keywords in row_lower:
                                race_counts[race] += 1
                    # Create a DataFrame for plotting
                    race_summary = pd.DataFrame.from_dict(race_counts, orient='index', columns=['Deaths per 100k'])
                    race_summary.sort_values(by='Deaths per 100k', inplace=True)

                    # Plot the data
                    plt.figure(figsize=(10, 6))
                    race_summary['Deaths per 100k'].plot(kind='bar', color='coral', edgecolor='black')
                    plt.title('Deaths per 100k by Race', fontsize=16)
                    plt.xlabel('Race', fontsize=14)
                    plt.ylabel('Deaths per 100k', fontsize=14)
                    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
                    plt.tight_layout()

                    # Show the graph
                    plt.show()
                else:
                    print("Required columns ('STUB_LABEL') are not present in the dataset.")
            # Graph: Gender v. Suicide rate
            elif userInputThree == 'Gender and Suicide Rates' or userInputThree == '4':
                if 'STUB_LABEL' in data.columns: 
                    # Count the number of female deaths
                    female_count = data[data['STUB_LABEL'].str.strip().str.lower() == 'female'].shape[0]
                    print(f'Total female deaths per 100k: {female_count}')
                    
                    # Count the number of male deaths
                    male_count = data[data['STUB_LABEL'].str.strip().str.lower() == 'male'].shape[0]
                    # Create a DataFrame for plotting
                    gender_counts = {'Male': male_count, 'Female': female_count}
                    gender_summary = pd.DataFrame.from_dict(gender_counts, orient='index', columns=['Death Count per 100k'])
                    
                    # Plot the data
                    plt.figure(figsize=(8, 6))
                    gender_summary['Death Count per 100k'].plot(kind='bar', color=['blue', 'pink'], edgecolor='black')
                    plt.title('Death counts of Male and Female per 100k', fontsize=16)
                    plt.xlabel('Gender', fontsize=14)
                    plt.ylabel('Death Count per 100k', fontsize=14)
                    plt.xticks(rotation=0)  # Keep x-axis labels horizontal
                    plt.tight_layout()

                    # Show the graph
                    plt.show()
                else:
                    print("Required column ('STUB_LABEL') is not present in the dataset.")
        # Invalid Input
            else:
                print("Invalid input. Please try again.")

        # Exit program
        elif userInput == 'Exit program' or userInput == '4':
            print("Thank you for engaging with the program, and we hope you gained valuable insights! Goodbye!")
            break  # Exit the loop
        # Invalid Input
        else:
            print("Invalid input. Please try again.")

# Run the Intro function
Intro()