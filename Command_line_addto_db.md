# In flask Shell

>>> from TWITOFF.models import *
>>> DB.create_all() # creates sqlite database! (only do once
>>> u1=User(name='austen', id=5452)
>>> t1=Tweet(text='Go DSPT3 Cohort', id=3)
>>> DB.session.add(u1)
>>> DB.session.add(t1)
>>> DB.session.commit()
