import urllib.request
import xml.etree.ElementTree as ET
import pickle
import difflib
from pprint import pprint as pp


def main():
    # mid = '1f4p3zPa1uU_gRnbQzMAqCZTPzD4' # National Parks
    # mid = '1Zn_fIUf06TLnOshLtZCqdbbHLCo' # CA Parks
    # mid = '1_QU4xcCYTGTszmV4IXMgKeN4uPE' # DG Courses Small
    # mid = '1irCF0iGu0KeGYiGPfqE1RLvvqd4' # DG Courses Large
    mid = '1aJKR8O-8BWOb9uR7p_2UmapNTL6n154B' # Other
    
    url = 'http://www.google.com/maps/d/kml?forcekml=1&mid={}'.format(mid) 
    listOfPlacemarks = []

    with urllib.request.urlopen(url) as response:
        html = response.read()
        root = ET.fromstring(html)
        
    for i in root[0][-1].findall('{http://www.opengis.net/kml/2.2}Placemark'):
        myText = i[0].text.replace('\xa0', '')
        myText = myText.replace('\n', '')
        listOfPlacemarks.append(myText)

    # pp(listOfPlacemarks)

    # Cache the list of Placemarks 
    # with open('listOfPlacemarks.pkl', 'wb') as f:
    #     pickle.dump(listOfPlacemarks, f)

    with open('listOfPlacemarks.pkl', 'rb') as f:
        cachedListOfPlacemarks = pickle.load(f)

    # Quick Tests:
    # cachedListOfPlacemarks.append('test')
    # listOfPlacemarks.append('another')
   
    delta = set(listOfPlacemarks)^set(cachedListOfPlacemarks)

    if delta:
        print('There ARE differences between cached and live placemark list.')
        # pp(delta)
        diff = difflib.Differ().compare(cachedListOfPlacemarks, listOfPlacemarks)
        for i in diff:
            if i[0] != ' ':
                print(i)
        # print('\n'.join(diff))
    else:
        print('There are NO differences between cached and live placemark list.')
        

if __name__ == '__main__':
    main()