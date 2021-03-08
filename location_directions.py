import googlemaps
from datetime import datetime
import time

gmaps = googlemaps.Client(key="INSERT CLIENT KEY")

class find_location_directions():
    def get_iframe(self, address):
        gmaps = googlemaps.Client(key='INSERT CLIENT KEY')
        # Geocoding an address
        geocode_result = gmaps.geocode(address)
        # IFRAME FOR EMBEDDING
        lat = geocode_result[0].get("geometry").get("location").get("lat")
        lng = geocode_result[0].get("geometry").get("location").get("lng")
        link_directions = 'https://maps.google.com/maps?q='+str(lat)+','+str(lng)+'&hl=es;z=14&amp'
        return link_directions

    def get_duration(self, address):
        # Request directions 
        now = datetime.now()
        directions_result = gmaps.directions("INSERT YOUR ADRESS",
                                             address,
                                             departure_time=now)
        #DURATION
        duration = directions_result[0].get("legs")[0].get("duration").get('text')
        return duration

    def create_directions(self, address, postal_code, place):
            address = str(address) +  str(postal_code) + str(place)
            duration = str(self.get_duration(address))
            link_directions = str(self.get_iframe(address))
            time.sleep(2)
            print(link_directions, duration)
            return duration, link_directions
