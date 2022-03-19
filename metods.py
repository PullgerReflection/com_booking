from djPullgerReflection.com_booking.models import reviews
from djPullgerReflection.com_booking.models import hotels

def isReviewExist(uuid_reviews):
    if len(reviews.objects.filter(uuid_reviews = uuid_reviews).all()) == 0:
        return False;
    else:
        return True;
    
def isHotelExist(hotels_uuid):
    if len(hotels.objects.filter(uuid = hotels_uuid)) == 0:
        return False;
    else:
        return True;

def getAllHotels():
    return hotels.objects.all()
    
def appendReview(inHotelUUID, inData):
    
    createRow = reviews();
    createRow.hotels_uuid = inHotelUUID;
   
    if isinstance(inData, dict):
        useDict = True;
    else:
        useDict = False;
    
    for reviewsField in reviews._meta.get_fields():
        fieldName = reviewsField.name;
        
        if fieldName == "hotels_uuid":
            continue; 
        
        print("Field name: " + fieldName) 
        if useDict == True:
            if fieldName in inData:
                fieldDATA = inData[fieldName];
            else:
                continue; 
        else:
            if hasattr(inData , fieldName):
                fieldDATA = getattr(inData , fieldName)
                print("Field [" + fieldName+ "] = " + str(fieldDATA))
            else:
                print("No attribute: " + fieldName)
                continue;

        setattr(createRow, fieldName, fieldDATA);
    
    createRow.save();
     
    #appendReview