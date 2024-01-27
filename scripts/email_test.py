from datetime import date,datetime
from core.models import  Profile
print(datetime.now().strftime('%a'))

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

free_adresses = {"recettes":"melidaletha@gmail.com"}
coaching_free_adresses = []
prem_adresses = {}
coaching_free = ["free1","free2","free3","free4","free5","free6","free7","free8","free9"]
coaching_prem = []
# c_profiles = []
# for p in profile_list:
#     if p.sub_topic == 'coaching':
#         c_profiles.append(p)


coaching_free_content = [
    f"""\<html>
    <head></head>
    <h3>Coaching 1</h3>
    <p>On vous souhaite un bon moment avec nous. Nous allons vous aider a atteindre les sommets que vous voulez atteindre.<br>
    <p>Coaching 1</p>
    
    </html>""",
    f"""\<html>
    <head></head>
    <h3>Coaching 2</h3>
    <p>On vous souhaite un bon moment avec nous. Nous allons vous aider a atteindre les sommets que vous voulez atteindre.<br>
    <p>Coaching 2</p>
    
    </html>""",
    f"""\<html>
    <head></head>
    <h3>Coaching 3</h3>
    <p>On vous souhaite un bon moment avec nous. Nous allons vous aider a atteindre les sommets que vous voulez atteindre.<br>
    <p>Coaching</p>
    
    </html>""",
    f"""\<html>
    <head></head>
    <h3>Coaching 4</h3>
    <p>On vous souhaite un bon moment avec nous. Nous allons vous aider a atteindre les sommets que vous voulez atteindre.<br>
    <p>coaching 4</p>
    <p>Coaching</p>
    
    </html>""",
    ]


c_profiles = Profile.objects.filter(sub_topic = 'coaching')
def send(email,content):
    print(email,":",content)

def run():
    for p in c_profiles:
        i = p.sent_emails
        send(p.sub_email,coaching_free[i])
        p.sent_emails += 1 

