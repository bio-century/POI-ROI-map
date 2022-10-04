# import Python libraries
import folium
import geopandas as gpd
import pandas as pd
from folium.plugins import FloatImage
from folium.plugins import MarkerCluster



# preamble before getting started: The initial idea of visualization was obtained from the following sources:
# https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac
# https://python-visualization.github.io/folium/quickstart.html
data_icons=pd.read_excel('./resources/database.xlsx', index_col=None, header=[0], sheet_name='icons')
data_ROI_areas=pd.read_excel('./resources/database.xlsx', index_col=None, header=[0], sheet_name='ROI_areas')
data_dist_cycles=pd.read_excel('./resources/database.xlsx', index_col=None, header=[0], sheet_name='dist_cycles')
data_starting_point=pd.read_excel('./resources/database.xlsx', index_col=None, header=[0], sheet_name='starting_point')



# define startpoint of the geomap view
# https://www.earthdatascience.org/tutorials/introduction-to-leaflet-animated-maps/
center_of_view = [float(data_starting_point.iloc[0]['latitude']), float(data_starting_point.iloc[0]['longitude'])]



# initiate map
m = folium.Map(location=center_of_view, tiles="OpenStreetMap", zoom_start=4.5, control_scale=True)



# create and fill headline of html doc
# adapted from:
# https://stackoverflow.com/questions/33086212/center-3-floating-divs-inside-a-wrapper-div
# https://code2care.org/pages/how-to-place-two-div-elements-next-to-each-other
title_html = '''
    <head><style> html { overflow-y: hidden; margin:0;padding:0} 
    img.one {
        height: 100%;
        width: 100%;
    }
    img.two {
        height: 100%;
        width: 100%;
    }
    #div1, #div2, #div3 {
        width: 10%;
        display:inline-block;
        height: 10%;
    }

    #wrapperDiv {
        text-align: center;
    }
    </style></head>
    <div id="wrapperDiv">
        <div id="div1" style="padding:0px;background-color:#ffffff;float:left"><img class="one" src="./../resources/images/logo.png"></div>
        <div id="div2" style="padding:0px;background-color:#ffffff;float:center"><img class="two" src="./../resources/images/title.png"></div>
        <div id="div3" style="padding:0px;background-color:#ffffff;float:right"><img class="one" src="./../resources/images/blank.png"></div>
    </div>
    <div style="padding:0px;background-color:#eff3fb;color:#0345bf;"><center>
    <font size="-3">copyrights: 
    Main libraries: <a href="http://python-visualization.github.io/folium/"> Folium </a>, under <a href="https://github.com/python-visualization/folium/blob/main/LICENSE.txt">MIT</a> |  
    <a href="https://leafletjs.com/"> Leaflet </a>, under <a href="https://github.com/Leaflet/Leaflet/blob/main/LICENSE">BSD 2</a> |  | 
    Data by <a href="https://wiki.osmfoundation.org/wiki/Main_Page">OpenStreetMap</a>, under <a href="https://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ#The_OpenStreetMap_Geodata_Licence">ODbL</a> | 
    Map tiles by <a href="https://stamen.com/">Stamen Design</a>, under <a href="https://github.com/stamen/maps.stamen.com/blob/master/LICENSE">BSD 3</a> | 
    <a href="https://carto.com/">CartoDB, CartoDB attributions</a>, under <a href="https://github.com/CartoDB/cartodb/blob/master/LICENSE">BSD 3</a> | 
    © EuroGeographics for the administrative boundaries (<a href="https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units">link</a>).
    .</font>
    </center>
    </div>
     ''' 
m.get_root().html.add_child(folium.Element(title_html))



# implement EU country borders to map
# https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/countries#countries20
marker_cluster_EU_countries = MarkerCluster(name='EU countries',show=True)
fp = "./resources/data/CNTR_BN_20M_2020_3035.geojson"
eu_df = gpd.read_file(fp)
geo_j = folium.GeoJson(data=eu_df,style_function=lambda x: {'fillColor': 'none'},
                               name="EU countries")
geo_j.add_to(marker_cluster_EU_countries)
marker_cluster_EU_countries.add_to(m)



# add different standard map representations to the menu
folium.TileLayer('stamentoner').add_to(m)
folium.TileLayer('stamenTerrain').add_to(m)
folium.TileLayer('stamenwatercolor').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.TileLayer("", name="None", attr="blank").add_to(m)



# draw circles around the center_of_view-position for distance-benchmark depiction
# coordinates & radii: ROI_map3.xlsx, sheets 'starting_point' & 'Radii'
def draw_circle(input_radius,input_center_circle,input_color,input_fill):
    folium.Circle(
        radius=input_radius,
        location=input_center_circle,
        color=input_color,
        fill=False,
        #weight=0.7,
        #popup = "",
        #opacity=0.5,
    ).add_to(m)

for i in range(0,len(data_dist_cycles)):
    draw_circle(float(data_dist_cycles.iloc[i]['radius']),center_of_view,data_dist_cycles.iloc[i]['color'],False)



# optional: circles for dedicated regions of interest
# latitude, longitude & radii: ROI_map3.xlsx, sheets 'ROI_areas'
def draw_circle2(input_radius,input_center_circle,input_color,input_fill):
    folium.Circle(
        radius=input_radius,
        location=input_center_circle,
        color=input_color,
        fill=input_fill,
        weight=0.99,
        opacity=0.7,
    ).add_to(m)

for i in range(0,len(data_ROI_areas)):
    draw_circle2(float(data_ROI_areas.iloc[i]['radius']),[float(data_ROI_areas.iloc[i]['latitude']),float(data_ROI_areas.iloc[i]['longitude'])],data_ROI_areas.iloc[i]['color'],True)

lgd_txt = '<span style="color: {col};">{txt}</span>'
color='red'



# cluster icons with respect to location, category and zoom
marker_cluster_cluster1 = MarkerCluster(name="cluster1")
marker_cluster_cluster2 = MarkerCluster(name="cluster2")
marker_cluster_individual_marker = MarkerCluster(name="individual markercluster")

# read in icons properties in a loop
for i in range(0,len(data_icons)):
    print(str(i))
    color=data_icons.iloc[i]['status']
    lgd_txt=(str(i)+'. '+data_icons.iloc[i]['name'])
    
    # generate html-code for icon popups
    info1_str=data_icons.iloc[i]['info1']
    info2_str=data_icons.iloc[i]['info2']
    info3_str=data_icons.iloc[i]['info3']
    data_icons_popup = f'''<table><tr><th>info1:&nbsp;</th><th>
            {info1_str}
            </th></tr>
            <tr><td>info2:&nbsp;</td><td>
            {info2_str}
            </td></tr>
            <tr><td>info3:&nbsp;</td><td>
            {info3_str}
            </td></tr></table>'''
    
    pl = folium.Marker(
        location=[float(data_icons.iloc[i]['latitude']), float(data_icons.iloc[i]['longitude'])],
        popup = data_icons_popup,
        icon=folium.Icon(color, icon="info-sign"),
        opacity=0.65,
    )
    
    # separate into 2 categories
    if data_icons.iloc[i]['cluster']=='cluster1':
        pl.add_to(marker_cluster_cluster1)
    elif data_icons.iloc[i]['cluster']=='cluster2':
        pl.add_to(marker_cluster_cluster2)
    else:
        pl.add_to(marker_cluster_individual_marker)

marker_cluster_cluster1.add_to(m)
marker_cluster_cluster2.add_to(m)
marker_cluster_individual_marker.add_to(m)



# add layer control to the map
folium.map.LayerControl('topright', collapsed=False).add_to(m)

longituteslist=[]
for i in range(0,len(data_icons)):
    longituteslist.append(float(data_icons.iloc[i]['latitude']))

latitudeslist=[]
for i in range(0,len(data_icons)):
    latitudeslist.append(float(data_icons.iloc[i]['longitude']))



# Add legend for icon explanation (25dpi)
image = ('./../resources/images/legend.png')
FloatImage(image, bottom=7, left=1).add_to(m)



# save html
m.save("./target/POI-ROI-map.html")
#m.save("./target/01_MAPS.html")