"""PROGRAM OF Automation Tasks like Creating,inserting data in files automatically.
PROGRAM NAME: Automation Tasks.
AUTHOR: AINEEN SAYYED.
DATE CREATED: 6/02/2026"""
import pandas as pd
import os
import glob

def create_sample_files():
    if not os.path.exists('data_input'):
        os.makedirs('data_input')

    data1 = {'Product': ['Laptop', 'Mouse', 'Monitor'], 'Quantity': [5, 20, 10], 'Price': [1000, 25, 200]}
    data2 = {'Product': ['Laptop', 'Keyboard', 'Monitor'], 'Quantity': [2, 15, 5], 'Price': [1000, 50, 200]}

    pd.DataFrame(data1).to_csv('data_input/january_sales.csv', index=False)
    pd.DataFrame(data2).to_csv('data_input/february_sales.csv', index=False)
    print("Step 1: Sample CSV files created in '/data_input' folder.")


def run_automation():
   
    path = 'data_input'
    all_files = glob.glob(os.path.join(path, "*.csv"))

  
    list_of_dfs = [pd.read_csv(f) for f in all_files]
    combined_df = pd.concat(list_of_dfs, ignore_index=True)

    
    combined_df['Revenue'] = combined_df['Quantity'] * combined_df['Price']

    report = combined_df.groupby('Product')['Revenue'].sum().reset_index()
    report = report.sort_values(by='Revenue', ascending=False)

   
    output_file = 'Final_Sales_Report.xlsx'
    with pd.ExcelWriter(output_file) as writer:
        combined_df.to_excel(writer, sheet_name='Raw Data', index=False)
        report.to_excel(writer, sheet_name='Summary', index=False)

    print(f"Step 2: Automation Complete! File saved as: {output_file}")

if __name__ == "__main__":
    
    try:
        create_sample_files()
        run_automation()
    except Exception as e:
        print(f"An error occurred: {e}")
