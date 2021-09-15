# oh holy creation

primes=[]
dsv=[]
import math
import time
from pygame import mixer
def datasorter_startup():
      while True:
            menu='''
Data Sorter:

1: Displays data
2: Sorts the data from highest integer value to lowest
3: Sorts the data from lowest integer value to highest
4: Displays highest and lowest values
5: Displays sum of values
6: Displays the average of the values
7: Enter data
8: Save data
9: Load data
10: Exit DataSorter

Enter your command
'''
            command=getint(menu,valuemin=1,valuemax=10)
            if command==1:
                  display_data()
            if command==2:
                  sort_htl()
            if command==3:
                  sort_lth()
            if command==4:
                   min_max()
            if command==5:
                  data_total()
            if command==6:
                  data_average()
            if command==7:
                  get_data(getint('How many packages will you input?\n'))
            if command==8:
                  savedata_location()
            if command==9:
                  path = input('Which file do you want to read?\n')
                  if path.upper == 'NED':
                        path = ('C:\\Users\\nedfp\\OneDrive\\Desktop\\Ned\\Happy Electron\\python\\projects\\poopybumbum-inator\\saved data\\'+input('File name?'))
                  load_data(path)
            if command==10:
                  break
def display_data():
      print('Displaying all values currently active\n')
      count=1
      for value in dsv:
            print('Value '+str(count)+' is set to '+str(value))
            count=count+1
def sort_htl():
      for sortpass in range(0, len(dsv)):
            doneswap=False
            for count in range(0, len(dsv)-1-sortpass):
                  if dsv[count]<dsv[count+1]:
                        temp=dsv[count]
                        dsv[count]=dsv[count+1]
                        dsv[count+1]=temp
                        doneswap=True
            if doneswap==False:
                  break
      print("The data has been sorted from highest to lowest. To see results, use command '1'.\n")
def sort_lth():
      for sortpass in range(0, len(dsv)):
            doneswap=False
            for count in range(0, len(dsv)-1-sortpass):
                  if dsv[count]>dsv[count+1]:
                        temp=dsv[count]
                        dsv[count]=dsv[count+1]
                        dsv[count+1]=temp
                        doneswap=True
            if doneswap==False:
                  break
      print("The data has been sorted from lowest to highest. To see results, use command '1'.\n")
def min_max():
      print('The smallest value is ',min(dsv),'\nThe largest value is ',max(dsv))
def data_total():
      total=0
      for count in dsv:
            total=total+count
      print(total)
def data_average():
      total=0
      for count in dsv:
            total=total+count
      average=total/len(dsv)
      print('Average value is ', average)
def get_data(data_no):
      dsv.clear()
      for count in range(1,data_no+1):
            prompt=('Enter data package '+ str(count)+':\n')
            dsv.append (getint(prompt))
def save_data(filepath, whichlist):
      outputfile=open(filepath,'w')
      for value in whichlist:
            outputfile.write(str(value)+'\n')
      outputfile.close
def savedata_location():
      path = input('Where would you like the file saved?\n')+input('What will you name your file?')
      path = path,'.txt'
      if path=='ned' or 'Ned':
            path='C:\\Users\\nedfp\\OneDrive\\Desktop\\Ned\\Happy Electron\\python\\projects\\poopybumbum-inator\\saved data'+input('File name?')
      if name=='PM' or 'PRIMENUMBER' or 'PRIME':
            whichlist=primes
      else:
            whichlist=dsv
      save_data(path, whichlist)
def load_data(filepath):
      dsv.clear
      outputfile=open(filepath, 'r')
      for line in outputfile:
            dsv.append (line)
      outputfile.close
def himalayan_goat():
      mixer.init()
      mixer.music.load("scmest.mp3")
      mixer.music.set_volume(1)
      mixer.music.play()
      print('*goat scream onslaught ended*\n\nnow try the program again')
def getint(prompt, valuemin='n/a', valuemax='n/a'):
      '''Takes in input from the user\nConverts it to an integer value\nRejects invalid strings\nEnsures the integer is within the min and max range\nDenies keybpard interupts'''
      while True:
            try:
                  numbertxt=input(prompt)
                  try:
                        numberint=int(numbertxt)
                  except ValueError:
                        print('Invalid number. Please enter digits')
                        continue
                  if valuemax!=('n/a'):
                        if numberint>int(valuemax):
                              print('Value too large')
                              print('Maximum value is',valuemax)
                              continue
                  if valuemin!=('n/a'):
                        if numberint<int(valuemin):
                              print('Value too small')
                              print('The minimum value is',valuemin)
                              continue
                  return numberint
            except KeyboardInterrupt:
                  print('Do not use ctr+c! This attempts to kill the prgram!')

def getfloat(prompt, valuemin, valuemax):
      '''Takes in input from the user\nConverts it to an float value\nRejects invalid strings\nEnsures the real number is within the min and max range'''
      while True:
            try:
                  numbertxt=input(prompt)
                  try:
                        numberfloat=float(numbertxt)
                  except ValueError:
                        print('Invalid number. Please enter digits')
                        continue
                  if numberfloat>float(valuemax):
                        print('Value too large')
                        print('Maximum value is',valuemax)
                        continue
                  if numberfloat<float(valuemin):
                        print('Value too small')
                        print('The minimum value is',valuemin)
                        continue
                  return numberfloat
            except KeyboardInterrupt:
                  print('Do not use ctr+c! This attempts to kill the prgram!')
def times_table(value, limit):
      count = 1
      while int(count) <= int(limit):
            result = int(value)*int(count)
            if(result!=69):
                  print(value,'times',count,'equals',result)
            if(result==69):
                  print(value,'times',count,'equals',result,'(lmao 69 nice)')
            count = int(count+1)
yes_no = 'n/a'
def isprime(number):
      if (number<2):
            return False
      for num in range(2, int(math.sqrt(number))+1):
            if (number%num==0):
                  return False
      return True
def listprimes():
      minimum=getint('Enter lower limit: ')
      maximum=getint('Enter upper limit: ')
      for no in range(minimum, maximum):
            if isprime(no):
                  primes.append(no)
def displayprimes():
      while True:
            listprimes()
            viewlist=input('Would you like to view the list? (y/n)')
            if viewlist=='y':
                  for line in primes:
                        print(line)
                  break
            if viewlist=='n':
                  break
            else:
                  print("Please enter either 'y' or 'n'")
while True:
      name = input('Enter your first name: ')
      yes_no = input('Confirm, name is "'+name+'"? (y/n)\n')
      name = name.replace(' ', '')
      while (yes_no == 'y'):
            if (name.upper() != 'NED' and name.upper()!='PM' and name.upper()!='CALCULATOR' and name.upper()!='AHIMALAYANGOAT' and name.upper()!='DS' and name.upper()!='DATASPRTER'):
                  print ('Thankyou. Please wait...')
                  time.sleep(3)
                  print('\n\n\n',name,'is a poopy bum bum\n')
                  break
            elif name.upper() == 'PRIME' or name.upper()=='PM':
                  primes.clear
                  displayprimes()
                  while True:
                        yesno=input('save list? (y/n)')
                        if yesno=='y':
                              savedata_location()
                              break
                        if yesno=='n':
                              break
                        else:
                              print('Please enter a valid response (y/n)')
                              continue
                  break
            elif name.upper() == 'AHIMALAYANGOAT':
                  himalayan_goat()
                  yes_no = 'n/a'
            elif name.upper() == 'DATASORTER' or name.upper()=='DS':
                  datasorter_startup()
                  break
            elif name.upper() == 'CALCULATOR':
                  value = input('no.1?\n')
                  limit = input('no.2?\n')
                  times_table(value,limit)
                  print('\n')
                  time.sleep(1)
                  break
            while name.upper() == 'NED':
                  print('Bullshit, Ned wrote this code!')
                  name = input ('''what's your real name?\n''')
                  name = name.replace(' ', '')
                  yes_no = input('confirm, name is "'+name+'"? (y/n)')
                  if (yes_no == 'n'):
                        print("but... we asked you to enter your own name... how'd you mess that up?\n")
                        continue
                  elif (yes_no != 'y') and (yes_no != 'n'):
                        print("we asked for s 'y' or an 'n'. this is not a 'y' or an 'n'.")
                        continue
      if yes_no.upper()!='Y' and yes_no.upper()!='N':
            print("Please enter either 'y' or 'n'")
            continue
