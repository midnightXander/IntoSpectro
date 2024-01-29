import smtplib
import ssl
import os
from email.message import EmailMessage
from .contents import *
from datetime import date,datetime
from core.models import  Profile

# gmail_adress = os.environ.get('GMAIL_ADRESS')
# gmail_pwd = os.environ.get('GMAIL_PWD')

gmail_adress = 'intospectro.newsletter@gmail.com'
gmail_pwd = 'zldt fevv sxat bnim'

email = EmailMessage()
email['From'] = gmail_adress

all_profiles = Profile.objects.all()

def send(recipient_email,content,subject):
    email['To'] = recipient_email
    email['Subject'] = subject
    email.add_alternative(content,subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context = ssl.create_default_context()) as smtp_server:
        smtp_server.login(gmail_adress,gmail_pwd)

        smtp_server.send_message(email)
        del email['To']
        del email['Subject']


def dateIsLessEqual(d1,m1,y1,d2,m2,y2):
    isLess = False
    if (y1 < y2):
        isLess = True
    elif y1 == y2:
        if (m1 == m2 and d1 <= d2) or (m1 < m2):
            isLess = True
    return isLess    


def newsletter():
    for p in all_profiles:
        now = datetime.now()
        end_date = p.sub_end_date
        if dateIsLessEqual(now.day,now.month,now.year,end_date.day,end_date.month,end_date.year):     
            i = p.sent_free_emails
            j = p.sent_prem_emails
            c_subject = 'Conseil Coaching du jour'
            r_subject = 'Recette du jour'
            d_subject = 'Blagues du jour'
            e_subject = 'Guide Ecommerce du jour'

    #sending free content 
            if not p.sub:
                
                if 'coaching' in p.sub_topic  and p.sent_free_emails<len(coaching_free_content):
                    send(p.sub_email,coaching_free_content[i],c_subject)

                if ('recette' in p.sub_topic) and p.sent_free_emails<len(recipes_free_content):
                    send(p.sub_email,recipes_free_content[i],r_subject)

                if ('ecommerce' in p.sub_topic) and p.sent_free_emails<len(ecommerce_free_content) :
                    send(p.sub_email,ecommerce_free_content[i],e_subject)

                if ('divertissement' in p.sub_topic) and p.sent_free_emails<len(entertainment_free_content) :
                    send(p.sub_email,entertainment_free_content[i],d_subject)
                p.sent_free_emails += 1

    #sending premium content
            else:
                if ('recette' in p.sub_topic) and p.sent_prem_emails<len(recipes_prem_content):
                    send(p.sub_email,recipes_prem_content[j],r_subject)
                     
                if ('coaching' in p.sub_topic) and p.sent_prem_emails<len(coaching_prem_content):
                    send(p.sub_email,coaching_prem_content[j],c_subject)
                
                if ('ecommerce' in p.sub_topic) and p.sent_prem_emails<len(ecommerce_prem_content):
                    send(p.sub_email,ecommerce_prem_content[j],e_subject)
                    
                if ('divertissement' in p.sub_topic) and p.sent_prem_emails<len(entertainment_prem_content):
                    send(p.sub_email,entertainment_prem_content[j],d_subject)                
                    
                p.sent_prem_emails += 1 
    #increment sent emails and save to database
            
            p.save() 

        else:
            send(p.sub_email,follow_up_content[0],'Votre Souscription')


def run():
    newsletter()
    