# Talking Rabbitt 🐰 – Conversational Business Intelligence

## Project Overview
Talking Rabbitt is a conversational intelligence layer that allows users to talk directly to their business data. The system takes datasets and allows users to ask natural language questions, immediately returning a concise text answer and an automated visualization tailored to their query.

## Product Vision
To replace "dashboard fatigue" by creating an intelligent interface where exploring data is as easy as having a chat. We want to empower everyone, from operators to executives, to analyze data freely without needing to learn complex BI tools like PowerBI or Tableau.

## Installation Instructions

1. Make sure you have Python 3.8+ installed.
2. Clone or download this project folder.
3. Navigate into the `mvp` directory:
   ```bash
   cd mvp
   ```
4. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the MVP

To launch the Talking Rabbitt MVP, simply run:
```bash
streamlit run app.py
```

This will automatically open the Streamlit web application in your browser.

## Example Questions to Ask
Once you upload the `sample_sales.csv`, try asking the following questions to the system:
- "Which region had the highest revenue?"
- "Show revenue trend by month"
- "Which product generated the most revenue?"

## The "Magic Moment"
The magic moment happens when a user uploads their Excel/CSV data and, instead of fighting with pivot tables or building manual charts, they just type their question and instantly see the exact chart they need—proving the value of seamless conversational analytics.
