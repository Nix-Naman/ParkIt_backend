import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("acc_key.json")
firebase_admin.initialize_app(cred)

db=firestore.client();

doc_ref=db.collection("Parking_Data").document('Indore')

def addSpot(data):
    print(type(data))
    x=[bool(d) for d in data]
    doc_ref.update(
      {
          'parking1': x
      }  
    )
