# Public Transport Quality Grades Backend
API Backend for Web Application

## Integrating public transport quality grades from ARE

The raw data for the current transport quality from ARE (Bundesamt für Raumentwicklung) is available here: <https://data.geo.admin.ch/ch.are.gueteklassen_oev/>

To use the data in this application, the data has to be converted from Shapefile to GeoJSON.
Use the following ogr2ogr command:

```bash
ogr2ogr -f GeoJSON -select "KLASSE" Oev_Gueteklassen_ARE.json Oev_Gueteklassen_ARE.shp -lco RFC7946=YES
```

The resulting file should be copied to `data/Oev_Gueteklassen_ARE.json`.
