# The POI-ROI-map project


## Abstract
Life science - an American thing? The SARS-CoV-2 pandemic has shown that European research institutions & companies are very well capable of making their contribution to the global fight for health. However, it is very easy to loose overview about which interesting life science facilities exist in Europe. The original intention of this little ROI-map project was to simplify your job search by enabling you to mark individual regions and points of interest (ROIs & POIs). Nonetheless, the script can also be used for any other purpose! A simple .xlsx spreadsheet serves you as an easy-to-access "database" and let you define the respective coordinates. Available marker elements are ROIs, distance as well as POI markers. All elements can be color-coded, the POIs can be further specified by info-popups and are automatically clustered with respect to the current zoom setting. Moreover, multiple map representations are available. Have fun to play around.<br><br>


## Table of Content
- [Installation](#installation)
- [Folder structure](#folderstructure)
- [Getting Started](#gettingstarted)
- [Example](#example)
- [Authors](#authors)
- [Contributors & Credits](#contributorscredits)
- [License](#license)
- [Acknowledgments & Sources](#acknowledgmentssources)
- [Contact](#contact)


## <a id='installation'></a> Installation
- Install Python on your local computer.
- Install following required python packages:
    - folium
    - geopandas
    - pandas
  Depending on your local setup use the pip- or the conda-commands. See requirements.txt for further specifications.
- Install an IDE of your choice


## <a id='folderstructure'></a> Folder structure
```
|   LICENSE.md
|   POI-ROI-map.py                              <-- main script
|   README.md
|   REQUIREMENTS.txt
|
+---resources
|   |   database.xlsx                           <-- database to define the positions of markers etc
|   |
|   +---data
|   |       CNTR_BN_20M_2020_3035.geojson       <-- EuroGeographics dataset for depicting boundaries of European countries
|   |
|   \---images                                  <-- all images required for HTML-headline and the map (legend) incl. vector graphics
|           blank.png
|           blank.svg
|           legend.png
|           legend.svg
|           logo.png
|           logo.svg
|           POI-ROI-map.png
|           POI-ROI-map.svg
|           title.png
|           title.svg
|
\---target                                      <-- target file (HTML-map) to be shown in your internet browser
        POI-ROI-map.html
```


## <a id='gettingstarted'></a> Getting Started
- Download the repository
  - Follow these steps:
    - Open the database.xlsx-file with a spreadsheet file editor. MS Excel works best
    - Adjust the database.xlsx-file with individual entries (optional). The required coordinates (latitude and longitude) can be obtained from google maps, latlong.net .... 
    For a new data entry expand the db-area of every worksheet by one line. Fill out all other required cells of the new row. Optional cells can be left blank.
    ```
      worksheet         input             necessity       
      ---------------------------------------------- 
      icons             name              optional        
                        latitude          required        
                        longitude         required        
                        status            required        
                        info1             optional        
                        info2             optional        
                        info3             optional        
                        cluster           required        
                        city              optional       
                        links             optional       
                        address           optional       
      ROI_areas         city              optional       
                        latitude          required       
                        longitude         required       
                        radius            required       
                        color             required       
      dist_cycles       cycle             optional       
                        radius            required       
                        color             required       
      starting_point    city              optional       
                        latitude          required       
                        longitude         required       
    ```
    - Open IDE of your choice and let run the program
    - Open the ROI_Map.html-file in your internet browser and take a look what you have created!
    - The legend on the right enables you to select which clusters should be depicted as well as which visualization should be used for the map


## <a id='example'></a> Example
A typical view looks like this:<br>
![POI-ROI-map_image](./resources/images/POI-ROI-map.png)


## <a id='authors'></a> Authors
bio-century.net admin


## <a id='contributorscredits'></a> Contributors & Credits
comber.io admin for inspirations, presentations of the website and code corrections.<br><br>


## <a id='license'></a> License
This project is published under the GNU General Public License v2.0 license. For terms and conditions see LICENSE.md<br><br>


## <a id='acknowledgmentssources'></a> Acknowledgments & Sources
- Technical sources:
  - <a href="https://inkscape.org/?switchlang=en/"> Inkscape </a>, under <a href="https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html">GNU GPL 2</a>
  - <a href="http://python-visualization.github.io/folium/"> Folium </a>, under <a href="https://github.com/python-visualization/folium/blob/main/LICENSE.txt">MIT</a>
  - <a href="https://leafletjs.com/"> Leaflet </a>, under <a href="https://github.com/Leaflet/Leaflet/blob/main/LICENSE">BSD 2</a>
  - <a href="https://wiki.osmfoundation.org/wiki/Main_Page">OpenStreetMap</a>, under <a href="https://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ#The_OpenStreetMap_Geodata_Licence">ODbL</a>
  - <a href="https://stamen.com/">Stamen Design</a>, under <a href="https://github.com/stamen/maps.stamen.com/blob/master/LICENSE">BSD 3</a>
  - <a href="https://carto.com/">CartoDB, CartoDB attributions</a>, under <a href="https://github.com/CartoDB/cartodb/blob/master/LICENSE">BSD 3</a>
  - ©EuroGeographics for the administrative boundaries (<a href="https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units">link</a>)

- Coding sources:
  - https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac
  - https://python-visualization.github.io/folium/quickstart.html
  - https://www.earthdatascience.org/tutorials/introduction-to-leaflet-animated-maps/
  - https://stackoverflow.com/questions/33086212/center-3-floating-divs-inside-a-wrapper-div
  - https://code2care.org/pages/how-to-place-two-div-elements-next-to-each-other
  - https://geopandas.org/en/stable/gallery/polygon_plotting_with_folium.html
  - https://coolum001.github.io/foliummaps.html


### <a id='contact'></a> Contact
info@bio-century.net


