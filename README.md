# Vehicle Explorer (Streamlit)

A small Streamlit app to explore a vehicle dataset.

## What this does
- Loads a CSV into a Pandas DataFrame
- Shows a header
- Has a checkbox to filter data (e.g., price threshold)
- Draws a Plotly histogram and scatter plot

## How to run locally

**Prereqs**: Python 3.10+ and `pip`.

```bash
# create/activate your environment (example: conda)
conda create -n myenv python=3.10 -y
conda activate myenv

# install deps
pip install -r requirements.txt

# run
streamlit run app.py