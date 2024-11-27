# import pandas as pd
# import mysql.connector

# # Read CSV data into a DataFrame
# df = pd.read_csv('CORSFINAL2.csv')

# # Establish connection to MySQL
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Root@123",
#     database="new"
# )
# cursor = connection.cursor()

# # Insert data into MySQL table
# for index, row in df.iterrows():
#     # Limit corsid to 50 characters
#     corsid = str(row['corsid'])
#     state_name = str(row['state_name'])
#     site_name = str(row['site_name'])
#     cursor.execute("INSERT INTO cors_app_gdc_data (corsid,state_name,site_name) VALUES (%s , %s , %s)", (corsid,state_name,site_name))

# # Commit changes and close connection
# connection.commit()
# connection.close()



# import pandas as pd
# import mysql.connector

# # Read CSV data into a DataFrame
# df = pd.read_csv('CORS_CODE_COORDINATES3.csv')

# # Establish connection to MySQL
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Root@123",
#     database="cors"
# )
# cursor = connection.cursor()

# # Insert data into MySQL table
# for index, row in df.iterrows():
#     # Extract values from the row and handle None cases
#     values = (
#         row.get('corsid', None),
#         row.get('site_name', None),
#         row.get('site_code', None),
#         row.get('coordinates_of_sites_dms_lat', None),
#         row.get('coordinates_of_sites_dms_long', None),
#         row.get('coordinates_of_sites_dms_elp_height', None),
#         row.get('digi_wr21_ip_dns_gateway_of_alloy_field', None),
#         row.get('digi_username_password', None),
#         row.get('alloy_cc_network_ip', None),
#         row.get('alloy_netmask', None),
#         row.get('alloy_local_wifi_ip', None),
#         row.get('alloy_username_and_password', None),
#         row.get('vendor_username', None),
#         row.get('gdc_username', None),
#         row.get('state', None)
#     )
    
#     # Prepare the SQL query
#     cursor.execute("""
#         INSERT INTO cors_app_centre_data (
#             corsid, site_name, site_code, coordinates_of_sites_dms_lat,
#             coordinates_of_sites_dms_long, coordinates_of_sites_dms_elp_height,
#             digi_wr21_ip_dns_gateway_of_alloy_field, digi_username_password,
#             alloy_cc_network_ip, alloy_netmask, alloy_local_wifi_ip,
#             alloy_username_and_password, vendor_username, gdc_username, state
#         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """, values)

# # Commit changes and close connection
# connection.commit()
# connection.close()




import pandas as pd
import mysql.connector

# Read CSV data into a DataFrame
df = pd.read_csv('Laplace Stations Final WGS84-DD.csv')

# Establish connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="grmdb"
)
cursor = connection.cursor()

# Retrieve the highest current keyid
cursor.execute("SELECT keyid FROM benchmark_gtstation ORDER BY keyid DESC LIMIT 1")
result = cursor.fetchone()

# Determine the starting number for keyid
if result and result[0]:
    highest_keyid = result[0]
    highest_number = int(highest_keyid[3:])
else:
    highest_number = 0

# Insert data into MySQL table
for index, row in df.iterrows():
    # Increment the keyid number
    highest_number += 1
    new_keyid = f"GTS{highest_number:04d}"
    
    # Extract values from the row and handle None cases
    values = (
        new_keyid,
        row.get('gtstation_name', None),
        row.get('ellipsoidheight', None),
        row.get('state', None),
        row.get('latitude', None),
        row.get('longitude', None),
        row.get('gdc_username', None)
    )
    
    # Prepare the SQL query
    cursor.execute("""
        INSERT INTO benchmark_gtstation (
            keyid, gtstation_name, ellipsoidheight, state, latitude, longitude,  gdc_username
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)""", values)

# Commit changes and close connection
connection.commit()
connection.close()