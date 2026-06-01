from tracker import data
import pandas as pd
import os

lat = data['iss_position']['latitude']
lon = data['iss_position']['longitude']

cleanData = {
    "Latitude":[lat],
    "Longitude":[lon]
}

df = pd.DataFrame(cleanData)
filename = "sapceStationData.csv"

if not os.path.exists(filename):
    df.to_csv(filename,index= False)
    print("Csv file created")

else:
    df.to_csv(filename,mode='a',header=False, index=False)
    print("Succesfully appended")
