# cashflow-analysis

An analysis for upcoming fresh graduates from certain study loan programme in MY to understand the possible financial situation according to their career choices.


## Dashboard

The interactive dashboard is deployed on Streamlit Cloud and can be accessed [here](https://study-loan-my.streamlit.app/).

## Data source

The data used in this analysis is based on various financial parameters and assumptions relevant to fresh graduates in Malaysia.

> [!NOTE]  
> For now, the initial years are set to 10 and the discount are set into 50% and 75%. 
> The Income converter are also currently implemented only for Germany.

## Project Structure

- `app.py`: Main entry point for the Streamlit application.
- `financial_planning.ipynb`: Jupyter notebook containing financial analysis and visualizations.
- `pages/1_loan.py`: Streamlit page for calculating study loan repayments.
- `pages/2_compounding.py`: Streamlit page for calculating investment growth.
- `pages/3_income.py`: Streamlit page for analyzing income and expenses.

## Requirements

The required Python packages are listed in `requirements.txt`:

```txt
streamlit==1.41.1
pandas==2.2.3
plotly==5.24.1
python-dotenv==1.0.1
```

## Installation

1. To install the project, clone the repository and navigate into the project directory:

```bash
git clone https://github.com/yourusername/cashflow-analysis.git
cd cashflow-analysis
```

2. Install the required packages
```bash
pip install -r requirements.txt
```

3. Run streamlit application
```bash
streamlit run app.py
```