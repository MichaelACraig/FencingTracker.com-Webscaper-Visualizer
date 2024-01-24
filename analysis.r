# Snippet view of the data
RegionData <- read.csv("Outputs/RegionData.csv")
head(RegionData)

TwoClubFencers <- read.csv("Outputs/TwoClubFencers.csv")
head(TwoClubFencers)

#print(.libPaths())
# Load the necessary packages
library(leaflet)
library(magrittr)
library(sf)
library(geojsonio)

# Read the GeoJSON file into R
# Replace 'us_states.geojson' with the path to your file
us_states <- sf::st_read('/../../../Library/R/x86_64/4.3/library/geojsonio/examples/us_states.json')

# Create a leaflet map
m <- leaflet() %>%
    addTiles()

# Add polygons for each region
for (state in Midwest) {
    m <- m %>%
        addPolygons(data = us_states[us_states$NAME == state, ], 
                    fillColor = "blue", 
                    fillOpacity = 0.6, 
                    color = "white", 
                    weight = 1)
}

for (state in West) {
    m <- m %>%
        addPolygons(data = us_states[us_states$NAME == state, ], 
                    fillColor = "red", 
                    fillOpacity = 0.6, 
                    color = "white", 
                    weight = 1)
}

for (state in South) {
    m <- m %>%
        addPolygons(data = us_states[us_states$NAME == state, ], 
                    fillColor = "green", 
                    fillOpacity = 0.6, 
                    color = "white", 
                    weight = 1)
}

for (state in North) {
    m <- m %>%
        addPolygons(data = us_states[us_states$NAME == state, ], 
                    fillColor = "yellow", 
                    fillOpacity = 0.6, 
                    color = "white", 
                    weight = 1)
}

# Display the map
saveWidget(m, "map.html", selfcontained = TRUE)