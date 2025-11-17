import numpy as np
from membership_function import trapezoidal_membership, triangle_membership


class Defuzzifier:
    """
    Farklı çıktı tipleri için defuzzification işlemi yapar.
    """
    
    def __init__(self):
        # Her çıktı tipi için membership fonksiyonları ve aralıkları tanımla
        self.output_configs = {
            'credit': {
                'range': (0, 1000),
                'functions': {
                    'Very_low': lambda val: trapezoidal_membership(val, 0, 0, 100, 200),
                    'Low': lambda val: triangle_membership(val, 100, 250, 400),
                    'Medium': lambda val: triangle_membership(val, 300, 500, 700),
                    'High': lambda val: triangle_membership(val, 600, 750, 900),
                    'Very_high': lambda val: trapezoidal_membership(val, 800, 900, 1000, 1000)
                }
            },
            'house': {
                'range': (0, 10),
                'functions': {
                    'Very_low': lambda val: trapezoidal_membership(val, 0, 0, 1, 3),
                    'Low': lambda val: triangle_membership(val, 1, 3, 5),
                    'Medium': lambda val: triangle_membership(val, 3, 5, 7),
                    'High': lambda val: triangle_membership(val, 5, 7, 9),
                    'Very_high': lambda val: trapezoidal_membership(val, 7, 9, 10, 10)
                }
            },
            'application': {
                'range': (0, 10),
                'functions': {
                    'Low': lambda val: trapezoidal_membership(val, 0, 0, 2, 4),
                    'Medium': lambda val: triangle_membership(val, 2, 5, 8),
                    'High': lambda val: trapezoidal_membership(val, 6, 8, 10, 10)
                }
            }
        }
    
    def centroid_defuzzification(self, fuzzy_output, output_type='credit'):
        """
        Centroid yöntemi ile bulanık çıktıyı kesin değere çevirir.
        
        Args:
            fuzzy_output (dict): {'Very_low': 0.2, 'Low': 0.5, ...}
            output_type (str): 'credit', 'house', veya 'application'
        
        Returns:
            float: Kesin çıktı değeri
        """
        
        if output_type not in self.output_configs:
            raise ValueError(f"Geçersiz output_type: {output_type}")
        
        config = self.output_configs[output_type]
        output_range = config['range']
        membership_functions = config['functions']
        
        # X ekseni için değerler oluştur
        x = np.linspace(output_range[0], output_range[1], 1000)
        
        # Toplam membership'i başlat
        aggregated = np.zeros(len(x))
        
        # Her kategori için işlem yap
        for category, strength in fuzzy_output.items():
            if strength > 0 and category in membership_functions:
                # Membership değerlerini hesapla
                membership_values = np.array([membership_functions[category](xi) for xi in x])
                
                # CLIPPING
                clipped = np.minimum(membership_values, strength)
                
                # AGGREGATION
                aggregated = np.maximum(aggregated, clipped)
        
        # Centroid hesapla
        numerator = np.sum(x * aggregated)
        denominator = np.sum(aggregated)
        
        if denominator == 0:
            return (output_range[0] + output_range[1]) / 2
        
        crisp_output = numerator / denominator
        return crisp_output
    
    def visualize_defuzzification(self, fuzzy_output, output_type='credit'):
        """
        Defuzzification sürecini görselleştirir
        """
        import matplotlib.pyplot as plt
        
        if output_type not in self.output_configs:
            raise ValueError(f"Geçersiz output_type: {output_type}")
        
        config = self.output_configs[output_type]
        output_range = config['range']
        membership_functions = config['functions']
        
        x = np.linspace(output_range[0], output_range[1], 1000)
        
        plt.figure(figsize=(14, 8))
        
        # Renk paleti
        colors = {
            'Very_low': 'blue', 'Low': 'cyan', 'Medium': 'green', 
            'High': 'orange', 'Very_high': 'red'
        }
        
        # 1. Orijinal membership fonksiyonlarını çiz
        for category, func in membership_functions.items():
            membership_vals = [func(xi) for xi in x]
            color = colors.get(category, 'gray')
            plt.plot(x, membership_vals, '--', color=color, 
                    alpha=0.3, label=f'{category} (original)')
        
        # 2. Clipped membership fonksiyonlarını çiz
        aggregated = np.zeros(len(x))
        
        for category, strength in fuzzy_output.items():
            if strength > 0 and category in membership_functions:
                membership_vals = np.array([membership_functions[category](xi) for xi in x])
                clipped = np.minimum(membership_vals, strength)
                color = colors.get(category, 'gray')
                plt.fill_between(x, clipped, alpha=0.4, color=color,
                               label=f'{category} = {strength:.2f}')
                aggregated = np.maximum(aggregated, clipped)
        
        # 3. Aggregate sonucu çiz
        plt.plot(x, aggregated, 'k-', linewidth=2, label='Aggregated Output')
        plt.fill_between(x, aggregated, alpha=0.2, color='black')
        
        # 4. Centroid'i hesapla ve işaretle
        centroid = self.centroid_defuzzification(fuzzy_output, output_type)
        plt.axvline(centroid, color='red', linestyle='--', linewidth=2, 
                    label=f'Centroid = {centroid:.2f}')
        
        # Başlıklar
        if output_type == 'credit':
            xlabel, title = 'Credit Score', 'Credit Evaluation - Defuzzification'
        elif output_type == 'house':
            xlabel, title = 'House Score', 'House Evaluation - Defuzzification'
        else:
            xlabel, title = 'Application Score', 'Application Evaluation - Defuzzification'
        
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel('Membership Degree', fontsize=12)
        plt.title(title, fontsize=14, fontweight='bold')
        plt.legend(loc='upper right', fontsize=9)
        plt.grid(True, alpha=0.3)
        plt.xlim(output_range)
        plt.ylim(0, 1.1)
        
        plt.tight_layout()
        plt.show()
        
        return centroid


# --- TEST ---
if __name__ == "__main__":
    defuzz = Defuzzifier()
    
    print("="*60)
    print("TEST 1: CREDIT DEFUZZIFICATION")
    print("="*60)
    
    fuzzy_credit = {
        'Very_low': 0.0,
        'Low': 0.3,
        'Medium': 0.8,
        'High': 0.5,
        'Very_high': 0.1
    }
    
    print("Bulanık Çıktı:", fuzzy_credit)
    crisp_score = defuzz.centroid_defuzzification(fuzzy_credit, 'credit')
    print(f"Kesin Kredi Skoru: {crisp_score:.2f}/1000\n")
    defuzz.visualize_defuzzification(fuzzy_credit, 'credit')
    
    print("="*60)
    print("TEST 2: HOUSE DEFUZZIFICATION")
    print("="*60)
    
    fuzzy_house = {
        'Very_low': 0.1,
        'Low': 0.5,
        'Medium': 0.8,
        'High': 0.4,
        'Very_high': 0.2
    }
    
    print("Bulanık Çıktı:", fuzzy_house)
    house_score = defuzz.centroid_defuzzification(fuzzy_house, 'house')
    print(f"Kesin Ev Skoru: {house_score:.2f}/10\n")
    defuzz.visualize_defuzzification(fuzzy_house, 'house')
    
    print("="*60)
    print("TEST 3: APPLICATION DEFUZZIFICATION")
    print("="*60)
    
    fuzzy_application = {
        'Low': 0.2,
        'Medium': 0.7,
        'High': 0.6
    }
    
    print("Bulanık Çıktı:", fuzzy_application)
    app_score = defuzz.centroid_defuzzification(fuzzy_application, 'application')
    print(f"Kesin Başvuran Skoru: {app_score:.2f}/10\n")
    defuzz.visualize_defuzzification(fuzzy_application, 'application')