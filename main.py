

import pandas as pd
import numpy as np
import plotly
import folium
import plotly.graph_objects as go   #存放图的对象的组件
#import chart_studio.plotly as py  #在线画图
import plotly.express as px

#m = folium.Map()
#添加图层，生成一站式服务。
#draw = Draw(export=True, filename="test.geojson")
#draw.add_to(m)
#m

df_incidents=pd.read_csv('5GPCI.csv')

lat = 36.8202
long = 118.0208

sanfran_map = folium.Map(location=[lat,long],zoom_start=12)
sanfran_map

sanfran_map = folium.Map(location=[lat,long],zoom_start=12)

incidents = folium.map.FeatureGroup()
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
            folium.CircleMarker(
            [lat, lng],
            radius=5,
            color='red',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
            )
    )
sanfran_map.add_child(incidents)

