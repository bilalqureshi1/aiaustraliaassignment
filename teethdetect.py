import http.client, urllib.request, urllib.parse, urllib.error, base64,json

headers = {
    # Request headers
    'Prediction-Key': '04f34831f904469aad9ec2b923168906',
    'Content-Type': 'application/json',
}

params = urllib.parse.urlencode({
'predictions': '{string}',

})
urlo=["https://media-exp1.licdn.com/dms/image/C4E03AQGEgXxIOj1RNw/profile-displayphoto-shrink_800_800/0/1604764065385?e=1617235200&v=beta&t=U62KpD7QjE7RfZ-JB6gG3cFOkKoyIBTcMzsb9LSdERg","https://media-exp1.licdn.com/dms/image/C5603AQH65OSX923CVQ/profile-displayphoto-shrink_800_800/0/1588008960533?e=1617235200&v=beta&t=odGh-5dWKgqUBdm2M21O-pK3R-hnzL19V0eoGcXmQSY","https://media-exp1.licdn.com/dms/image/C5603AQHv9IK9Ts0dFA/profile-displayphoto-shrink_800_800/0/1517497547164?e=1617235200&v=beta&t=rjlXWcuZOZOXp1mZXnPYKchV5WZT8d9WjwIkpOi2YI0"]
for x in range(0,len(urlo)):

    body = { 'url': urlo[x] } 
    newbody =str(body)

    try:
      conn = http.client.HTTPSConnection('australiaeast.api.cognitive.microsoft.com')
      conn.request("POST","/customvision/v3.0/Prediction/bd8f63f0-6962-4cde-bd1c-871d0dc04157/detect/iterations/Iteration2/url?%s" % params ,newbody, headers)
      response = conn.getresponse()
      data = response.read()
      parsed = json.loads(data) 
      print ("Response: for photo "+str(x+1)) 
      ##print ((json.dumps(parsed, sort_keys=True, indent=2)))
      
      print(parsed['predictions'][0]['tagName'])
      print('probablity: ')
      print(parsed['predictions'][0]['probability'])
      conn.close()
    except Exception as e:
      print(e)

####################################
