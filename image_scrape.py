import pandas as pd
from pandas.io.json import json_normalize
import google_streetview.api
import os

os.chdir('C:/Users/elmsc/Documents/gis/image_scrape')

#https://maps.googleapis.com/maps/api/streetview?size=1200x800&pano=iOsxtpWAa-yq5of4v9BJRg&key=AIzaSyCfCXdXfjYPd8nAii9dPFVPUjYIBzBf4vo

images = pd.read_csv('data/2017-panorama.csv')

images.head()

images['panoramaID'].nunique()

#test = pd.DataFrame()

#test['unique'] = images['panoramaID'] + '_' + images['UID'] + '_' + images['parkName']
#test['unique'].nunique()
#dups = test[test.duplicated(['unique'], keep=False)]
# exactly 210 duplicates

#TODO ADD METADATA TO CSV
meta_col = ['date', 'pano_id', 'status', 'lat', 'lng']
meta = pd.DataFrame(columns = meta_col)
del(meta_col)


for i,j,k in zip(images['panoramaID'],images['UID'],images['parkName']):
    params = [{
            'size': '640x640',
            'pano': i,
            'key': 'AIzaSyCfCXdXfjYPd8nAii9dPFVPUjYIBzBf4vo'}]

    results = google_streetview.api.results(params)
    results.download_links('downloads')
    
    #NEED TO NAME JPG BY UNIQUE ID NOT PANO ID
    
    os.rename('downloads/gsv_0.jpg', 'downloads/' + i + '_' + j + '_' + k .+ 'jpg')
    results.save_metadata('downloads/metadata.json')
    
    temp_meta = pd.read_json('downloads/metadata.json')
    location = pd.DataFrame(json_normalize(temp_meta['location']))

    temp_meta = temp_meta.drop(columns = ['location', 'copyright', '_file'])
    temp_meta = pd.concat([temp_meta,location],axis=1)
    meta = meta.append(temp_meta, ignore_index = True)
    del(location,temp_meta)


meta = meta.rename(columns = {'pano_id': 'panoramaID'})
images = images.merge(meta, on = 'panoramaID', how = 'left')
