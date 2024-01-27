from core.models import Profile
from datetime import date,datetime
from django.utils import timezone




def run():
    all_p = Profile.objects.all()
    
    all_p[0].sub_end_date = datetime.now()
    kwargs = {} #timezone.now() #int(datetime.now().strftime('%Y'))
    #all_p[0].save()
    end_date = all_p[0].sub_start_date.month + 1
    kwargs['year'] = 2024
    kwargs['month'] = end_date 
    kwargs['day'] = all_p[0].sub_start_date.day 
    #dt = datetime.now().replace(**kwargs)
    #print(all_p[0].sub_end_date.replace(**kwargs))
    print(datetime.now())
    all_p[0].save()
    #print(timezone.now().month + 2)
# d = datetime(2024,1,24)
# print(d.year)
# class Profile():
#     def __init__(self,email,sub_topic,sent_emails):
#         self.sub_email = email
#         self.sub_topic = sub_topic
#         self.sent_emails = sent_emails
#     def incr_sent(self):
#         self.sent_emails += 1    

# p1 = Profile("melidaletha@gmail.com","coaching",0)
# p2 = Profile("denzeldecode@gmail.com","coaching",1)
# p3 = Profile("emma@gmail.com","recettes",0)
# profile_list = [p1,p2,p3]

# emails = [p.sub_email for p in profile_list]
# print(emails)


