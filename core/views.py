from django.shortcuts import render,redirect
from .models import Profile
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib import messages
from datetime import date,datetime
import smtplib
import ssl
import os
from email.message import EmailMessage


gmail_adress = os.environ.get('GMAIL_ADRESS')
gmail_pwd = os.environ.get('GMAIL_PWD')


def send_welcome_email(topic,recipient_email):
    email = EmailMessage()
    email["Subject"] = "Bienvenue dans intro spectro newsletter"
    email["From"] = gmail_adress
    email.add_alternative(f"""\
    <html>
    <head></head>
    <h3>Bienvenue dans notre newsletter !</h3>
    <p>

Nous sommes ravis de vous accueillir parmi notre communauté grandissante. En vous inscrivant à notre newsletter, vous faites partie d'une communauté passionnée et curieuse, prête à découvrir et explorer de nouveaux horizons.

Ici, nous vous promettons des contenus uniques et captivants, soigneusement sélectionnés pour satisfaire votre intérêt et vous tenir informé des dernières tendances, des conseils pratiques et des inspirations.</p>
<p>
Nous sommes impatients de partager cette aventure avec vous. Si vous avez des questions, des suggestions ou si vous souhaitez partager votre expérience avec nous, n'hésitez pas à nous contacter. Nous sommes là pour vous servir.

Une fois encore, bienvenue dans notre newsletter et préparez-vous à l'enrichissement, à l'inspiration et à l'épanouissement.

Bien cordialement,
</p>
<em>L'équipe Intospectro</em>
    
    </html>
    
    """,subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl.create_default_context()) as smtp_server:
        smtp_server.login(gmail_adress,gmail_pwd)
        email["To"] = recipient_email

        smtp_server.send_message(email)
        del email["To"]
        del email["From"]
        del email["Subject"]

topics = [' recette', ' coaching', ' divertissement', ' ecommerce']

def send_subscribed_email(recipient_email,end_date):
    email = EmailMessage()
    email["Subject"] = "Felicitation pour votre souscription"
    email["From"] = gmail_adress
    email.add_alternative(f"""\
    <html>
<head></head>
<h3>Vous venez de souscrire a l'offre premium<h3>
<p><h4>Cher abonné</h4>,

Nous sommes ravis de vous annoncer que vous venez de souscrire à notre offre premium ! Cela signifie que vous aurez accès à un contenu exclusif, des avantages spécialisés et une expérience encore plus enrichissante.
</p>
<p>
Dorénavant, vous recevrez des newsletters premium qui vous fourniront des informations approfondies, des conseils d'experts et des ressources exclusives dans votre(vos) domaine(s) d'intérêt(s).
</p>
<p>
Nous tenons à vous remercier pour votre confiance et votre engagement envers notre newsletter. Votre abonnement premium est une reconnaissance de la valeur que nous vous apportons et nous mettons tout en œuvre pour continuer à vous offrir des contenus de qualité supérieure.
</p>
<p>
Votre souscription prendra fin le {end_date}
</p>
<br>
Cordialement,<br>
L'équipe de la newsletter
</html>
""",subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl.create_default_context()) as smtp_server:
        smtp_server.login(gmail_adress,gmail_pwd)
        email["To"] = recipient_email

        smtp_server.send_message(email)
        del email["To"]
        del email["From"]
        del email["Subject"]


def get_end_date(profile,y=0,m=1):
        end = profile.sub_start_date.month
        kwargs = {}
        kwargs['year'] = profile.sub_start_date.year + y
        kwargs['month'] = profile.sub_start_date.month + m
        kwargs['day'] = profile.sub_start_date.day + 1
        return profile.sub_end_date.replace(**kwargs)


def index(request):
    if request.method == "POST":
        email = request.POST['email']
        topic = request.POST['topic'] 
        
        profile = Profile.objects.create(sub_email=email,
        sub_topic = topic,sub_start_date = datetime.now(),sub_end_date= datetime.now(),sent_free_emails=0,
        sent_prem_emails=0,
        sub=False)
        profile.sub_end_date=get_end_date(profile)
        profile.save()

        messages.info(request,'Votre inscription a été un succès')
        send_welcome_email(topic,email)
        
    return render(request,"core/index.html")

def pricing(request):
    if request.method == "POST":
        email = request.POST['email']
        sub_id = request.POST['sub_id']
        return HttpResponseRedirect(reverse('core:payment',args=[email,sub_id]))
    
    return render(request,"core/pricing.html")

#sub_id is the numer corresponding to the tier the user choosed
def payment(request,email,sub_id):
    emails = []
    profiles = Profile.objects.all()
    
    emails = [p.sub_email for p in profiles]

    if email in emails:
        profile = Profile.objects.get(sub_email = email)
    else:
        profile = Profile.objects.create(sub_email=email,
        sub_topic = 'recette',sub_start_date = datetime.now(),
        sub_end_date= datetime.now(),
        sent_free_emails=0,
        sent_prem_emails=0,
        sub=False)
        profile.sub_end_date=get_end_date(profile)
        profile.save() 
        #send_welcome_email
    if request.method  == 'POST':
        if sub_id == 1:
            topic = request.POST['topic'] 
            profile.sub_topic = topic
            profile.sub = True
            profile.sub_start_date = datetime.now()
            profile.sub_end_date = get_end_date(profile)
            profile.save()
            
        elif sub_id == 2:
            topic = request.POST['topic'] 
            profile.sub_topic = topic
            profile.sub = True
            profile.sub_start_date = datetime.now()
            profile.sub_end_date = get_end_date(profile,y=1,m=0)
            profile.save()
        elif sub_id == 3:
            topic = ''
            for t in topics:
                topic += t
            profile.sub_topic = topic
            profile.sub = True
            profile.sub_start_date = datetime.now()
            profile.sub_end_date = get_end_date(profile)
            profile.save()
        elif sub_id == 4:
            topic = ''
            for t in topics:
                topic += t
            profile.sub_topic = topic
            profile.sub = True
            profile.sub_start_date = datetime.now()
            profile.sub_end_date = get_end_date(profile,y=1,m=0)
            profile.save()    
        elif sub_id == 5:
            try:
                topic1 = request.POST['topic1']
            except:
                topic1 = ''
            try:
                topic2 = request.POST['topic2']
            except:
                topic2 = ''
            try:
                topic3 = request.POST['topic3']
            except:
                topic3 = ''
            try:
                topic4 = request.POST['topic4']
            except:
                topic4 = ''          
            chosed_topics = topic1 +' '+' '+topic2 +' '+topic3+' '+topic4

            months = request.POST['months']
            months = int(months)
            profile.sub_topic = chosed_topics
            profile.sub = True
            profile.sub_start_date = datetime.now()
            profile.sub_end_date = get_end_date(profile,y=0,m=months)
            profile.save() 
        send_subscribed_email(profile.sub_email,profile.sub_end_date)    
            
    subscription_id = sub_id
    context = {'sub_id':subscription_id,'profile':profile}    
    return render(request,"core/payment.html",context)

#def paid(request):
    #take the data from payment.html and change sub to True for the user once the payment is successful
    # ajust start and end_dates for the premium subscription 
    # send a sucess message and redirect user to price list 
#    pass