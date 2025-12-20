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
    
    def plot_interest_rate_fuzzification(self, input_value=None, ax=None):
        """Plot the fuzzification of interest rates with all membership functions."""
        from fuzzification import interest_rate_fuzzification
        
        x_values = np.linspace(0, 10, 1000)
        low = [interest_rate_fuzzification(x)['Low'] for x in x_values]
        medium = [interest_rate_fuzzification(x)['Medium'] for x in x_values]
        high = [interest_rate_fuzzification(x)['High'] for x in x_values]
        
        if ax is None:
            plt.figure(figsize=self.figsize)
            ax = plt.gca()
            show_plot = True
        else:
            show_plot = False

        ax.plot(x_values, low, label='Low', linewidth=2, color='blue')
        ax.plot(x_values, medium, label='Medium', linewidth=2, color='green')
        ax.plot(x_values, high, label='High', linewidth=2, color='orange')
        
        ax.fill_between(x_values, low, color='blue', alpha=0.4)
        ax.fill_between(x_values, medium, color='green', alpha=0.4)
        ax.fill_between(x_values, high, color='orange', alpha=0.4)

        if input_value is not None:
            ax.axvline(x=input_value, color='black', linestyle='--', linewidth=1.5, label=f'Input: {input_value}')
            memberships = interest_rate_fuzzification(input_value)
            for label, value in memberships.items():
                if value > 0:
                    ax.plot(input_value, value, 'ko')  # Black dot
                    ax.text(input_value, value, f' {label}: {value:.2f}', fontsize=10, verticalalignment='bottom')

        ax.set_xlabel('Interest Rate (%)', fontsize=12)
        ax.set_ylabel('Membership Degree', fontsize=12)
        ax.set_title('Interest Rate Fuzzification', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 1.1)
        
        if show_plot:
            plt.tight_layout()
            plt.show()
    
    def plot_application_salary_fuzzification(self, input_value=None, ax=None):
        """Plot the fuzzification of application salary with all membership functions."""
        from fuzzification import application_salary_fuzzification
        
        x_values = np.linspace(0, 100000, 1000)
        low = [application_salary_fuzzification(x)['Low'] for x in x_values]
        medium = [application_salary_fuzzification(x)['Medium'] for x in x_values]
        high = [application_salary_fuzzification(x)['High'] for x in x_values]
        very_high = [application_salary_fuzzification(x)['Very High'] for x in x_values]
        
        if ax is None:
            plt.figure(figsize=self.figsize)
            ax = plt.gca()
            show_plot = True
        else:
            show_plot = False

        ax.plot(x_values, low, label='Low', linewidth=2, color='blue')
        ax.plot(x_values, medium, label='Medium', linewidth=2, color='green')
        ax.plot(x_values, high, label='High', linewidth=2, color='orange')
        ax.plot(x_values, very_high, label='Very High', linewidth=2, color='red')
        
        ax.fill_between(x_values, low, color='blue', alpha=0.4)
        ax.fill_between(x_values, medium, color='green', alpha=0.4)
        ax.fill_between(x_values, high, color='orange', alpha=0.4)
        ax.fill_between(x_values, very_high, color='red', alpha=0.4)

        if input_value is not None:
            ax.axvline(x=input_value, color='black', linestyle='--', linewidth=1.5, label=f'Input: {input_value}')
            memberships = application_salary_fuzzification(input_value)
            for label, value in memberships.items():
                if value > 0:
                    ax.plot(input_value, value, 'ko')
                    ax.text(input_value, value, f' {label}: {value:.2f}', fontsize=10, verticalalignment='bottom')

        ax.set_xlabel('Salary ($)', fontsize=12)
        ax.set_ylabel('Membership Degree', fontsize=12)
        ax.set_title('Application Salary Fuzzification', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 110000)
        ax.set_ylim(0, 1.1)
        
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        if show_plot:
            plt.tight_layout()
            plt.show()

    def plot_application_assets_fuzzification(self, input_value=None, ax=None):
        """Plot the fuzzification of application assets with all membership functions."""
        from fuzzification import application_assets_fuzzification
        
        x_values = np.linspace(0, 1000000, 1000)
        low = [application_assets_fuzzification(x)['Low'] for x in x_values]
        medium = [application_assets_fuzzification(x)['Medium'] for x in x_values]
        high = [application_assets_fuzzification(x)['High'] for x in x_values]
        
        if ax is None:
            plt.figure(figsize=self.figsize)
            ax = plt.gca()
            show_plot = True
        else:
            show_plot = False

        ax.plot(x_values, low, label='Low', linewidth=2, color='blue')
        ax.plot(x_values, medium, label='Medium', linewidth=2, color='green')
        ax.plot(x_values, high, label='High', linewidth=2, color='orange')
        
        ax.fill_between(x_values, low, color='blue', alpha=0.4)
        ax.fill_between(x_values, medium, color='green', alpha=0.4)
        ax.fill_between(x_values, high, color='orange', alpha=0.4)

        if input_value is not None:
            ax.axvline(x=input_value, color='black', linestyle='--', linewidth=1.5, label=f'Input: {input_value}')
            memberships = application_assets_fuzzification(input_value)
            for label, value in memberships.items():
                if value > 0:
                    ax.plot(input_value, value, 'ko')
                    ax.text(input_value, value, f' {label}: {value:.2f}', fontsize=10, verticalalignment='bottom')

        ax.set_xlabel('Application Assets ($)', fontsize=12)
        ax.set_ylabel('Membership Degree', fontsize=12)
        ax.set_title('Application Assets Fuzzification', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1100000)
        ax.set_ylim(0, 1.1)
        
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        if show_plot:
            plt.tight_layout()
            plt.show()

    def plot_market_value_fuzzification(self, input_value=None, ax=None):
        """Plot the fuzzification of house market values with all membership functions."""
        from fuzzification import market_value_house_fuzzification
        
        x_values = np.linspace(0, 1000000, 1000)
        low = [market_value_house_fuzzification(x)['Low'] for x in x_values]
        medium = [market_value_house_fuzzification(x)['Medium'] for x in x_values]
        high = [market_value_house_fuzzification(x)['High'] for x in x_values]
        very_high = [market_value_house_fuzzification(x)['Very High'] for x in x_values]
        
        if ax is None:
            plt.figure(figsize=self.figsize)
            ax = plt.gca()
            show_plot = True
        else:
            show_plot = False

        ax.plot(x_values, low, label='Low', linewidth=2, color='blue')
        ax.plot(x_values, medium, label='Medium', linewidth=2, color='green')
        ax.plot(x_values, high, label='High', linewidth=2, color='orange')
        ax.plot(x_values, very_high, label='Very High', linewidth=2, color='red')
        
        ax.fill_between(x_values, low, color='blue', alpha=0.4)
        ax.fill_between(x_values, medium, color='green', alpha=0.4)
        ax.fill_between(x_values, high, color='orange', alpha=0.4)
        ax.fill_between(x_values, very_high, color='red', alpha=0.4)

        if input_value is not None:
            ax.axvline(x=input_value, color='black', linestyle='--', linewidth=1.5, label=f'Input: {input_value}')
            memberships = market_value_house_fuzzification(input_value)
            for label, value in memberships.items():
                if value > 0:
                    ax.plot(input_value, value, 'ko')
                    ax.text(input_value, value, f' {label}: {value:.2f}', fontsize=10, verticalalignment='bottom')

        ax.set_xlabel('Market Value ($)', fontsize=12)
        ax.set_ylabel('Membership Degree', fontsize=12)
        ax.set_title('House Market Value Fuzzification', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1000000)
        ax.set_ylim(0, 1.1)
        
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
        
        if show_plot:
            plt.tight_layout()
            plt.show()

    def plot_location_fuzzification(self, input_value=None, ax=None):
        """Plot the fuzzification of house location with all membership functions."""
        from fuzzification import location_of_house_fuzzification
        
        x_values = np.linspace(0, 10, 1000)
        bad = [location_of_house_fuzzification(x)['Bad'] for x in x_values]
        fair = [location_of_house_fuzzification(x)['Fair'] for x in x_values]
        excellent = [location_of_house_fuzzification(x)['Excellent'] for x in x_values]
        
        if ax is None:
            plt.figure(figsize=self.figsize)
            ax = plt.gca()
            show_plot = True
        else:
            show_plot = False

        ax.plot(x_values, bad, label='Bad', linewidth=2, color='red')
        ax.plot(x_values, fair, label='Fair', linewidth=2, color='yellow')
        ax.plot(x_values, excellent, label='Excellent', linewidth=2, color='green')

        ax.fill_between(x_values, bad, color='red', alpha=0.4)
        ax.fill_between(x_values, fair, color='yellow', alpha=0.4)
        ax.fill_between(x_values, excellent, color='green', alpha=0.4)

        if input_value is not None:
            ax.axvline(x=input_value, color='black', linestyle='--', linewidth=1.5, label=f'Input: {input_value}')
            memberships = location_of_house_fuzzification(input_value)
            for label, value in memberships.items():
                if value > 0:
                    ax.plot(input_value, value, 'ko')
                    ax.text(input_value, value, f' {label}: {value:.2f}', fontsize=10, verticalalignment='bottom')

        ax.set_xlabel('Location Score', fontsize=12)
        ax.set_ylabel('Membership Degree', fontsize=12)
        ax.set_title('House Location Fuzzification', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 1.1)
        
        if show_plot:
            plt.tight_layout()
            plt.show()

    def plot_all_inputs(self, inputs):
        """
        Plot all input fuzzification graphs in a single window.
        inputs: dict containing values for 'market_house', 'location_house', 
                'application_assets', 'application_salary', 'interest_rate'
        """
        fig, axes = plt.subplots(3, 2, figsize=(16, 12))
        axes = axes.flatten()
        
        self.plot_market_value_fuzzification(inputs.get('market_house'), ax=axes[0])
        self.plot_location_fuzzification(inputs.get('location_house'), ax=axes[1])
        self.plot_application_assets_fuzzification(inputs.get('application_assets'), ax=axes[2])
        self.plot_application_salary_fuzzification(inputs.get('application_salary'), ax=axes[3])
        self.plot_interest_rate_fuzzification(inputs.get('interest_rate'), ax=axes[4])
        
        # Hide the last empty subplot
        axes[5].axis('off')
        
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
