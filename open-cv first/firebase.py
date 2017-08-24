from firebase import firebase

firebase = firebase.FirebaseApplication('https://project--2968749792503630642.firebaseio.com/', None)
result = firebase.post("data",1)
