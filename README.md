# Control System Design Tool

An interactive web application for control system analysis and design, built with Streamlit and Python Control Systems Library.

## Features

- **Interactive Parameter Tuning**: Adjust system parameters and controller gains in real-time
- **Multiple Controller Types**:
  - Proportional (P)
  - Proportional-Integral (PI)
  - Lead Compensator (Avance de phase)
- **Comprehensive Visualizations**:
  - Nichols Plot (Open-Loop)
  - Bode Plot (Closed-Loop)
  - Step Response (Closed-Loop)
- **Responsive Design**: Wide layout with full-width interactive plots

## Demo

[Live Demo on Streamlit Cloud](#)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:

```bash
git clone https://github.com/vincentchoqueuse/control_design_app.git
cd controler
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the application locally:

```bash
streamlit run control_design_app.py
```

The app will open in your default web browser at `http://localhost:8501`

## How to Use

1. **Define Your Plant**: Enter the numerator and denominator coefficients of your transfer function in the sidebar
2. **Select Controller**: Choose from P, PI, or Lead Compensator
3. **Tune Parameters**: Adjust controller gains (Kp, Ki, K, α, T) to achieve desired performance
4. **Analyze Results**: View real-time updates of:
   - Nichols chart showing stability margins
   - Bode plots showing frequency response
   - Step response showing time-domain behavior

## Project Structure

```
controler/
├── control_design_app.py   # Main Streamlit application
├── plots.py                 # Plot generation functions
├── figures.py               # Figure classes for different plot types
├── grid.py                  # Grid generation for Nichols and root locus
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Dependencies

- `streamlit` - Web application framework
- `control` - Python Control Systems Library
- `numpy` - Numerical computing
- `matplotlib` - Plotting library
- `plotly` - Interactive plotting

See `requirements.txt` for complete list with versions.

## Examples

### Example 1: Second-Order System with P Controller

**Plant**: `G(s) = 1 / (s² + 2s + 1)`

- Numerator: `1`
- Denominator: `1, 2, 1`

**Controller**: Proportional (P)

- Kp: `2.0`

### Example 2: Type-0 System with PI Controller

**Plant**: `G(s) = 1 / (s + 1)`

- Numerator: `1`
- Denominator: `1, 1`

**Controller**: PI

- Kp: `1.0`
- Ki: `0.5`

## Authors

- **Vincent Choqueuse**
- **Emmanuel Delaleau**

_ENIB - École Nationale d'Ingénieurs de Brest_

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with the Python Control Systems Library
- Powered by Streamlit
- Interactive plots using Plotly
