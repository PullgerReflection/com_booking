from django.db import models
#import pgtrigger

'''
@pgtrigger.register(
    pgtrigger.Trigger(
        name='test1',
        when=pgtrigger.Before,
        operation=pgtrigger.Insert,
        func="NEW.uuid = uuid_generate_v4(); RETURN NEW;",
        # Don't increment version on redundant updates.
        #condition=pgtrigger.Condition('OLD.* IS DISTINCT FROM NEW.*')
    )
)
'''

class hotels(models.Model):
    uuid = models.CharField(max_length=36, primary_key = True) 
    country = models.CharField(max_length=2) 
    id_name = models.CharField(max_length=150) 

'''
@pgtrigger.register(
    pgtrigger.Trigger(
        name='test1',
        when=pgtrigger.Before,
        operation=pgtrigger.Insert,
        func="NEW.uuid = uuid_generate_v4(); RETURN NEW;",
        # Don't increment version on redundant updates.
        #condition=pgtrigger.Condition('OLD.* IS DISTINCT FROM NEW.*')
    )
)
'''

class reviews(models.Model):    
    uuid = models.CharField(max_length=36, primary_key = True) 
    uuid_reviews = models.CharField(max_length=30)
    hotels_uuid = models.CharField(max_length=36) 
    #hotels_uuid = models.ForeignKey(hotels, on_delete=models.CASCADE) 
    userName = models.CharField(max_length=36, null=True)
    post_date = models.DateTimeField(null=True)
    review_bad = models.TextField(null=True)
    review_bad_lang = models.CharField(max_length=5, null=True)
    review_good = models.TextField(null=True)
    review_good_lang = models.CharField(max_length=5, null=True)
    
    
    