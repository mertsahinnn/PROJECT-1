def evaluate_house_rule(market_fuzzy_values, location_fuzzy_values):
    """
    Takes fuzzified 'Market Value' and 'Location' inputs,
    applies House Evaluation rules, and returns the fuzzy result for the 'House' output.
    
    Args:
    market_fuzzy_values (dict): Fuzzy degrees for 'Market Value'.
                               {'Low': float, 'Medium': float, 'High': float, 'Very High': float}
    location_fuzzy_values (dict): Fuzzy degrees for 'Location'.
                                  {'Bad': float, 'Fair': float, 'Excellent': float}

    Returns:
    dict: Fuzzy degrees for the 'House' output.
          {'Very_low': float, 'Low': float, 'Medium': float, 'High': float, 'Very_high': float}
    """
    
    rule_strengths = {
        'Very_low': [],
        'Low': [],
        'Medium': [],
        'High': [],
        'Very_high': []
    }
    
    # --- Apply rules (AND = min, OR = max) ---
    
    # Rule 1: If (Market_value is Low) then (House is Low)
    rule_1 = market_fuzzy_values['Low']
    rule_strengths['Low'].append(rule_1)
    
    # Rule 2: If (Location is Bad) then (House is Low)
    rule_2 = location_fuzzy_values['Bad']
    rule_strengths['Low'].append(rule_2)
    
    # Rule 3: If (Location is Bad) and (Market_value is Low) then (House is Very_low)
    rule_3 = min(location_fuzzy_values['Bad'], market_fuzzy_values['Low'])
    rule_strengths['Very_low'].append(rule_3)
    
    # Rule 4: If (Location is Bad) and (Market_value is Medium) then (House is Low)
    rule_4 = min(location_fuzzy_values['Bad'], market_fuzzy_values['Medium'])
    rule_strengths['Low'].append(rule_4)
    
    # Rule 5: If (Location is Bad) and (Market_value is High) then (House is Medium)
    rule_5 = min(location_fuzzy_values['Bad'], market_fuzzy_values['High'])
    rule_strengths['Medium'].append(rule_5)
    
    # Rule 6: If (Location is Bad) and (Market_value is Very_high) then (House is High)
    rule_6 = min(location_fuzzy_values['Bad'], market_fuzzy_values['Very High'])
    rule_strengths['High'].append(rule_6)
    
    # Rule 7: If (Location is Fair) and (Market_value is Low) then (House is Low)
    rule_7 = min(location_fuzzy_values['Fair'], market_fuzzy_values['Low'])
    rule_strengths['Low'].append(rule_7)
    
    # Rule 8: If (Location is Fair) and (Market_value is Medium) then (House is Medium)
    rule_8 = min(location_fuzzy_values['Fair'], market_fuzzy_values['Medium'])
    rule_strengths['Medium'].append(rule_8)
    
    # Rule 9: If (Location is Fair) and (Market_value is High) then (House is High)
    rule_9 = min(location_fuzzy_values['Fair'], market_fuzzy_values['High'])
    rule_strengths['High'].append(rule_9)
    
    # Rule 10: If (Location is Fair) and (Market_value is Very_high) then (House is Very_high)
    rule_10 = min(location_fuzzy_values['Fair'], market_fuzzy_values['Very High'])
    rule_strengths['Very_high'].append(rule_10)
    
    # Rule 11: If (Location is Excellent) and (Market_value is Low) then (House is Medium)
    rule_11 = min(location_fuzzy_values['Excellent'], market_fuzzy_values['Low'])
    rule_strengths['Medium'].append(rule_11)
    
    # Rule 12: If (Location is Excellent) and (Market_value is Medium) then (House is High)
    rule_12 = min(location_fuzzy_values['Excellent'], market_fuzzy_values['Medium'])
    rule_strengths['High'].append(rule_12)
    
    # Rule 13: If (Location is Excellent) and (Market_value is High) then (House is Very_high)
    rule_13 = min(location_fuzzy_values['Excellent'], market_fuzzy_values['High'])
    rule_strengths['Very_high'].append(rule_13)
    
    # Rule 14: If (Location is Excellent) and (Market_value is Very_high) then (House is Very_high)
    rule_14 = min(location_fuzzy_values['Excellent'], market_fuzzy_values['Very High'])
    rule_strengths['Very_high'].append(rule_14)
    
    # --- For each output category, take the maximum rule strength (OR operation) ---
    house_output = {
        'Very_low': max(rule_strengths['Very_low']) if rule_strengths['Very_low'] else 0,
        'Low': max(rule_strengths['Low']) if rule_strengths['Low'] else 0,
        'Medium': max(rule_strengths['Medium']) if rule_strengths['Medium'] else 0,
        'High': max(rule_strengths['High']) if rule_strengths['High'] else 0,
        'Very_high': max(rule_strengths['Very_high']) if rule_strengths['Very_high'] else 0
    }
    
    return house_output


def evaluate_application_rule(assets_fuzzy_values, salary_fuzzy_values):
    """
    Takes fuzzified 'Assets' and 'Salary' inputs,
    applies Application Evaluation rules, and returns the fuzzy result for the 'Application' output.
    
    Args:
    assets_fuzzy_values (dict): Fuzzy degrees for 'Assets'.
                                 {'Low': float, 'Medium': float, 'High': float}
    salary_fuzzy_values (dict): Fuzzy degrees for 'Salary'.
                                 {'Low': float, 'Medium': float, 'High': float, 'Very High': float}

    Returns:
    dict: Fuzzy degrees for the 'Application' output.
          {'Low': float, 'Medium': float, 'High': float}
    """
    
    rule_strengths = {
        'Low': [],
        'Medium': [],
        'High': []
    }
    
    # --- Apply rules (AND = min, OR = max) ---
    
    # Rule 1: If (Asset is Low) and (Income is Low) then (Applicant is Low)
    rule_1 = min(assets_fuzzy_values['Low'], salary_fuzzy_values['Low'])
    rule_strengths['Low'].append(rule_1)
    
    # Rule 2: If (Asset is Low) and (Income is Medium) then (Applicant is Low)
    rule_2 = min(assets_fuzzy_values['Low'], salary_fuzzy_values['Medium'])
    rule_strengths['Low'].append(rule_2)
    
    # Rule 3: If (Asset is Low) and (Income is High) then (Applicant is Medium)
    rule_3 = min(assets_fuzzy_values['Low'], salary_fuzzy_values['High'])
    rule_strengths['Medium'].append(rule_3)
    
    # Rule 4: If (Asset is Low) and (Income is Very_high) then (Applicant is High)
    rule_4 = min(assets_fuzzy_values['Low'], salary_fuzzy_values['Very High'])
    rule_strengths['High'].append(rule_4)
    
    # Rule 5: If (Asset is Medium) and (Income is Low) then (Applicant is Low)
    rule_5 = min(assets_fuzzy_values['Medium'], salary_fuzzy_values['Low'])
    rule_strengths['Low'].append(rule_5)
    
    # Rule 6: If (Asset is Medium) and (Income is Medium) then (Applicant is Medium)
    rule_6 = min(assets_fuzzy_values['Medium'], salary_fuzzy_values['Medium'])
    rule_strengths['Medium'].append(rule_6)
    
    # Rule 7: If (Asset is Medium) and (Income is High) then (Applicant is High)
    rule_7 = min(assets_fuzzy_values['Medium'], salary_fuzzy_values['High'])
    rule_strengths['High'].append(rule_7)
    
    # Rule 8: If (Asset is Medium) and (Income is Very_high) then (Applicant is High)
    rule_8 = min(assets_fuzzy_values['Medium'], salary_fuzzy_values['Very High'])
    rule_strengths['High'].append(rule_8)
    
    # Rule 9: If (Asset is High) and (Income is Low) then (Applicant is Medium)
    rule_9 = min(assets_fuzzy_values['High'], salary_fuzzy_values['Low'])
    rule_strengths['Medium'].append(rule_9)
    
    # Rule 10: If (Asset is High) and (Income is Medium) then (Applicant is Medium)
    rule_10 = min(assets_fuzzy_values['High'], salary_fuzzy_values['Medium'])
    rule_strengths['Medium'].append(rule_10)
    
    # Rule 11: If (Asset is High) and (Income is High) then (Applicant is High)
    rule_11 = min(assets_fuzzy_values['High'], salary_fuzzy_values['High'])
    rule_strengths['High'].append(rule_11)
    
    # Rule 12: If (Asset is High) and (Income is Very_high) then (Applicant is High)
    rule_12 = min(assets_fuzzy_values['High'], salary_fuzzy_values['Very High'])
    rule_strengths['High'].append(rule_12)
    
    # --- For each output category, take the maximum rule strength (OR operation) ---
    application_output = {
        'Low': max(rule_strengths['Low']) if rule_strengths['Low'] else 0,
        'Medium': max(rule_strengths['Medium']) if rule_strengths['Medium'] else 0,
        'High': max(rule_strengths['High']) if rule_strengths['High'] else 0
    }
    
    return application_output

def evaluate_loan_rule(salary_fuzzy_values, interest_fuzzy_values, application_fuzzy_values, house_fuzzy_values):
    """
    Takes fuzzified 'Salary', 'Interest Rate', 'Application', and 'House' inputs,
    applies Loan Evaluation rules, and returns the fuzzy result for the 'Credit' output.
    
    Args:
    salary_fuzzy_values (dict): Fuzzy degrees for 'Salary'.
                                 {'Low': float, 'Medium': float, 'High': float, 'Very High': float}
    interest_fuzzy_values (dict): Fuzzy degrees for 'Interest Rate'.
                                   {'Low': float, 'Medium': float, 'High': float}
    application_fuzzy_values (dict): Fuzzy degrees for 'Application'.
                                      {'Low': float, 'Medium': float, 'High': float}
    house_fuzzy_values (dict): Fuzzy degrees for 'House'.
                                {'Very_low': float, 'Low': float, 'Medium': float, 'High': float, 'Very_high': float}

    Returns:
    dict: Fuzzy degrees for the 'Credit' output.
          {'Very_low': float, 'Low': float, 'Medium': float, 'High': float, 'Very_high': float}
    """
    
    rule_strengths = {
        'Very_low': [],
        'Low': [],
        'Medium': [],
        'High': [],
        'Very_high': []
    }
    
    # --- Apply rules (AND = min, OR = max) ---
    
    # Rule 1: If (Income is Low) and (Interest is Medium) then (Credit is Very_low)
    rule_1 = min(salary_fuzzy_values['Low'], interest_fuzzy_values['Medium'])
    rule_strengths['Very_low'].append(rule_1)
    
    # Rule 2: If (Income is Low) and (Interest is High) then (Credit is Very_low)
    rule_2 = min(salary_fuzzy_values['Low'], interest_fuzzy_values['High'])
    rule_strengths['Very_low'].append(rule_2)
    
    # Rule 3: If (Income is Medium) and (Interest is High) then (Credit is Low)
    rule_3 = min(salary_fuzzy_values['Medium'], interest_fuzzy_values['High'])
    rule_strengths['Low'].append(rule_3)
    
    # Rule 4: If (Applicant is Low) then (Credit is Very_low)
    rule_4 = application_fuzzy_values['Low']
    rule_strengths['Very_low'].append(rule_4)
    
    # Rule 5: If (House is Very_low) then (Credit is Very_low)
    rule_5 = house_fuzzy_values['Very_low']
    rule_strengths['Very_low'].append(rule_5)
    
    # Rule 6: If (Applicant is Medium) and (House is Very_low) then (Credit is Low)
    rule_6 = min(application_fuzzy_values['Medium'], house_fuzzy_values['Very_low'])
    rule_strengths['Low'].append(rule_6)
    
    # Rule 7: If (Applicant is Medium) and (House is Low) then (Credit is Low)
    rule_7 = min(application_fuzzy_values['Medium'], house_fuzzy_values['Low'])
    rule_strengths['Low'].append(rule_7)
    
    # Rule 8: If (Applicant is Medium) and (House is Medium) then (Credit is Medium)
    rule_8 = min(application_fuzzy_values['Medium'], house_fuzzy_values['Medium'])
    rule_strengths['Medium'].append(rule_8)
    
    # Rule 9: If (Applicant is Medium) and (House is High) then (Credit is High)
    rule_9 = min(application_fuzzy_values['Medium'], house_fuzzy_values['High'])
    rule_strengths['High'].append(rule_9)
    
    # Rule 10: If (Applicant is Medium) and (House is Very_high) then (Credit is High)
    rule_10 = min(application_fuzzy_values['Medium'], house_fuzzy_values['Very_high'])
    rule_strengths['High'].append(rule_10)
    
    # Rule 11: If (Applicant is High) and (House is Very_low) then (Credit is Low)
    rule_11 = min(application_fuzzy_values['High'], house_fuzzy_values['Very_low'])
    rule_strengths['Low'].append(rule_11)
    
    # Rule 12: If (Applicant is High) and (House is Low) then (Credit is Medium)
    rule_12 = min(application_fuzzy_values['High'], house_fuzzy_values['Low'])
    rule_strengths['Medium'].append(rule_12)
    
    # Rule 13: If (Applicant is High) and (House is Medium) then (Credit is High)
    rule_13 = min(application_fuzzy_values['High'], house_fuzzy_values['Medium'])
    rule_strengths['High'].append(rule_13)
    
    # Rule 14: If (Applicant is High) and (House is High) then (Credit is High)
    rule_14 = min(application_fuzzy_values['High'], house_fuzzy_values['High'])
    rule_strengths['High'].append(rule_14)
    
    # Rule 15: If (Applicant is High) and (House is Very_high) then (Credit is Very_high)
    rule_15 = min(application_fuzzy_values['High'], house_fuzzy_values['Very_high'])
    rule_strengths['Very_high'].append(rule_15)
    
    # --- For each output category, take the maximum rule strength (OR operation) ---
    credit_output = {
        'Very_low': max(rule_strengths['Very_low']) if rule_strengths['Very_low'] else 0,
        'Low': max(rule_strengths['Low']) if rule_strengths['Low'] else 0,
        'Medium': max(rule_strengths['Medium']) if rule_strengths['Medium'] else 0,
        'High': max(rule_strengths['High']) if rule_strengths['High'] else 0,
        'Very_high': max(rule_strengths['Very_high']) if rule_strengths['Very_high'] else 0
    }
    
    return credit_output


# --- TESTING ---
if __name__ == "__main__":
    # Test data - House Evaluation
    market_value = {'Low': 0.8, 'Medium': 0.2, 'High': 0.0, 'Very High': 0.0}
    location = {'Bad': 0.1, 'Fair': 0.5, 'Excellent': 0.4}
    
    result = evaluate_house_rule(market_value, location)
    print("House Evaluation Result:")
    for key, value in result.items():
        print(f"  {key}: {value:.2f}")
    
    print("\n" + "="*50 + "\n")
    
    # Test data - Application Evaluation
    assets = {'Low': 0.3, 'Medium': 0.5, 'High': 0.2}
    salary = {'Low': 0.1, 'Medium': 0.4, 'High': 0.3, 'Very High': 0.2}
    
    result = evaluate_application_rule(assets, salary)
    print("Application Evaluation Result:")
    for key, value in result.items():
        print(f"  {key}: {value:.2f}")
    
    print("\n" + "="*50 + "\n")
    
    # Test data - Loan Evaluation
    salary = {'Low': 0.2, 'Medium': 0.5, 'High': 0.2, 'Very High': 0.1}
    interest_rate = {'Low': 0.3, 'Medium': 0.4, 'High': 0.3}
    application = {'Low': 0.1, 'Medium': 0.6, 'High': 0.3}
    house = {'Very_low': 0.0, 'Low': 0.2, 'Medium': 0.5, 'High': 0.2, 'Very_high': 0.1}
    
    result = evaluate_loan_rule(salary, interest_rate, application, house)
    print("Loan Evaluation Result:")
    for key, value in result.items():
        print(f"  {key}: {value:.2f}")