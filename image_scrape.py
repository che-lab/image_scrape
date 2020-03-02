import pandas as pd
import google_streetview.api
import os



#https://maps.googleapis.com/maps/api/streetview?size=1200x800&pano=iOsxtpWAa-yq5of4v9BJRg&key=AIzaSyCfCXdXfjYPd8nAii9dPFVPUjYIBzBf4vo

images = pd.read_csv('data/2017-panorama.csv')

images.head()

#TODO ADD METADATA TO CSV


#for i in images['panoramaID'].head(5):
#    params = [{
#            'size': '640x640',
#            'pano': i,
#            'key': 'AIzaSyCfCXdXfjYPd8nAii9dPFVPUjYIBzBf4vo'}]
#
#    api_list = google_streetview.helpers.api_list(params) 
#    
#    results = google_streetview.api.results(api_list)
#    
#    
#    results.download_links('downloads')
#    os.rename('downloads/gsv_0.jpg', 'downloads/hello.jpg')
#    results.save_metadata('metadata.json')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#pans = images['panoramaID']
#pans.iloc[:5]
#
#params = [{
#        'size': '640x640',
#        'pano': pans.iloc[:5],
#        'key': 'AIzaSyCfCXdXfjYPd8nAii9dPFVPUjYIBzBf4vo'}]
#
#api_list = google_streetview.helpers.api_list(params)
#
#results = google_streetview.api.results(api_list)
#results.download_links('downloads')
#results.save_metadata('metadata2.json')