from instabot import Bot,utils
import getpass
import argparse
import os
import sys

bot = Bot()

bot.login(username=input('Enter your Instagram Username: '), password=getpass.getpass('Securely Enter Your Password: '))

i=1
while i!=0:
 print ("1 for Following User ")
 print ("2 for Unfollowing All Users ")
 print ("3 to send message to User ")
 print ("4 to Upload Instagram Post ")
 print ("5 to Get Follower Details of a user in a file format ")
 print ("6 for Unfollowing User ")
 print ("7 for DM Bomb :)")
 print ("8 for downloading user posts :)")
 print ("0 to Exit ")

 i = input("Enter your value: ")
 
 if i=='0':
     break
      
 elif i=='1':
    uname=input(' Enter Username: ')
    bot.follow(uname)
    
 elif i=='2':
    bot.unfollow_everyone()
    
 elif i=='3':
    uname=input('Enter Username:  ')
    mess=input('Enter Message: ')
    bot.send_message(mess, [uname])
    
 elif i=='4':
    path=input('Enter Path Of Picture: ')
    bot.upload_photo(path, caption=input('Enter Caption For Post: '))
    
 elif i=='5':
     uname=input('Enter Username:  ')
     filename=input('Enter Filename: ')
     f = utils.file(filename)
     for username in f:
        following = bot.get_user_following(username)
     f.save_list(following)
    
 elif i=='7':
    uname=input('Enter Username: ')
    mess=input('Enter Message: ')
    count=int(input('Enter Count: '))
    i=0
    while i<count:
     bot.send_message(mess, [uname])
     i=i+1
      
 elif i=='8':
      u_name=input('Enter Username: ')
      medias = bot.get_total_user_medias(u_name)
      bot.download_photos(medias)
      
 else:
    print("Invalid Input")
  
