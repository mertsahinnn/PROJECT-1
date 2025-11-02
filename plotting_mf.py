import matplotlib.pyplot as plt
import numpy as np


class FuzzificationPlotter:
    """
    A class to handle plotting of fuzzification functions for various house and application parameters.
    """
    
    def __init__(self, figsize=(14, 7)):
        """
        Initialize the plotter with default figure size.
        
        Parameters:
        figsize (tuple): Default figure size for plots
        """
        self.figsize = figsize
    
    def plot_interest_rate_fuzzification(self):
        """Plot the fuzzification of interest rates with all membership functions."""
        from fuzzification import interest_rate_fuzzification
        
        x_values = np.linspace(0, 10, 1000)
        low = [interest_rate_fuzzification(x)['Low'] for x in x_values]
        medium = [interest_rate_fuzzification(x)['Medium'] for x in x_values]
        high = [interest_rate_fuzzification(x)['High'] for x in x_values]
        
        plt.figure(figsize=self.figsize)
        plt.plot(x_values, low, label='Low', linewidth=2, color='blue')
        plt.plot(x_values, medium, label='Medium', linewidth=2, color='green')
        plt.plot(x_values, high, label='High', linewidth=2, color='orange')
        
        plt.fill_between(x_values, low, color='blue', alpha=0.4)
        plt.fill_between(x_values, medium, color='green', alpha=0.4)
        plt.fill_between(x_values, high, color='orange', alpha=0.4)

        plt.xlabel('Interest Rate (%)', fontsize=12)
        plt.ylabel('Membership Degree', fontsize=12)
        plt.title('Interest Rate Fuzzification', fontsize=14, fontweight='bold')
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.xlim(0, 10)
        plt.ylim(0, 1.1)
        
        plt.tight_layout()
        plt.show()
    
    def plot_application_salary_fuzzification(self):
        """Plot the fuzzification of application salary with all membership functions."""
        from fuzzification import application_salary_fuzzification
        
        x_values = np.linspace(0, 100000, 1000)
        low = [application_salary_fuzzification(x)['Low'] for x in x_values]
        medium = [application_salary_fuzzification(x)['Medium'] for x in x_values]
        high = [application_salary_fuzzification(x)['High'] for x in x_values]
        very_high = [application_salary_fuzzification(x)['Very High'] for x in x_values]
        
        plt.figure(figsize=self.figsize)
        plt.plot(x_values, low, label='Low', linewidth=2, color='blue')
        plt.plot(x_values, medium, label='Medium', linewidth=2, color='green')
        plt.plot(x_values, high, label='High', linewidth=2, color='orange')
        plt.plot(x_values, very_high, label='Very High', linewidth=2, color='red')
        
        plt.fill_between(x_values, low, color='blue', alpha=0.4)
        plt.fill_between(x_values, medium, color='green', alpha=0.4)
        plt.fill_between(x_values, high, color='orange', alpha=0.4)
        plt.fill_between(x_values, very_high, color='red', alpha=0.4)

        plt.xlabel('Salary ($)', fontsize=12)
        plt.ylabel('Membership Degree', fontsize=12)
        plt.title('Application Salary Fuzzification', fontsize=14, fontweight='bold')
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.xlim(0, 110000)
        plt.ylim(0, 1.1)
        
        ax = plt.gca()
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        plt.tight_layout()
        plt.show()

    def plot_application_assets_fuzzification(self):
        """Plot the fuzzification of application assets with all membership functions."""
        from fuzzification import applicaton_assets_fuzzification
        
        x_values = np.linspace(0, 1000000, 1000)
        low = [applicaton_assets_fuzzification(x)['Low'] for x in x_values]
        medium = [applicaton_assets_fuzzification(x)['Medium'] for x in x_values]
        high = [applicaton_assets_fuzzification(x)['High'] for x in x_values]
        
        plt.figure(figsize=self.figsize)
        plt.plot(x_values, low, label='Low', linewidth=2, color='blue')
        plt.plot(x_values, medium, label='Medium', linewidth=2, color='green')
        plt.plot(x_values, high, label='High', linewidth=2, color='orange')
        
        plt.fill_between(x_values, low, color='blue', alpha=0.4)
        plt.fill_between(x_values, medium, color='green', alpha=0.4)
        plt.fill_between(x_values, high, color='orange', alpha=0.4)

        plt.xlabel('Application Assets ($)', fontsize=12)
        plt.ylabel('Membership Degree', fontsize=12)
        plt.title('Application Assets Fuzzification', fontsize=14, fontweight='bold')
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.xlim(0, 1100000)
        plt.ylim(0, 1.1)
        
        ax = plt.gca()
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        plt.tight_layout()
        plt.show()

    def plot_market_value_fuzzification(self):
        """Plot the fuzzification of house market values with all membership functions."""
        from fuzzification import market_value_house_fuzzification
        
        x_values = np.linspace(0, 1000000, 1000)
        low = [market_value_house_fuzzification(x)['Low'] for x in x_values]
        medium = [market_value_house_fuzzification(x)['Medium'] for x in x_values]
        high = [market_value_house_fuzzification(x)['High'] for x in x_values]
        very_high = [market_value_house_fuzzification(x)['Very High'] for x in x_values]
        
        plt.figure(figsize=self.figsize)
        plt.plot(x_values, low, label='Low', linewidth=2, color='blue')
        plt.plot(x_values, medium, label='Medium', linewidth=2, color='green')
        plt.plot(x_values, high, label='High', linewidth=2, color='orange')
        plt.plot(x_values, very_high, label='Very High', linewidth=2, color='red')
        
        plt.fill_between(x_values, low, color='blue', alpha=0.4)
        plt.fill_between(x_values, medium, color='green', alpha=0.4)
        plt.fill_between(x_values, high, color='orange', alpha=0.4)
        plt.fill_between(x_values, very_high, color='red', alpha=0.4)

        plt.xlabel('Market Value ($)', fontsize=12)
        plt.ylabel('Membership Degree', fontsize=12)
        plt.title('House Market Value Fuzzification', fontsize=14, fontweight='bold')
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.xlim(0, 1000000)
        plt.ylim(0, 1.1)
        
        ax = plt.gca()
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        plt.tight_layout()
        plt.show()

    def plot_location_fuzzification(self):
        """Plot the fuzzification of house location with all membership functions."""
        from fuzzification import location_of_house_fuzzification
        
        x_values = np.linspace(0, 10, 1000)
        bad = [location_of_house_fuzzification(x)['Bad'] for x in x_values]
        fair = [location_of_house_fuzzification(x)['Fair'] for x in x_values]
        excellent = [location_of_house_fuzzification(x)['Excellent'] for x in x_values]
        
        plt.figure(figsize=self.figsize)
        plt.plot(x_values, bad, label='Bad', linewidth=2, color='red')
        plt.plot(x_values, fair, label='Fair', linewidth=2, color='yellow')
        plt.plot(x_values, excellent, label='Excellent', linewidth=2, color='green')

        plt.fill_between(x_values, bad, color='red', alpha=0.4)
        plt.fill_between(x_values, fair, color='yellow', alpha=0.4)
        plt.fill_between(x_values, excellent, color='green', alpha=0.4)

        plt.xlabel('Location Score', fontsize=12)
        plt.ylabel('Membership Degree', fontsize=12)
        plt.title('House Location Fuzzification', fontsize=14, fontweight='bold')
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.xlim(0, 10)
        plt.ylim(0, 1.1)
        
        plt.tight_layout()
        plt.show()
    
    def plot_all(self):
        """Plot all fuzzification functions."""
        self.plot_market_value_fuzzification()
        self.plot_location_fuzzification()
        self.plot_application_assets_fuzzification()
        self.plot_application_salary_fuzzification()
        self.plot_interest_rate_fuzzification()


# --- TESTING ---
if __name__ == "__main__":
    plotter = FuzzificationPlotter()
    plotter.plot_market_value_fuzzification()
    plotter.plot_location_fuzzification()
    # plotter.plot_all()  # Tüm grafikleri çizmek için
