import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate the mean
def calculate_mean(data):
    return sum(data) / len(data)

# Define a function to calculate the variance
def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

# Define a function to calculate the standard deviation
def calculate_std_deviation(data):
    return calculate_variance(data) ** 0.5

# Define a function to calculate z-scores
def calculate_z_scores(data):
    mean = calculate_mean(data)
    std_dev = calculate_std_deviation(data)
    return [(x - mean) / std_dev for x in data]

# Define a function to calculate the median
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]
    return median

# Read data from the Excel file
file_path = "./diabetes.xlsx"
data = pd.read_excel(file_path)

# Extract the "Glucose" and "BloodPressure" columns
glucose_data = data["Glucose"]
blood_pressure_data = data["BloodPressure"]

# Calculate statistics
glucose_mean = calculate_mean(glucose_data)
glucose_variance = calculate_variance(glucose_data)
glucose_std_dev = calculate_std_deviation(glucose_data)
glucose_z_scores = calculate_z_scores(glucose_data)
glucose_median = calculate_median(glucose_data)

blood_pressure_mean = calculate_mean(blood_pressure_data)
blood_pressure_variance = calculate_variance(blood_pressure_data)
blood_pressure_std_dev = calculate_std_deviation(blood_pressure_data)
blood_pressure_z_scores = calculate_z_scores(blood_pressure_data)
blood_pressure_median = calculate_median(blood_pressure_data)

# Print the statistics
print("Statistics for Glucose:")
print(f"Mean: {glucose_mean}")
print(f"Variance: {glucose_variance}")
print(f"Standard Deviation: {glucose_std_dev}")
print(f"Z-Scores: {glucose_z_scores}")
print(f"Median: {glucose_median}\n")

print("Statistics for Blood Pressure:")
print(f"Mean: {blood_pressure_mean}")
print(f"Variance: {blood_pressure_variance}")
print(f"Standard Deviation: {blood_pressure_std_dev}")
print(f"Z-Scores: {blood_pressure_z_scores}")
print(f"Median: {blood_pressure_median}\n")

# Create boxplots
plt.boxplot([glucose_data, blood_pressure_data], labels=["Glucose", "Blood Pressure"])
plt.title("Boxplots for Glucose and Blood Pressure")
plt.xlabel("Variable")
plt.ylabel("Value")
plt.show()
