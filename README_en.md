---

# Basal Metabolic Rate (BMR) Calculator

This is a simple Python script that calculates a person's Basal Metabolic Rate (BMR), which is the number of calories the body burns at rest to maintain vital functions such as breathing and circulation. BMR is an important parameter for people who want to control their diet and energy expenditure, especially in the context of weight management or fitness goals.

## How It Works

- The program prompts the user for the following information:
  - **Sex** (M for male, F for female)
  - **Weight** in kilograms
  - **Height** in centimeters
  - **Age** in years

- Based on this information, the BMR is calculated using the following formulas:
  - For males:  
    `BMR = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)`
  - For females:  
    `BMR = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)`

- The calculated BMR is then displayed in calories per day.

## How to Use

1. Run the script in your Python environment.
2. The program will ask you to input your sex, weight, height, and age.
3. After entering the data, the BMR value will be displayed on the screen.
4. Press Enter to exit the program.

## Example of Execution

```text
[BMR Calculator]

Enter your sex (M for male, F for female): M
Enter your weight in kg: 70
Enter your height in cm: 175
Enter your age: 25

Your Basal Metabolic Rate (BMR) is: 1754.40 calories/day.
Press Enter to exit...
```

## Requirements

- Python 3.x or higher.

---
