import mysql.connector
import pandas as pd

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "reporting_db"
}

try:
    # Connect to MySQL
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Fetch data from MySQL
    query = "SELECT * FROM sales_data"
    cursor.execute(query)
    result = cursor.fetchall()

    # Get column names
    columns = [desc[0] for desc in cursor.description]

    # Convert to Pandas DataFrame
    df = pd.DataFrame(result, columns=columns)

    # Save to Excel
    excel_file = "database_report.xlsx"
    df.to_excel(excel_file, index=False)

    print(f"✅ Report saved successfully as {excel_file}")

except mysql.connector.Error as e:
    print(f"❌ Error connecting to MySQL: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
