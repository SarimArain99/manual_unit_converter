import streamlit as st

conversion_factors = {
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Nautical Miles": 0.000539957,
    },
    "Weight": {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1e6,
        "Pounds": 2.20462,
        "Ounces": 35.274,
        "Stones": 0.157473,
    },
    "Digital Storage": {
        "Bytes": 1,
        "Kilobytes": 1 / 1024,
        "Megabytes": 1 / (1024**2),
        "Gigabytes": 1 / (1024**3),
        "Terabytes": 1 / (1024**4),
        "Petabytes": 1 / (1024**5),
        "Bits": 8,
    },
    "Speed": {
        "Meters per second": 1,
        "Kilometers per hour": 3.6,
        "Miles per hour": 2.23694,
        "Feet per second": 3.28084,
        "Knots": 1.94384,
    },
    "Acceleration": {
        "Meters per second squared": 1,
        "Feet per second squared": 3.28084,
        "G-force": 0.101972,
    },
    "Volume": {
        "Liters": 1,
        "Milliliters": 1000,
        "Cubic meters": 0.001,
        "Cubic centimeters": 1000,
        "Cubic inches": 61.0237,
        "Cubic feet": 0.0353147,
        "Gallons (US)": 0.264172,
        "Pints (US)": 2.11338,
    },
    "Area": {
        "Square meters": 1,
        "Square kilometers": 0.000001,
        "Square centimeters": 10000,
        "Square millimeters": 1e6,
        "Square inches": 1550,
        "Square feet": 10.7639,
        "Acres": 0.000247105,
        "Hectares": 0.0001,
    },
    "Density": {
        "Kilograms per cubic meter": 1,
        "Grams per cubic centimeter": 0.001,
        "Pounds per cubic inch": 3.61273e-5,
        "Pounds per cubic foot": 0.0624279,
    },
    "Energy": {
        "Joules": 1,
        "Kilojoules": 0.001,
        "Calories": 0.239006,
        "Kilocalories": 0.000239006,
        "Watt-hours": 0.000277778,
        "Kilowatt-hours": 2.77778e-7,
        "BTU": 0.000947817,
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 0.001,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9,
    },
    "Mass": {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1e6,
        "Micrograms": 1e9,
        "Metric Tons": 0.001,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    },
    "Pressure": {
        "Pascals": 1,
        "Kilopascals": 0.001,
        "Bars": 1e-5,
        "Atmospheres": 9.86923e-6,
        "Pounds per square inch": 0.000145038,
    },
    "Temperature": {
        "Celsius": 1,
        "Fahrenheit": lambda c: (c * 9 / 5) + 32,
        "Kelvin": lambda c: c + 273.15,
    },
    "Time": {
        "Seconds": 1,
        "Milliseconds": 1000,
        "Microseconds": 1e6,
        "Minutes": 1 / 60,
        "Hours": 1 / 3600,
        "Days": 1 / 86400,
        "Weeks": 1 / 604800,
        "Years": 1 / 31536000,
    },
}

st.markdown(
    """
    <style>
        
        .stApp {
            background:#b5bbc9;
            height: 100vh;
        }

        /* Centering the main content */
        .main-container {
            max-width: 600px;
            background: white;
            margin: auto;
            margin-top: 50px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }

        /* Title and subtitle */
        .title {
            color: #585e6c;
            font-size: 45px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 5px;
        }

        .subtitle {
            color: #585e6c;
            font-size: 1.1em;
            text-align: center;
            margin-bottom: 20px;
        }

        .stSelectbox, .stNumberInput {
            border-radius: 10px !important;
            border: 2px solid #585e6c !important;
            padding: 10px;
            font-size: 16px;
        }

        .stButton>button {
            background-color: #585e6c;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background-color: #585e6c;
            transform: scale(1.05);
            color:#b5bbc9;
        }

        /* Conversion result */
        .stSuccess {
            background-color: #b5bbc9;
            color: #585e6c;
            font-size: 18px;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.15);
        }
         label, .stSelectbox label, .stNumberInput label, .stTextInput label, .stRadio label {
            color: #585e6c !important;  /* Dark red */
            font-weight: bold !important;
            font-size: 16px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-container">', unsafe_allow_html=True)


st.markdown('<div class="title">Unit Converter</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Effortlessly meet all your unit conversion needs</p>',
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='subtitle'>Start converting now and simplify your calculations!</p>",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)


category = st.selectbox("Select Category", list(conversion_factors.keys()))
unitOptions = conversion_factors[category]

col1, col2 = st.columns(2)

with col1:
    inputOptions = st.selectbox("Select Current Unit", list(unitOptions.keys()))
with col2:
    outputOptions = st.selectbox("Select Output Unit", list(unitOptions.keys()))

userInput = st.number_input("Enter Value", min_value=0.0, format="%.2f")


if st.button("Convert"):
    if inputOptions and outputOptions:
        if category == "Temperature":
            if inputOptions == "Fahrenheit":
                valToCelsius = (userInput - 32) * 5 / 9
            elif inputOptions == "Kelvin":
                valToCelsius = userInput - 273.15
            else:
                valToCelsius = userInput

            if outputOptions == "Fahrenheit":
                converted_value = (valToCelsius * 9 / 5) + 32
            elif outputOptions == "Kelvin":
                converted_value = valToCelsius + 273.15
            else:
                converted_value = valToCelsius
        else:
            converted_value = (
                userInput / unitOptions[inputOptions] * unitOptions[outputOptions]
            )

        st.success(
            f"{userInput} {inputOptions} = {converted_value:.2f} {outputOptions}"
        )
