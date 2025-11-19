import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Import project modules
from defuzzification import Defuzzifier
import fuzzification
from inference import evaluate_application_rule, evaluate_house_rule, evaluate_loan_rule
# plotting_mf is not strictly needed for the main logic but useful if we want to show MF plots
# from plotting_mf import FuzzificationPlotter 

class FuzzyLogicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fuzzy Logic Credit Evaluation System")
        self.root.geometry("600x750")
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main Frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Credit Evaluation System", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # --- Inputs ---
        self.entries = {}
        
        # Market Value
        self.create_input_field(main_frame, 1, "Market Value ($):", "market_house", 87000)
        
        # Location Score
        self.create_input_field(main_frame, 2, "Location Score (0-10):", "location_house", 4.5)
        
        # Application Assets
        self.create_input_field(main_frame, 3, "Assets ($):", "application_assets", 150000)
        
        # Application Salary
        self.create_input_field(main_frame, 4, "Salary ($):", "application_salary", 45000)
        
        # Interest Rate
        self.create_input_field(main_frame, 5, "Interest Rate (%):", "interest_rate", 3.5)
        
        # --- Buttons ---
        calc_button = ttk.Button(main_frame, text="Calculate Credit Score", command=self.calculate)
        calc_button.grid(row=6, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)
        
        # --- Outputs ---
        self.result_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        self.result_frame.grid(row=7, column=0, columnspan=2, sticky="ew", pady=10)
        
        self.house_score_label = ttk.Label(self.result_frame, text="House Score: -", font=("Helvetica", 12))
        self.house_score_label.pack(anchor="w", pady=2)
        
        self.app_score_label = ttk.Label(self.result_frame, text="Application Score: -", font=("Helvetica", 12))
        self.app_score_label.pack(anchor="w", pady=2)
        
        self.credit_score_label = ttk.Label(self.result_frame, text="Credit Score: -", font=("Helvetica", 14, "bold"))
        self.credit_score_label.pack(anchor="w", pady=5)
        
        # --- Visualization Options ---
        self.plot_frame = ttk.LabelFrame(main_frame, text="Visualizations", padding="10")
        self.plot_frame.grid(row=8, column=0, columnspan=2, sticky="ew", pady=10)
        
        self.plot_house_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.plot_frame, text="Show House Defuzzification", variable=self.plot_house_var).pack(anchor="w")
        
        self.plot_app_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.plot_frame, text="Show Application Defuzzification", variable=self.plot_app_var).pack(anchor="w")
        
        self.plot_credit_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.plot_frame, text="Show Credit Defuzzification", variable=self.plot_credit_var).pack(anchor="w")

    def create_input_field(self, parent, row, label_text, var_name, default_val):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, sticky="w", pady=5)
        entry = ttk.Entry(parent)
        entry.insert(0, str(default_val))
        entry.grid(row=row, column=1, sticky="e", pady=5)
        self.entries[var_name] = entry

    def calculate(self):
        try:
            # 1. Get Inputs
            market_house = float(self.entries["market_house"].get())
            location_house = float(self.entries["location_house"].get())
            application_assets = float(self.entries["application_assets"].get())
            application_salary = float(self.entries["application_salary"].get())
            interest_rate = float(self.entries["interest_rate"].get())
            
            # 2. Fuzzification
            fuzzified_market_house = fuzzification.market_value_house_fuzzification(market_house)
            fuzzified_location_house = fuzzification.location_of_house_fuzzification(location_house)
            fuzzified_application_assets = fuzzification.applicaton_assets_fuzzification(application_assets)
            fuzzified_application_salary = fuzzification.application_salary_fuzzification(application_salary)
            fuzzified_interest_rate = fuzzification.interest_rate_fuzzification(interest_rate)
            
            # 3. Inference
            # House Evaluation
            result_evaluation_house = evaluate_house_rule(fuzzified_market_house, fuzzified_location_house)
            
            # Application Evaluation
            result_evaluation_application = evaluate_application_rule(fuzzified_application_assets, fuzzified_application_salary)
            
            # Loan Evaluation
            # Note: evaluate_loan_rule expects specific inputs. 
            # Based on inference.py: evaluate_loan_rule(salary, interest_rate, application, house)
            # It seems it uses the FUZZIFIED salary and interest rate directly, 
            # PLUS the FUZZY OUTPUTS of application and house evaluations.
            
            result_loan = evaluate_loan_rule(
                fuzzified_application_salary, 
                fuzzified_interest_rate, 
                result_evaluation_application, 
                result_evaluation_house
            )
            
            # 4. Defuzzification
            defuzz = Defuzzifier()
            
            house_score = defuzz.centroid_defuzzification(result_evaluation_house, 'house')
            app_score = defuzz.centroid_defuzzification(result_evaluation_application, 'application')
            credit_score = defuzz.centroid_defuzzification(result_loan, 'credit')
            
            # 5. Update UI
            self.house_score_label.config(text=f"House Score: {house_score:.2f} / 10")
            self.app_score_label.config(text=f"Application Score: {app_score:.2f} / 10")
            self.credit_score_label.config(text=f"Credit Score: {credit_score:.2f} / 1000")
            
            # 6. Plotting
            # We use the existing visualize_defuzzification method which calls plt.show()
            # This will open separate windows.
            if self.plot_house_var.get():
                defuzz.visualize_defuzzification(result_evaluation_house, 'house')
                
            if self.plot_app_var.get():
                defuzz.visualize_defuzzification(result_evaluation_application, 'application')
                
            if self.plot_credit_var.get():
                defuzz.visualize_defuzzification(result_loan, 'credit')
                
        except ValueError as e:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FuzzyLogicApp(root)
    root.mainloop()
