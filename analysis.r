# Snippet view of the data
RegionData <- read.csv("Outputs/RegionData.csv")
head(RegionData)

TwoClubFencers <- read.csv("Outputs/TwoClubFencers.csv")
head(TwoClubFencers)

# Visualization of Regional Data through the US Map; Installed needed packages
library("leaflet")
library("htmlwidgets")
library("ggplot2")
library("maps")
library("sf")



#Saves map to html to be viewed and opened in browser
saveWidget(m, "map.html", selfcontained = TRUE)

