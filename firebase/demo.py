from firebase import firebase

firebase = firebase.FirebaseApplication('https://esp8266-31217.firebaseio.com', None)

firebase.post('data', 2)
# firebase.delete("data",None,None,None)
# result = firebase.post("/dien",{"data" : 'a'})
# firebase.put('test/asdf',"count",5)
# firebase.put('demo',"led_1",1)
# firebase.put('demo',"led_2",2)
# firebase.put('demo',"led_3",3)
# firebase.put('demo',"led_4",4)





