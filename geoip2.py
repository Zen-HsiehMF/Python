import geoip2.database

reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
response = reader.city('140.127.218.198')
print response.country.iso_code
response.country.name
response.subdivisions.most_specific.name
response.subdivisions.most_specific.iso_code
response.city.name
print response.location.latitude
print response.location.longitude
reader.close()
