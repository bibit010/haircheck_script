import pandas as pd
import os
from openpyxl.styles import PatternFill

def process_haircheck_data(input_csv, output_excel):
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Remove 'Reporting starts' and 'Reporting ends' columns
    df = df.drop(columns=['Reporting starts', 'Reporting ends'], errors='ignore')
    
    # Define campaign categories
    website_campaigns = [
        "NL / Lead / CBO / Kyiv Odesa / 26.07.2024",
        "SITE / Cold / ABO / Lead / 29.05.2024",
        "SITE / NLAS / Warm / ABO / 12.02.2024"
    ]
    instagram_facebook_campaigns = [
        "INST / Engagement / COLD - 22.05.2024",
        "INST / Engagement Messages / WARM - 20.05.2024",
        "NL / Fb Lead Form / Ugly hair / Lookalike (UA, 1%) - LTV ALL/ 26/08/2024 Campaign",
        "NL / TRAFF / Inst / 24.07.2024",
        "NL / Tailored leads campaign / Lookalike (UA, 1%) - LTV ALL/ 15/07/2024 Campaign"
    ]
    
    # Categorize campaigns
    df['Category'] = df['Campaign name'].apply(lambda x: 'Website' if x in website_campaigns else 
                                               ('Instagram&Facebook' if x in instagram_facebook_campaigns else 'Other'))
    
    # Group by Day and Category, then aggregate
    grouped = df.groupby(['Day', 'Category']).agg({
        'Amount spent (USD)': 'sum',
        'Link clicks': 'sum',
        'Leads': 'sum',
        'Messaging conversations started': 'sum'
    }).reset_index()
    
    # Pivot the data for easier processing
    pivoted = grouped.pivot(index='Day', columns='Category', values=['Amount spent (USD)', 'Link clicks', 'Leads', 'Messaging conversations started'])
    pivoted.columns = [f"{col[1]}_{col[0]}" for col in pivoted.columns]
    pivoted = pivoted.reset_index()
    
    # Calculate total impressions for Instagram&Facebook
    pivoted['Instagram&Facebook_Total_Impressions'] = (
        pivoted['Website_Messaging conversations started'].fillna(0) +
        pivoted['Instagram&Facebook_Messaging conversations started'].fillna(0) +
        pivoted['Instagram&Facebook_Leads'].fillna(0)
    )
    
    # Prepare final dataframe with reorganized columns
    final_df = pd.DataFrame({
        'Day': pivoted['Day'],
        'Instagram&Facebook_Amount_Spent': pivoted['Instagram&Facebook_Amount spent (USD)'],
        'Instagram&Facebook_Link_Clicks': pivoted['Instagram&Facebook_Link clicks'],
        'Instagram&Facebook_Leads': pivoted['Instagram&Facebook_Leads'],
        'Instagram&Facebook_Messaging_Conversations_Started': pivoted['Instagram&Facebook_Messaging conversations started'],
        'Website_Messaging_Conversations_Started': pivoted['Website_Messaging conversations started'],
        'Instagram&Facebook_Total_Impressions': pivoted['Instagram&Facebook_Total_Impressions'],
        'Website_Amount_Spent': pivoted['Website_Amount spent (USD)'],
        'Website_Link_Clicks': pivoted['Website_Link clicks'],
        'Website_Leads': pivoted['Website_Leads']
    })
    
    # Replace NaN with 'N/A'
    final_df = final_df.fillna('N/A')
    
    # Write to Excel
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        final_df.to_excel(writer, index=False, sheet_name='Haircheck Report')
        
        # Get the workbook and the worksheet
        workbook = writer.book
        worksheet = writer.sheets['Haircheck Report']
        
        # Define fill colors
        yellow_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
        blue_fill = PatternFill(start_color="ADD8E6", end_color="ADD8E6", fill_type="solid")
        
        # Apply yellow fill to specified columns
        yellow_columns = ['B', 'C', 'D', 'E', 'F', 'G']
        for col in yellow_columns:
            for cell in worksheet[col]:
                cell.fill = yellow_fill
        
        # Apply blue fill to specified columns
        blue_columns = ['H', 'I', 'J']
        for col in blue_columns:
            for cell in worksheet[col]:
                cell.fill = blue_fill
        
        # Auto-adjust column widths
        for idx, col in enumerate(final_df.columns):
            max_length = max(final_df[col].astype(str).map(len).max(), len(col))
            worksheet.column_dimensions[worksheet.cell(row=1, column=idx+1).column_letter].width = max_length + 2

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "Haircheck-template-22-sep-28-sep.csv")
    output_excel = os.path.join(script_dir, "Haircheck_Report.xlsx")
    
    process_haircheck_data(input_csv, output_excel)
    print(f"Excel report has been generated: {output_excel}")