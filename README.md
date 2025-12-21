# Fuzzy Logic Project

A simple fuzzy logic system with membership functions, fuzzification, rule-based inference, and defuzzification. Includes a Tkinter GUI to interactively input values and visualize membership functions using Matplotlib.

## Features
- Membership functions: triangular and trapezoidal
- Fuzzification of inputs into linguistic sets
- Rule-based inference for multiple domains (application, house, loan)
- Defuzzification (e.g., centroid) to produce crisp outputs
- Interactive GUI built with Tkinter + Matplotlib embedding
- Plotting utilities for membership functions

## Requirements
- Python 3.9+ (includes Tkinter on most installations)
- See `requirements.txt` for Python packages

Install dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage
Run the GUI application:

```powershell
python main.py
```

This opens the Tkinter window where you can:
- Enter input values
- Select rules to evaluate
- Visualize membership functions and resulting outputs

## Project Structure
- [membership_function.py](membership_function.py): Core triangular and trapezoidal membership functions
- [fuzzification.py](fuzzification.py): Converts crisp inputs to fuzzy sets; uses `FuzzificationPlotter`
- [inference.py](inference.py): Rule evaluation functions for different domains
- [defuzzification.py](defuzzification.py): Methods to convert fuzzy results back to crisp values
- [plotting_mf.py](plotting_mf.py): Plotting helper (`FuzzificationPlotter`) using Matplotlib
- [main.py](main.py): Tkinter GUI entry point; embeds Matplotlib via `FigureCanvasTkAgg`

## Notes
- `tkinter` and `tk` come with standard Python on Windows. If you encounter errors related to Tk, ensure your Python installation includes Tcl/Tk.
- If running in environments without a display (e.g., remote servers), plotting and the GUI may not function.

## License
This project is for educational purposes. Add a license if you plan to distribute.