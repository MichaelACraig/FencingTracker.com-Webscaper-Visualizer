# Load the necessary packages
library(leaflet)
library(sf)
library(magrittr)
library(geojsonio)
library(htmlwidgets)

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

# Loop through regions and add polygons to the map
for (region_name in names(regions)) {
  
  # Debugging: Print out the states filtered for each region
  filtered_states <- us_states[us_states$id %in% regions[[region_name]], ]
  print(paste(region_name, ":", toString(filtered_states$id)))
  
  m <- m %>%
    addPolygons(data = filtered_states,
                fillColor = region_colors[[region_name]],
                fillOpacity = 0.6,
                color = "black",
                weight = 1,
                label = ~id)
}

# Display the map
saveWidget(m, "map.html", selfcontained = TRUE)

