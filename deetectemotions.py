########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64,json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b5b37e9ca5fb44f69bd0a421356e600f',
}
"""
below parameters for the 
"""
params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    
    'returnFaceAttributes': 'gender,emotion, glasses, age, facialHair, smile',
    'returnRecognitionModel': 'false',
    'detectionModel': 'detection_01',
    
})
"""
pass linkedin url 3 of them
"""
urlo=["https://media-exp1.licdn.com/dms/image/C4E03AQGEgXxIOj1RNw/profile-displayphoto-shrink_800_800/0/1604764065385?e=1617235200&v=beta&t=U62KpD7QjE7RfZ-JB6gG3cFOkKoyIBTcMzsb9LSdERg","https://media-exp1.licdn.com/dms/image/C5603AQH65OSX923CVQ/profile-displayphoto-shrink_800_800/0/1588008960533?e=1617235200&v=beta&t=odGh-5dWKgqUBdm2M21O-pK3R-hnzL19V0eoGcXmQSY","https://media-exp1.licdn.com/dms/image/C5603AQHv9IK9Ts0dFA/profile-displayphoto-shrink_800_800/0/1517497547164?e=1617235200&v=beta&t=rjlXWcuZOZOXp1mZXnPYKchV5WZT8d9WjwIkpOi2YI0"]
for x in range(0,len(urlo)):
   body = { 'url': urlo[x] } 
   newbody =str(body)
   """
   type in the location of the server
   """
   try:
        conn = http.client.HTTPSConnection('australiaeast.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, newbody, headers)
        response = conn.getresponse()
        data = response.read()
        parsed = json.loads(data)
        print("Photo "+str(x+1))
        print ("Response:") 
        print (json.dumps(parsed, sort_keys=True, indent=2)) 
        conn.close()
   except Exception as e:
            print(e)

####################################