# import plotly.graph_objects as go

# Ra=[73.6305,56.868975,-81.49779,-28.375005,-52.832145,145.95,-175.296,-151.65,101.85,-154.5,-175.821]
# Dec=[-72.5771,26.622,23.530393,38.21,89.348426,14.7899,-28.042,30.27,25.28,17.76,-4.3204]
# fig = go.Figure()

# fig.add_trace(go.Scattergeo(
#     mode="markers",
#     lon = Ra,
#     lat = Dec,
#     marker = {'size': 8,
#               'color':'blue',
#              })
#              )

# fig.update_layout(geo=dict(
#                     showland=False,
#                     showcountries=False,
#                     showocean=False,
#                     countrywidth=0.5,
#                     #coastlinecolor='rgb(255, 255, 255)',
#                     landcolor='rgb(255, 255, 255)',
#                     lakecolor='rgb(255, 255, 255)',
#                     oceancolor='rgb(255, 255, 255)',
#                     projection=dict(
#                         type='aitoff',
#                     ),
#                     lonaxis=dict(
#                         showgrid=True,
#                         dtick=15,
#                         gridcolor='rgb(102, 102, 102)',
#                         gridwidth=0.5
#                     ),
#                     lataxis=dict(
#                         showgrid=True,
#                         dtick=15,
#                         gridcolor='rgb(102, 102, 102)',
#                         gridwidth=0.5
#                     )
#                 )
# )
# fig.show()
# #plot(fig)


import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u
from astroplan import Observer, FixedTarget
from astroplan.plots import plot_sky, plot_airmass

observing_location = EarthLocation(lat='31d57.5m', lon='-111d35.8m', height=2096*u.m)
observer = Observer(location=observing_location, name="Subaru Telescope", timezone="US/Hawaii")
time = Time('2024-05-03 12:00:00')  # Set your desired observation time


target1 = FixedTarget.from_name("Polaris")
target2 = FixedTarget.from_name("Sirius")


altaz_frame = AltAz(obstime=time, location=observer.location)
altaz_target1 = target1.coord.transform_to(altaz_frame)
altaz_target2 = target2.coord.transform_to(altaz_frame)

alt_target1 = altaz_target1.alt
az_target1 = altaz_target1.az
alt_target2 = altaz_target2.alt
az_target2 = altaz_target2.az


plt.figure(figsize=(10, 6))
plot_sky(target1, observer, time)
plot_sky(target2, observer, time)
plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
plt.title("Sky Positions")
plt.show()



# Print altitude and azimuth values
print("Altitude of Polaris:", alt_target1)
print("Azimuth of Polaris:", az_target1)
print("Altitude of Sirius:", alt_target2)
print("Azimuth of Sirius:", az_target2)

