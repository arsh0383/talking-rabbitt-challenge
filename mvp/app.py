import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Talking Rabbitt", page_icon="🐰", layout="centered")

def analyze_and_plot(df, question):
    question = question.lower()
    
    # Logic 1: Highest revenue region
    if "region" in question and ("highest" in question or "most" in question or "top" in question):
        grouped = df.groupby('Region')['Revenue'].sum().reset_index()
        top_region = grouped.loc[grouped['Revenue'].idxmax()]
        
        answer = f"{top_region['Region']} region generated the highest revenue with ${top_region['Revenue']:,.0f}."
        
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(grouped['Region'], grouped['Revenue'], color='#3498db')
        ax.set_title('Total Revenue by Region', fontsize=14, fontweight='bold')
        ax.set_ylabel('Revenue ($)')
        ax.set_xlabel('Region')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Add values on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'${height:,.0f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
        
        return answer, fig
        
    # Logic 2: Revenue trend by month
    elif "trend" in question or ("revenue" in question and "month" in question):
        # Assuming Data might not be chronologically ordered strings, we map them
        month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
                     'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        
        # Group by month
        grouped = df.groupby('Month')['Revenue'].sum().reset_index()
        
        # Sort if it's month names
        if grouped['Month'].isin(month_map.keys()).any():
            grouped['MonthNum'] = grouped['Month'].map(month_map)
            grouped = grouped.sort_values('MonthNum')
            
        answer = "Here is the revenue trend grouped by month."
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(grouped['Month'], grouped['Revenue'], marker='o', linestyle='-', color='#e74c3c', linewidth=2)
        ax.set_title('Revenue Trend by Month', fontsize=14, fontweight='bold')
        ax.set_ylabel('Revenue ($)')
        ax.set_xlabel('Month')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Add labels
        for i, txt in enumerate(grouped['Revenue']):
            ax.annotate(f'${txt:,.0f}', (grouped['Month'].iloc[i], grouped['Revenue'].iloc[i]),
                        textcoords="offset points", xytext=(0,10), ha='center')

        return answer, fig

    # Logic 3: Highest revenue product
    elif "product" in question and ("most" in question or "highest" in question or "top" in question):
        grouped = df.groupby('Product')['Revenue'].sum().reset_index()
        top_product = grouped.loc[grouped['Revenue'].idxmax()]
        
        answer = f"{top_product['Product']} generated the most revenue with ${top_product['Revenue']:,.0f}."
        
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(grouped['Product'], grouped['Revenue'], color='#2ecc71')
        ax.set_title('Total Revenue by Product', fontsize=14, fontweight='bold')
        ax.set_ylabel('Revenue ($)')
        ax.set_xlabel('Product')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'${height:,.0f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
            
        return answer, fig
        
    else:
        return "I'm sorry, I didn't quite understand that question. Try asking about the highest revenue by region, top product, or revenue trend by month.", None

# Main Application UI
def main():
    st.title("Talking Rabbitt 🐰 – Conversational Business Intelligence")
    
    st.markdown("""
    Welcome to **Talking Rabbitt**! Upload your sales data and just ask questions to instantly get insights and charts. No dashboard required.
    """)
    
    uploaded_file = st.file_uploader("Upload your CSV sales data", type=['csv'])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
            st.markdown("---")
            st.subheader("Talk to your data")
            
            question = st.text_input("Ask a question about your data:", 
                                     placeholder="e.g. Which region generated the highest revenue?")
            
            if st.button("Ask Rabbitt 🐰"):
                if question:
                    with st.spinner("Analyzing data..."):
                        # Process question
                        answer, fig = analyze_and_plot(df, question)
                        
                        # Display Results
                        st.success(answer)
                        
                        if fig:
                            st.pyplot(fig)
                else:
                    st.warning("Please enter a question to ask Rabbitt.")
                    
        except Exception as e:
            st.error(f"Error reading file or analyzing data: {e}")

if __name__ == "__main__":
    main()
