import pandas as pd
import os
from openpyxl.styles import PatternFill
import sys

# Define campaign groups as variables for easy modification
instagram_facebook_campaigns = [
    "INST / Engagement / COLD - 22.05.2024",
    "INST / Engagement Messages / WARM - 20.05.2024",
    "NL / Fb Lead Form / Ugly hair / Lookalike (UA, 1%) - LTV ALL/ 26/08/2024  Campaign",
    "NL / TRAFF / Inst / 24.07.2024",
    "NL / Tailored leads campaign / Lookalike (UA, 1%) - LTV ALL/ 15/07/2024 Campaign",
    "NL / FB Lead Form / Hair transplant /K+O / M22-50 / Broad  18/10/2024   Campaign",
    "NL / FB Lead Form / Regenera 2 /K+O / M22-50 / Broad  24/10/2024   Campaign",
    "NL / Fb Lead Form / Ugly hair / Odesa / Lookalike (UA, 1%)  - LTV ALL/ 21/10/2024"
]

website_campaigns = [
    "NL / Lead  / CBO / Kyiv Odesa / 26.07.2024",
    "SITE / Cold / ABO / Lead / 29.05.2024",
    "SITE / NLAS / Warm / ABO / 12.02.2024"
]

def find_csv_file():
    """Find CSV file in current directory."""
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    if len(csv_files) == 0:
        print("Error: No CSV file found in the current directory")
        sys.exit(1)
    elif len(csv_files) > 1:
        print("Error: Multiple CSV files found in the directory. Please keep only one CSV file.")
        sys.exit(1)
    return csv_files[0]

def check_missing_campaigns(day_data):
    """Check for missing campaigns for a specific day."""
    present_campaigns = day_data['Campaign name'].unique()
    
    missing_ig_fb = [camp for camp in instagram_facebook_campaigns 
                    if camp not in present_campaigns]
    missing_website = [camp for camp in website_campaigns 
                      if camp not in present_campaigns]
    
    comments = []
    if missing_ig_fb:
        comments.append(f"Missing Instagram/Facebook campaigns: {', '.join(missing_ig_fb)}")
    if missing_website:
        comments.append(f"Missing Website campaigns: {', '.join(missing_website)}")
    
    return ' | '.join(comments) if comments else ''

def get_output_filename(df):
    """Determine the output filename based on the dates in the data."""
    try:
        dates = pd.to_datetime(df['Day'])
        unique_months = dates.dt.strftime('%B_%Y').unique()
        
        if len(unique_months) == 1:
            return f'campaign_report_{unique_months[0]}.xlsx'
        else:
            months_str = '_and_'.join(unique_months)
            return f'campaign_report_multiple_months_{months_str}.xlsx'
    except Exception as e:
        print(f"Warning: Could not process dates properly: {str(e)}")
        return 'campaign_report_unknown_date.xlsx'

def process_data(csv_file):
    """Process the CSV data and create the required metrics."""
    try:
        # Read CSV file
        print(f"Processing {csv_file}...")
        df = pd.read_csv(csv_file)
        
        # Initialize result dataframes
        results = []
        
        # Process data day by day
        for day in df['Day'].unique():
            day_data = df[df['Day'] == day]
            
            # Calculate metrics for Instagram & Facebook campaigns
            ig_fb_data = day_data[day_data['Campaign name'].isin(instagram_facebook_campaigns)]
            ig_fb_budget = ig_fb_data['Amount spent (USD)'].sum()
            ig_fb_target_leads = (
                ig_fb_data['Leads'].sum() +
                ig_fb_data['Messaging conversations started'].sum() +
                day_data[day_data['Campaign name'].isin(website_campaigns)]['Messaging conversations started'].sum()
            )
            
            # Calculate metrics for Website campaigns
            site_data = day_data[day_data['Campaign name'].isin(website_campaigns)]
            site_budget = site_data['Amount spent (USD)'].sum()
            site_link_clicks = site_data['Link clicks'].sum()
            site_leads = site_data['Leads'].sum()
            
            # Check for missing campaigns
            comments = check_missing_campaigns(day_data)
            
            results.append({
                'Date': pd.to_datetime(day),  # Convert to datetime for proper sorting
                'Ins&FB_Budget': ig_fb_budget,
                'Ins&FB_Target_leads': ig_fb_target_leads,
                'Site_Budget': site_budget,
                'Site_Link_Clicks': site_link_clicks,
                'Site_Leads': site_leads,
                'Lead Target': site_leads,
                'Comments': comments
            })
        
        # Convert to DataFrame and sort by date
        results_df = pd.DataFrame(results)
        results_df = results_df.sort_values('Date')
        
        # Convert date back to original format
        results_df['Date'] = results_df['Date'].dt.strftime('%d/%m/%Y')
        
        return results_df
    
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        sys.exit(1)

def export_to_excel(df, output_file):
    """Export the data to Excel with colored cells."""
    try:
        # Select columns for export
        columns = ['Date', 'Ins&FB_Budget', 'Ins&FB_Target_leads', 
                  'Site_Budget', 'Site_Link_Clicks', 'Site_Leads', 
                  'Lead Target', 'Comments']
        export_df = df[columns].copy()
        
        # Export to Excel
        writer = pd.ExcelWriter(output_file, engine='openpyxl')
        export_df.to_excel(writer, index=False, sheet_name='Sheet1')
        
        # Get the worksheet
        worksheet = writer.sheets['Sheet1']
        
        # Define fills
        yellow_fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
        green_fill = PatternFill(start_color='90EE90', end_color='90EE90', fill_type='solid')
        red_fill = PatternFill(start_color='FFB6C1', end_color='FFB6C1', fill_type='solid')
        
        # Apply colors
        for row in range(2, worksheet.max_row + 1):
            # Yellow for Ins&FB columns
            worksheet.cell(row=row, column=2).fill = yellow_fill
            worksheet.cell(row=row, column=3).fill = yellow_fill
            
            # Green for Site columns
            for col in range(4, 8):
                worksheet.cell(row=row, column=col).fill = green_fill
            
            # Red for non-empty Comments
            if worksheet.cell(row=row, column=8).value:
                worksheet.cell(row=row, column=8).fill = red_fill
        
        writer.close()
        print(f"Report exported successfully to: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"Error exporting Excel file: {str(e)}")
        sys.exit(1)

def main():
    try:
        # Find CSV file
        csv_file = find_csv_file()
        
        # Process data
        print("Running the script...")
        results_df = process_data(csv_file)
        
        # Get output filename based on data dates
        output_file = get_output_filename(pd.read_csv(csv_file))
        
        # Export Excel file
        export_to_excel(results_df, output_file)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()