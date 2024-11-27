# import os
# import sys
# import csv

# # Add the project root directory to the system path
# sys.path.append(r"D:\benchmarkdata\corsdatabaseproject")

# # Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cors.settings')

# # Initialize Django
# import django
# django.setup()

# # Import the model
# from cors_app.models import CorsAppGdcData,BenchmarkGcpdata,BenchmarkSbmdata,BenchmarkGtstation

# # Define the path to the images directory
# IMAGE_PATH = r"D:\benchmarkdata\corsdatabaseproject\media\image\image"

# # Define the output CSV file
# OUTPUT_CSV = r"D:\benchmarkdata\corsdatabaseproject\image_data_sbm.csv"

# # Create and populate the CSV file
# with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     # Write the header
#     writer.writerow(["keyid", "gdc_username", "east_count", "west_count", "north_count", "south_count", "total_images"])

#     # Fetch all records from the database
#     cors_data = BenchmarkSbmdata.objects.using('database3').values("keyid", "gdc_username")

#     for data in cors_data:
#         keyid = data["keyid"]
#         gdc_name = data["gdc_username"]

#         # Initialize counts
#         east_count = west_count = north_count = south_count = 0

#         # Match images in the directory
#         for filename in os.listdir(IMAGE_PATH):
#             if filename.startswith(f"{keyid}_"):
#                 if "_east" in filename:
#                     east_count += 1
#                 elif "_west" in filename:
#                     west_count += 1
#                 elif "_north" in filename:
#                     north_count += 1
#                 elif "_south" in filename:
#                     south_count += 1

#         # Calculate total images
#         total_images = east_count + west_count + north_count + south_count

#         # Write the row to the CSV
#         writer.writerow([keyid, gdc_name, east_count, west_count, north_count, south_count, total_images])

# print(f"CSV created successfully at {OUTPUT_CSV}")
# import os
# import sys
# import csv

# # Add the project root directory to the system path
# sys.path.append(r"C:\wwwroot\corsdatabaseproject")

# # Set the Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cors.settings')

# # Initialize Django
# import django
# django.setup()

# # Import the model
# from cors_app.models import CorsAppGdcData,BenchmarkGcpdata,BenchmarkSbmdata,BenchmarkGtstation

# # Define the path to the images directory
# IMAGE_PATH = r"C:\wwwroot\corsdatabaseproject\media\image\image"

# # Define the output CSV file
# OUTPUT_CSV = r"C:\wwwroot\corsdatabaseproject\image_data_total_gcp.csv"

# # Create and populate the CSV file
# with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     # Write the header
#     writer.writerow(["gdc_username", "east_count", "west_count", "north_count", "south_count", "total_images"])

#     # Fetch all unique gdc_names from the database
#     cors_data = BenchmarkGcpdata.objects.using('database3').values("gdc_username").distinct()

#     for data in cors_data:
#         gdc_username = data["gdc_username"]

#         # Initialize counts
#         east_count = west_count = north_count = south_count = 0

#         # Fetch all corsid values for this gdc_name
#         corsids = BenchmarkGcpdata.objects.using('database3').filter(gdc_username=gdc_username).values_list("keyid", flat=True)

#         # Match images in the directory for all corsids belonging to this gdc_name
#         for keyid in corsids:
#             for filename in os.listdir(IMAGE_PATH):
#                 if filename.startswith(f"{keyid}_"):
#                     if "_east" in filename:
#                         east_count += 1
#                     elif "_west" in filename:
#                         west_count += 1
#                     elif "_north" in filename:
#                         north_count += 1
#                     elif "_south" in filename:
#                         south_count += 1

#         # Calculate total images for this gdc_name
#         total_images = east_count + west_count + north_count + south_count

#         # Write the row to the CSV
#         writer.writerow([gdc_username, east_count, west_count, north_count, south_count, total_images])

# print(f"CSV created successfully at {OUTPUT_CSV}")


import os
import sys
import csv

# Add the project root directory to the system path
sys.path.append(r"C:\wwwroot\corsdatabaseproject")

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cors.settings')

# Initialize Django
import django
django.setup()

# Import the models
from cors_app.models import CorsAppGdcData, CorsAppCentreData

# Define the path to the images directory
IMAGE_PATH = r"C:\wwwroot\corsdatabaseproject\media\image"

# Define the output CSV file
OUTPUT_CSV = r"C:\wwwroot\corsdatabaseproject\gdc_image_totals.csv"

# Create and populate the CSV file
with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["gdc_username", "east_count", "west_count", "north_count", "south_count", "total_images"])

    # Fetch all unique `gdc_username` values
    gdc_data = CorsAppCentreData.objects.values("gdc_username").distinct()

    for data in gdc_data:
        gdc_username = data["gdc_username"]

        # Initialize counts
        east_count = west_count = north_count = south_count = 0

        # Fetch all `corsid` values associated with this `gdc_username`
        corsids = CorsAppCentreData.objects.filter(gdc_username=gdc_username).values_list("corsid", flat=True)

        # Match images in the directory for all `corsid` values
        for corsid in corsids:
            for filename in os.listdir(IMAGE_PATH):
                if filename.startswith(f"{corsid}_"):
                    if "_east" in filename:
                        east_count += 1
                    elif "_west" in filename:
                        west_count += 1
                    elif "_north" in filename:
                        north_count += 1
                    elif "_south" in filename:
                        south_count += 1

        # Calculate total images for this `gdc_username`
        total_images = east_count + west_count + north_count + south_count

        # Write the row to the CSV
        writer.writerow([gdc_username, east_count, west_count, north_count, south_count, total_images])

print(f"CSV created successfully at {OUTPUT_CSV}")



