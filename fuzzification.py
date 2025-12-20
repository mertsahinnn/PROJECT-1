import matplotlib.pyplot as plt
import numpy as np
from membership_function import trapezoidal_membership, triangle_membership
from plotting_mf import FuzzificationPlotter


def market_value_house_fuzzification(value):
    """
    Fuzzify the market value of a house into linguistic categories:
    'Low', 'Medium','High' and 'Very High' using trapezoidal membership function.

    Parameters:
    value (float): The market value of the house.

    Returns:
    dict: A dictionary with membership values for each category.
    """
    memberships = {
        'Low': trapezoidal_membership(value, 0, 0, 70000,100000),
        'Medium': trapezoidal_membership(value, 50000, 100000, 200000, 250000),
        'High': trapezoidal_membership(value, 200000, 300000, 650000, 850000),
        'Very High': trapezoidal_membership(value, 650000, 850000, 1000000, 1000000)
    }
    return memberships


def location_of_house_fuzzification(location):
    """
    Fuzzify the location of a house into linguistic categories:
    'Bad', 'Fair' and 'Excellent' using trapezoidal membership functions.

    Parameters:
    location (float): The location score of the house.

    Returns:
    dict: A dictionary with membership values for each category.
    """
    memberships = {
        'Bad': trapezoidal_membership(location, 0, 0, 1.5, 4),
        'Fair': trapezoidal_membership(location, 2.5, 5, 6, 8.5),
        'Excellent': trapezoidal_membership(location, 6, 8.5, 10, 10)
    }
    return memberships


def application_assets_fuzzification(assets):
    """
    Fuzzify the application assets into linguistic categories:
    'Low', 'Medium', and 'High' using trapezoidal and triangular membership functions.

    Parameters:
    assets (float): The total assets of the applicant.

    Returns:
    dict: A dictionary with membership values for each category.
    """
    memberships = {
        'Low': triangle_membership(assets, 0, 0, 150000),
        'Medium': trapezoidal_membership(assets, 50000, 250000, 450000, 650000),
        'High': trapezoidal_membership(assets, 500000, 700000, 1000000, 1000000)
    }
    return memberships

def application_salary_fuzzification(income):
    """
    Fuzzify the application salary into linguistic categories:
    'Low', 'Medium', 'High' and 'Very High' using trapezoidal and triangular membership functions.

    Parameters:
    income (float): The salary of the applicant.

    Returns:
    dict: A dictionary with membership values for each category.
    """
    memberships = {
        'Low': trapezoidal_membership(income, 0, 0, 10000, 25000),
        'Medium': triangle_membership(income, 15000, 35000, 55000),
        'High': triangle_membership(income, 40000, 60000, 80000),
        'Very High': trapezoidal_membership(income, 60000, 80000, 100000, 100000)
    }
    return memberships

def interest_rate_fuzzification(rate):
    """
    Fuzzify the interest rate into linguistic categories:
    'Low', 'Medium', and 'High' using trapezoidal membership functions.

    Parameters:
    rate (float): The interest rate.

    Returns:
    dict: A dictionary with membership values for each category.
    """
    memberships = {
        'Low': trapezoidal_membership(rate, 0, 0, 2, 5),
        'Medium': trapezoidal_membership(rate, 2, 4, 6, 8),
        'High': trapezoidal_membership(rate, 6, 8.5, 10, 10)
    }
    return memberships

def house_fuzzification(house):
    """
    Fuzzify the house parameter into linguistic categories:
    'Very low', 'Low', 'Medium', 'High', and 'Very High' using triangular membership functions.

    Parameters:
    house (float): The value of the house.

    Returns:
    dict: A dictionary with membership values for each category.
    """
    memberships = {
        'Very_low': triangle_membership(house, 0, 0, 3),
        'Low': triangle_membership(house, 0, 3, 6),
        'Medium': triangle_membership(house, 2, 5, 8),
        'High': triangle_membership(house, 4, 7, 10),
        'Very_high': triangle_membership(house, 7, 10, 10)
    }
    return memberships

def application_fuzzification(application):
    """
    Fuzzify the application parameter into linguistic categories:
    'Low', 'Medium' and 'High' using triangular and trapezoidal membership functions.

    Parameters:
    application (float): The value of the application.

    Returns:
    dict: A dictionary with membership values for each category.
    """
    memberships = {
        'Low': trapezoidal_membership(application, 0, 0, 2, 4),
        'Medium': triangle_membership(application, 2, 5, 8),
        'High': trapezoidal_membership(application, 6, 8, 10, 10)
    }
    return memberships
    
   



# --- TESTING THE FUZZIFICATION FUNCTIONS ---
if __name__ == "__main__":
    
    plotter = FuzzificationPlotter(figsize=(14, 7))

    test_values = [87000, 50000, 150000, 400000, 900000, 1200000]
    for val in test_values:
        fuzzified = market_value_house_fuzzification(val)
        print(f"Market Value: {val} => Fuzzified: {fuzzified}")
        
        
    test_values_location = [1, 3, 5, 7, 9, 10]
    for val in test_values_location:
        fuzzified = location_of_house_fuzzification(val)
        print(f"Location Score: {val} => Fuzzified: {fuzzified}")

    plotter.plot_market_value_fuzzification()    
    plotter.plot_location_fuzzification()
    
    
    
    