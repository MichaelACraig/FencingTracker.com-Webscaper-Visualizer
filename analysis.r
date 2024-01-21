#Snippet view of the data
RegionData <- read.csv("Outputs/RegionData.csv")
head(RegionData)

TwoClubFencers <- read.csv("Outputs/TwoClubFencers.csv")
head(TwoClubFencers)

#Visualization of Regional Data
library("leaflet")
library("htmlwidgets")

# Basic US map
m <- leaflet() %>%
    addProviderTiles(providers$OpenStreetMap) %>%
    setView(lng = -95.7129, lat = 37.0902, zoom = 4)

#Saves map to html to be viewed and opened in browser
saveWidget(m, "map.html", selfcontained = TRUE)
