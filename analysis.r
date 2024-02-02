# Notes:
# Inorder to do the statistical analysis, we need to gather a list of all individuals in the region_dataset and place them in a-
# individual region vector. We can then get a mean of all individual's wins and loss, and generate a ratio that covers the entire region.
# Once this is done, we can compare which regions perform the best over time, overall.

#We can then move to the edge case analysis, which is the two_clubs_dataset. I'm pretty sure removed all two-clubs cases into a separate
#dataset .csv file without creating duplicates, so we can just cross-reference the region_dataset and the two_clubs_dataset, and compare
#the win/loss ratio of the two to see which do better over time.


# Load the necessary packages
library(leaflet)
library(sf)
library(magrittr)
library(geojsonio)
library(htmlwidgets)
library(dplyr)

region_dataset <- read.csv("Outputs\\RegionData.csv")
head(region_dataset)

two_clubs_dataset <- read.csv("Outputs\\TwoClubFencers.csv")
head(two_clubs_dataset)

main_dataset <- read.csv("Outputs\\ScrapedData.csv")
head(main_dataset)

# Region summaries - convert to integers
region_summaries <- region_dataset %>%
  group_by(Region) %>%
  summarise(
    RegionTotalWins = sum(as.numeric(ATWins), na.rm = TRUE),
    RegionTotalLosses = sum(as.numeric(ATLosses), na.rm = TRUE),
    RegionWinLossRatio = ifelse(TotalLosses == 0, NA, RegionTotalWins / RegionTotalLosses)
  )

# View the summarized data
print(region_summaries)

# Two Club Fencers Analysis - Take the two_clubs dataset and the main dataset
# Essentially doing the same thing as regional summaries, but for the main dataset and comparing it with two_clubs win/lose ratio
main_dataset_summaries <- main_dataset %>%
  summarise(
    MainTotalWins = sum(as.numeric(ATWins), na.rm = TRUE),
    MainTotalLosses = sum(as.numeric(ATLosses), na.rm = TRUE),
    MainWinLossRatio = ifelse(MainTotalLosses == 0, NA, MainTotalWins / MainTotalLosses)
  )

print(main_dataset_summaries)
  
two_clubs_summaries <- region_dataset %>%
  summarise(
    TwoClubsTotalWins = sum(as.numeric(ATWins), na.rm = TRUE),
    TwoClubsTotalLosses = sum(as.numeric(ATLosses), na.rm = TRUE),
    TwoClubsWinLossRatio = ifelse(TwoClubsTotalLosses == 0, NA, TwoClubsTotalWins / TwoClubsTotalLosses)
  )

print(two_clubs_summaries)

# Read the GeoJSON file into R
us_states <- sf::st_read('C:\\Users\\13212\\Desktop\\Project Files\\FencingTrackerWebScraper\\FencingTracker.com-Webscaper-Visualizer\\geojsonio\\examples\\us_states.json')

# Create a leaflet map
m <- leaflet() %>%
  addTiles() %>%
  setView(lng = -96, lat = 37.8, zoom = 4)

# Define regions and their colors
regions <- list(
  Midwest = c('Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota',
              'Ohio', 'South Dakota', 'Wisconsin'),
  
  West = c('Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'New Mexico',
           'Oregon', 'Utah', 'Washington', 'Wyoming'),
  
  South = c('Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi',
            'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia'),
  
  North = c('Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pennsylvania',
            'Rhode Island', 'Vermont')
)

region_colors <- c(
  Midwest = "yellow", 
  West = "orange", 
  South = "red", 
  North = "blue"
  )


for (region_name in names(regions)) { # Loop through regions and add polygons to the map
  
  # Debugging: Print out the states filtered for each region
  filtered_states <- us_states[us_states$id %in% regions[[region_name]], ]
  print(paste(region_name, ":", toString(filtered_states$id)))
  
  m <- m %>%
    addPolygons(data = filtered_states,
                fillColor = region_colors[[region_name]],
                fillOpacity = 0.6,
                color = region_colors[[region_name]],
                weight = 0.1,
                label = ~id)
}

for (region_name in names(regions)) {
  filtered_states <- us_states[us_states$id %in% regions[[region_name]], ]
  
  if(!all(st_is_valid(filtered_states))){
    filtered_states <- st_make_valid(filtered_states)
  }
  
  filtered_states <- st_simplify(filtered_states, preserveTopology = TRUE)
  
  # Calculate the merged geometry to find the centroid of each region
  merged_geometry <- st_union(filtered_states)
  centroid <- st_centroid(merged_geometry)
  
  centroid_coords <- as.numeric(st_coordinates(centroid))
  
  # Assuming you have a way to calculate the win/loss ratio for each region
  # For demonstration, let's just display the region name. Replace this with your actual ratio.
  ratio_text <- paste(region_name, "Win/Loss Ratio: X/Y") # Replace X/Y with actual ratio
  
  m <- m %>%
    addLabelOnlyMarkers(lng = centroid_coords[1], lat = centroid_coords[2],
                        label = ratio_text, labelOptions = labelOptions(noHide = TRUE, direction = 'center'))
}


# Display the map; Viewer in RStudio has limitations so export to web widget.
saveWidget(m, "analysis_map.html", selfcontained = TRUE) 

