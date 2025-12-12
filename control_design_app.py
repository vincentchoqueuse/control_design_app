import streamlit as st
import control as ct
import numpy as np
import matplotlib.pyplot as plt
from plots import nichols, bode, step

# Configure page
st.set_page_config(page_title="Control System Design", layout="wide")
st.title("Control System Design Tool")


# Sidebar for parameters
# School logo
logo_path = "https://upload.wikimedia.org/wikipedia/commons/c/ca/Enib_inp_2025.png"  # Place your school logo file here
try:
    st.sidebar.image(logo_path, width=100)
except:
    st.sidebar.markdown("**[School Logo]**")  # Placeholder if logo file not found

st.sidebar.header("System Parameters")

# System transfer function parameters
st.sidebar.subheader("Plant Transfer Function")

# Default values for a simple system
default_b = [1]
default_a = [1, 2, 1]

# Input for numerator coefficients
b_input = st.sidebar.text_input(
    "Numerator coefficients (b) - comma separated",
    value=",".join(map(str, default_b)),
    help="Enter coefficients from highest to lowest degree"
)

# Input for denominator coefficients
a_input = st.sidebar.text_input(
    "Denominator coefficients (a) - comma separated",
    value=",".join(map(str, default_a)),
    help="Enter coefficients from highest to lowest degree"
)

# Parse coefficients
try:
    b = [float(x.strip()) for x in b_input.split(',')]
    a = [float(x.strip()) for x in a_input.split(',')]
    G = ct.TransferFunction(b, a)
except:
    st.sidebar.error("Invalid coefficients. Please enter comma-separated numbers.")
    st.stop()

# Controller selection
st.sidebar.header("Controller Parameters")
controller_type = st.sidebar.selectbox(
    "Controller Type",
    ["P", "PI", "Avance de phase"]
)

# Controller parameters based on type
if controller_type == "P":
    Kp = st.sidebar.number_input("Kp (Proportional Gain)", min_value=0.0, value=1.0, step=0.001, format="%.3f")
    C = ct.TransferFunction([Kp], [1])

elif controller_type == "PI":
    Kp = st.sidebar.number_input("Kp (Proportional Gain)", min_value=0.0, value=1.0, step=0.001, format="%.3f")
    Ki = st.sidebar.number_input("Ki (Integral Gain)", min_value=0.0, value=1.0, step=0.001, format="%.3f")
    C = ct.TransferFunction([Kp, Ki], [1, 0])

else:  # Avance de phase (Lead)
    K = st.sidebar.number_input("K (Gain)", min_value=0.0, value=1.0, step=0.001, format="%.3f")
    alpha = st.sidebar.number_input("α (alpha)", min_value=0.001, max_value=0.99, value=0.5, step=0.001, format="%.3f",
                                    help="alpha < 1 for lead compensator")
    T = st.sidebar.number_input("T (time constant)", min_value=0.0, value=1.0, step=0.001, format="%.3f")
    # Lead compensator: C(s) = K * (1 + T*s) / (1 + alpha*T*s)
    C = ct.TransferFunction([K*T, K], [alpha*T, 1])

# Frequency range parameters
st.sidebar.header("Frequency Range")
omega_min = st.sidebar.number_input(
    "ω min (rad/s)",
    min_value=0.001,
    value=0.01,
    step=0.001,
    format="%.3f",
    help="Minimum frequency for frequency response plots"
)
omega_max = st.sidebar.number_input(
    "ω max (rad/s)",
    min_value=0.01,
    value=100.0,
    step=1.0,
    help="Maximum frequency for frequency response plots"
)

# Generate frequency vector
w = np.logspace(np.log10(omega_min), np.log10(omega_max), 500)

# Calculate open-loop and closed-loop systems
L = C * G  # Open-loop transfer function
try:
    T_cl = ct.feedback(L, 1)  # Closed-loop transfer function
except:
    st.error("Unable to compute closed-loop system. Check system stability.")
    st.stop()

# Create tabs for different plots
tab1, tab2, tab3 = st.tabs(["Nichols Plot (Open-Loop)", "Bode Plot (Closed-Loop)", "Step Response (Closed-Loop)"])

# Tab 1: Black-Nichols plot (open-loop)
with tab1:
    try:
        fig1 = nichols(L, w=w)
        st.plotly_chart(fig1, width="stretch", height=600, theme=None)
    except Exception as e:
        st.error(f"Error generating Nichols plot: {str(e)}")

# Tab 2: Bode plot (closed-loop)
with tab2:
    try:
        fig2 = bode(T_cl, w=w)
        st.plotly_chart(fig2, width="stretch", height=600, theme=None)
    except Exception as e:
        st.error(f"Error generating Bode plot: {str(e)}")

# Tab 3: Step response (closed-loop)
with tab3:
    try:
        fig3 = step(T_cl)
        st.plotly_chart(fig3, width="stretch", height=600, theme=None)
    except Exception as e:
        st.error(f"Error generating step response: {str(e)}")

# Authors section at bottom of sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("**Authors:**")
st.sidebar.markdown("Vincent Choqueuse")
st.sidebar.markdown("Emmanuel Delaleau")

