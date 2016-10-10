#### built in modules
import csv                      # csv file operations
import numbers
import MySQLdb as mdb
import platform                 
import os                       # To rename the file after check in
import datetime                 # To calculate total parked days
import time                     # To calculate total parked time
import sys
import urllib                   # To 
import mechanize                # For mechanize browser
from bs4 import BeautifulSoup   # For html parser

#### user defined files
#import databaseLogin
import gui
import login
import newuser
import parking_request
import available_parking
import check_in


try:
    import wx
except ImportError:
    print 'Application doesn\'t meet the requirements'
    raise SystemExit

#from PyDictionary import PyDictionary as pyd

######################################
class MainApp(gui.MainFrame):
    def __init__(self,parent):
        gui.MainFrame.__init__(self,parent)
        self.SetTitle('Parking Management')
        
        #self.panelsix = databaseLoginPanel(self)

        ####object of homepage class
        self.panelOne = panel1(self)

        #### Class for new user registration
        self.panelTwo = panel2(self)

        #### Class for login request
        self.panelThree = panel3(self)

        #### Class for new parking request
        self.panelFour = panel4(self)

        #### class to check for available parking
        self.panelFive = panelAvailableParking(self)

        self.checkInObject = userCheckIn(self)        

        #self.panelOne.Show()
        self.panelOne.Show()
        self.panelTwo.Hide()
        self.panelThree.Hide()
        self.panelFour.Hide()
        self.panelFive.Hide()
        self.checkInObject.Hide()
        #self.panelsix.Show()
        
        self.Center()



class panel1(gui.panel_one):
    def __init__(self,parent):
        gui.panel_one.__init__(self,parent)
        self.parent = parent

    #----------------------------------------------------------------------
    def login(self,event):
        if self.IsShown():
            self.parent.SetTitle('Login')
            self.Hide()
            self.parent.panelThree.Show()
    
    #----------------------------------------------------------------------
    def newUser(self,event):
        if self.IsShown():
            self.parent.SetTitle('Registration')
            self.Hide()
            self.parent.panelTwo.Show()

    #----------------------------------------------------------------------
    def availableParking(self,event):
        if self.IsShown():
            self.parent.SetTitle('Available Parking')
            self.Hide()
            self.parent.panelFive.Show()

    #----------------------------------------------------------------------
    def checkInTime(self,event):
        if self.IsShown():
            self.parent.SetTitle('User Check In')
            self.Hide()
            self.parent.checkInObject.Show()

    #----------------------------------------------------------------------
    def OnEraseBackground(self, evt):
        # Add a picture to the background
        dc = evt.GetDC()
 
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("newPhoto.jpg")
        dc.DrawBitmap(bmp, 0, 0)
    

#########################################
class panel2(newuser.panel_newUser):
    def __init__(self,parent):
        newuser.panel_newUser.__init__(self,parent)
        self.parent = parent

    #----------------------------------------------------------------------
    def onCheck(self,event):
        pass
    
    #----------------------------------------------------------------------
    def registerUser(self,event):
        name = self.nameText.GetValue()
        #dict = pyd()
        #nameCopy= dict.meaning(name)
        reg = self.regNoText.GetValue()
        # block = self.hostelText.GetString(self.hostelText.GetSelection())
        mobile = self.mobileText.GetValue()
        email = self.emailText.GetValue()
        password = self.newPasswordText.GetValue()

        #### Changing label colors
        self.name.SetForegroundColour('black')
        self.regNo.SetForegroundColour('black')
        # self.hostel.SetForegroundColour('black')
        self.mobile.SetForegroundColour('black')
        self.email.SetForegroundColour('black')
        self.newPassword.SetForegroundColour('black')
        self.newPasswordConfirm.SetForegroundColour('black')

        #### Validating the input data
        # validName = self.nameValidator(name)
        validReg = self.regValidator(reg)
        validEmail = self.emailValidator(email)
        validMobile = self.mobileValidator(mobile)
        validPassword = self.passwordValidator(password)
        confirmPassword = self.newPasswordConfirmText.GetValue()
        validName = self.nameValidator(name)
        found,foundReg,self.foundEmail,foundMobile = self.checkSameUser()

        if not name and not reg and not mobile and not email and not password:
            self.changeAllLabelToRed()
            emptyDetailMessage = wx.MessageDialog(None,'Please enter your details ', 'Registration',wx.OK)
            emptyDetailMessage.ShowModal()
            emptyDetailMessage.Destroy()

        elif validName or validReg or validMobile or validEmail or validPassword or not found:
            if not name or not reg or not validMobile or not validEmail or not validPassword or password != confirmPassword:
                if not validEmail and not validMobile:
                    self.email.SetForegroundColour('red')
                    self.mobile.SetForegroundColour('red')                    
                    message = wx.MessageDialog(None, 'Email and Mobile is not valid','Error',wx.OK)
                    message.ShowModal()
                    message.Destroy()   
                    self.newPasswordText.Clear()
                    self.newPasswordConfirmText.Clear()
                
                elif not validEmail:
                    self.email.SetForegroundColour('red')
                                        
                    message = wx.MessageDialog(None, 'Email  is not valid','Error',wx.OK)
                    message.ShowModal()
                    message.Destroy()   
                    self.newPasswordText.Clear()
                    self.newPasswordConfirmText.Clear()

                elif not validMobile:
                    self.mobile.SetForegroundColour('red')
                    message = wx.MessageDialog(None, 'Mobile number is not valid','Error',wx.OK)
                    message.ShowModal()
                    message.Destroy()
                    self.newPasswordText.Clear()
                    self.newPasswordConfirmText.Clear()
                
                elif not validPassword:
                    self.newPassword.SetForegroundColour('red')
                    message = wx.MessageDialog(None,'Password must be 6 characters long','Weak Password',wx.OK | wx.ICON_ERROR)
                    message.ShowModal()
                    message.Destroy()
                    self.newPasswordText.Clear()
                    self.newPasswordConfirmText.Clear()
                
                elif password != confirmPassword:
                    self.newPasswordConfirm.SetForegroundColour('red')
                    message = wx.MessageDialog(None, 'Password doesn\'t match','Error',wx.OK)
                    message.ShowModal()
                    message.Destroy()
                    self.newPasswordText.Clear()
                    self.newPasswordConfirmText.Clear()

                else:
                    #### if above all condition fails then change color of all labels

                    self.changeAllLabelToRed()
                    message = wx.MessageDialog(None,'Fill all the details correctly','Empty details',wx.OK)
                    message.ShowModal()
                    message.Destroy()
                    self.newPasswordText.Clear()
                    self.newPasswordConfirmText.Clear()
            
            #### if all entered details are valid then write them to file

            elif validName and validReg and validEmail and validMobile and password == confirmPassword and validPassword and not found:
                
                try:
                    try:
                        
                        OS = platform.system().upper()
                        if OS == 'LINUX':
                            os.system('service mysql start')
                            conn = mdb.connect("localhost","root","","dbms")
                            db = conn.cursor() 
                            tableDialog = wx.TextEntryDialog(None,message='Enter database table name')
                            tableDialog.ShowModal()
                            tableName = tableDialog.GetValue()
                            tableDialog.Destroy()                            
                        try:
                             db.execute("select * from %s"  %(tableName)) 
                             tableMessage = wx.MessageDialog(None,'Table already exists, we are writing the data in same table','Error' ,wx.OK)
                             tableMessage.ShowModal()
                             tableMessage.Destroy()  
                             db.execute("insert into %s values('%s','%s','%s','%s','%s')" %(tableName,email,password,reg,mobile,name))
                             conn.commit()
                        except:
                           
                           db.execute("create table %s(email varchar(20),password varchar(20),reg int, mobile int, name varchar(20))" %(tableName))
                           db.execute("insert into %s values('%s','%s','%s','%s','%s')" %(tableName,email,password,reg,mobile,name))
                           conn.commit()

                            
                    except:
                        
                        message = wx.MessageDialog(None,"Database problem","Error",wx.OK)
                        message.ShowModal()
                        message.Destroy()                 

                    with open('ParkedUsers31.csv','a+') as csvFile:
                        fWrite = csv.writer(csvFile)
                        fWrite.writerow([reg,password,email,mobile,name])
                        csvFile.close()
                    if csvFile.closed:
                        message = wx.MessageDialog(None,'Successfully Registered','Success',wx.OK)
                        message.ShowModal()
                        message.Destroy()
                        self.nameText.Clear()
                        self.regNoText.Clear()
                        # self.hostelText.SetSelection(0)
                        self.mobileText.Clear()
                        self.emailText.Clear()
                        self.newPasswordText.Clear()
                        self.newPasswordConfirmText.Clear()
                        self.Hide()
                        self.parent.panelTwo.Show()
                
                #### if any error occurs while opening the file then show this message

                except:
                    message = wx.MessageDialog(None,'Error occured while processing the data','Error',wx.OK)
                    message.ShowModal()
                    message.Destroy()
            
            #### found = True --> if entered email is already in database 

            elif found:
            
                message = wx.MessageDialog(None,'It seems you are already registered.','Registration',wx.OK)
                message.ShowModal()
                message.Destroy()
            
        '''if  nameCopy:
            message = wx.MessageDialog(None, 'Use your real Name','Error',wx.OK)
            message.ShowModal()
            message.Destroy()'''

    #----------------------------------------------------------------------
    def regValidator(self,reg):
        
        try:
            reg = unicode(reg,'utf-8')
            return False
        except:
            return True

    #----------------------------------------------------------------------
    def checkSameUser(self):
                reg = self.regNoText.GetValue()
                email = self.emailText.GetValue()
                mobile = self.mobileText.GetValue()
                found  = False
                try:
                    with open('RegisteredUsers.csv','r') as csvFile:
                        fRead = csv.reader(csvFile)
                        for row in fRead:
                            if row[2] == reg:
                                found = True
                                return True,reg,email,mobile
                        if not found:
                            return False,reg,email,mobile
                        #if not found:
                        #    return True,reg,email,mobile
                except IOError:
                    return False, reg, email, mobile

    #----------------------------------------------------------------------
    def emailValidator(self,email):
        countAt = email.count('@')
        countDotCom = email.count('.com')
        #countDot = email.count('.')
        if countAt==1 and countDotCom==1:    # and countDot==0:
            return True
        else:
            return False
    
    #----------------------------------------------------------------------
    #### mobile number should not contain more than 10 digits
    def mobileValidator(self,mobile):
        check = bool
        if len(str(mobile)) == 10:   #type(mobile) == int
            return True
        else:
            
            return False

    #----------------------------------------------------------------------
    #### to check the strong password requirements
    #### needs modification to check length it is not the correct way
    def passwordValidator(self,password):
        correct = True
        if len(str(password)) < 6 or len(str(password)) == 0:
            return False
        else:
            return True
        '''for x in password:
            if ord(x) in range(33,122):
                correct = True
            else:
                return False
            if correct == True:
                return True'''

    #----------------------------------------------------------------------
    def nameValidator(self,name):
        if name.isalpha():
            return True
        else:
            return False

    #----------------------------------------------------------------------
    #### Action required when user clicks Back Button
    def backButton(self,event):
        if self.IsShown():
            self.nameText.Clear()
            self.regNoText.Clear()
            # self.hostelText.SetSelection(0)
            self.mobileText.Clear()
            self.emailText.Clear()
            self.newPasswordText.Clear()
            self.newPasswordConfirmText.Clear()

            self.name.SetForegroundColour('black')
            # self.hostel.SetForegroundColour('black')
            self.email.SetForegroundColour('black')
            self.mobile.SetForegroundColour('black')                        
            self.parent.SetTitle("Parking Management")
            self.Hide()
            self.parent.panelOne.Show()

    #----------------------------------------------------------------------
    def changeAllLabelToRed(self):
        self.name.SetForegroundColour('red')
        self.regNo.SetForegroundColour('red')
        # self.hostel.SetForegroundColour('red')
        self.mobile.SetForegroundColour('red')
        self.email.SetForegroundColour('red')
        self.newPassword.SetForegroundColour('red')
        self.newPasswordConfirm.SetForegroundColour('red')


###########################################

class panel3(login.panel_Login):
    def __init__(self,parent):
        login.panel_Login.__init__(self,parent)
        self.parent = parent

    #----------------------------------------------------------------------
    def loginAction(self,event):

        #### if login panel is visible 
        if self.IsShown():
            username = self.usernameText.GetValue()
            password = self.passwordText.GetValue()
            reg = username

            self.username.SetForegroundColour('#00aa00')
            self.password.SetForegroundColour('#00aa00')

            global noMatch
            noMatch = False
            usernameMatch = ''

            #### if both username and password field is null or empty
            if  username=='' and password == '':
                # change the text colour to red and display a dialog
                self.changeUsernamePasswordColourRed()

                message = wx.MessageDialog(None,'Enter username and password.','Login Error',wx.OK | wx.ICON_ERROR)
                message.ShowModal()
                message.Destroy()

            #### if username field is null
            elif username == '' and password != '':
                self.changeUsernameColourRed()

                message = wx.MessageDialog(None,'Enter username','Login Error',wx.OK | wx.ICON_ERROR)
                message.ShowModal()
                message.Destroy()

            #### if password field is null
            elif username != '' and password == '':
                self.changePasswordColourRed()  
                message = wx.MessageDialog(None,'Enter password','Login Error',wx.OK | wx.ICON_ERROR)
                message.ShowModal()
                message.Destroy()


            ##### if username and password are not null
            elif username and password:
                try:
                    with open('ParkedUsers31.csv','r') as csvFile:
                        fRead = csv.reader(csvFile)
                        for row in fRead:
                            # row = row.split()
                            if row[0] == username or row[2] == reg:
                                if row[1] == password:
                                    noMatch = True
                                    self.usernameText.Clear()
                                    self.passwordText.Clear()
                                    self.parent.SetTitle('Parking Request')
                                    self.Hide()
                                    self.parent.panelFour.Show()
                                    break
                                else:
                                    usernameMatch = row[0]
                            else:
                                noMatch = False
                        #if usernameMatch != '':
                        try:
                            url = 'http://ums.lpu.in/lpuums'
                        
                            br = mechanize.Browser()
                            br.set_handle_robots(False)
                            br.open(url)
                            br.select_form(name='form1')
                            br['TextBox1']= username
                            br['TextBox2'] = password
                        
                            response = br.submit()
                            content = response.read()
                            
                            soup = BeautifulSoup(content, 'html.parser')
                            count = 0
                            for link in soup.find_all('input'):
                                found = link.get('value')
                                Username = link.get('id')
                                if found == username:
                                    count = count + 1
                                
                            if count >= 2:
                                regNo = self.usernameText.GetValue()
                                self.usernameText.Clear()
                                self.passwordText.Clear()
                                if self.IsShown():
                                    self.parent.SetTitle('Parking Request')
                                    self.Hide() 
                                    self.parent.panelFour.Show()
                            
                            elif count < 2 and noMatch == False:
                                message = wx.MessageDialog(None,'Username/Password is incorrect.','Login Error',wx.OK | wx.ICON_ERROR)
                                message.ShowModal()
                                message.Destroy()
                                self.passwordText.Clear()
                                        
                        except:
                                message = wx.MessageDialog(None,'Please check your internet connection','Error',wx.OK | wx.ICON_ERROR)
                                message.ShowModal()
                                message.Destroy()
                        # self.changePasswordColourRed()
                        # message = wx.MessageDialog(None,'You entered incorrect password','Login Error',wx.OK | wx.ICON_ERROR)
                        # message.ShowModal()
                        # message.Destroy()
                        # self.passwordText.Clear()
                        #elif noMatch == False:

                         #   message = wx.MessageDialog(None,'Invalid credentials details.','Login Error',wx.OK | wx.ICON_ERROR)
                         #   message.ShowModal()
                         #   message.Destroy()
                         #   self.passwordText.Clear()
                except:
                    message = wx.MessageDialog(None, 'It seems that you are not registered','Login',wx.OK)
                    message.ShowModal()
                    message.Destroy()
                    self.passwordText.Clear()
                
           
    ####  Change username, password label color to red

    #----------------------------------------------------------------------
    def changeUsernamePasswordColourRed(self):
        self.username.SetForegroundColour('red')
        self.password.SetForegroundColour('red')      

    #----------------------------------------------------------------------
    def changeUsernameColourRed(self):
        self.username.SetForegroundColour('red')  
    
    #----------------------------------------------------------------------
    def changePasswordColourRed(self):
        self.password.SetForegroundColour('red')
    
    #----------------------------------------------------------------------
    def newUserAction(self,event):

        if self.IsShown():  
            self.usernameText.Clear()
            self.passwordText.Clear()
            self.parent.SetTitle('Registration')
            self.Hide()
            self.parent.panelTwo.Show()


    #----------------------------------------------------------------------
    def erasePlaceHolderText(self,event):
        #if self.usernameText.GetValue() == 'Email or Registraton ID':
        self.usernameText.Clear()
        event.Skip()

    #----------------------------------------------------------------------
    def backButton(self,event):
        if self.IsShown():
            self.username.SetForegroundColour('#00aa00')
            self.password.SetForegroundColour('#00aa00')
            self.usernameText.Clear()
            self.passwordText.Clear()
            self.parent.SetTitle('Parking Management')
            self.Hide()
            self.parent.panelOne.Show()
        else:
            self.panelThree.Show()

    #----------------------------------------------------------------------
    def OnEraseBackground(self, evt):
        
        # Add a picture to the background

        dc = evt.GetDC()
 
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image.jpg")
        dc.DrawBitmap(bmp, 0, 0)


#########################################
####  New Parking Request
class panel4(parking_request.parking):
    def __init__(self,parent):
        parking_request.parking.__init__(self,parent)
        self.parent = parent

    #----------------------------------------------------------------------
    def chooseBlock(self,event):
        block = self.blockMenu.GetString(self.blockMenu.GetSelection())

    #----------------------------------------------------------------------
    def chosenVehicle(self,event):
        info = self.vehicleMenu.GetString(self.vehicleMenu.GetSelection())
        if info == 'Two Wheeler':
            self.rupeeLabel.SetLabel('5 Rupees / day')
            self.rupeeLabel.SetForegroundColour('green')
        if info == 'Four Wheeler':
            self.rupeeLabel.SetLabel('10 Rupees / day')
            self.rupeeLabel.SetForegroundColour('green')

    #----------------------------------------------------------------------
    # Action for order button
    def newParkingRequest(self,event):    
        lines = 0
        match = False
        #currentTime = time.ctime()
        currentTime = datetime.datetime.now()
        currentTime = datetime.datetime.strftime(currentTime,' %H:%M')
        currentDate = datetime.date.today()
        currentDate = datetime.date.strftime(currentDate,'%d, %b')
        parkingTime = currentDate + currentTime

        

        regNo = self.regNoText.GetValue()

        block = self.blockMenu.GetString(self.blockMenu.GetSelection())
        vehicleType = self.vehicleMenu.GetString(self.vehicleMenu.GetSelection())
        if block == '--Select--' or vehicleType == '--Select--' or not regNo:
            message = wx.MessageDialog(None,'Please fill all fields','Parking Request',wx.OK)
            message.ShowModal()
            message.Destroy()
        elif regNo and block and vehicleType:
            try:
                with open('ParkedUsers31.csv','a+') as parked:
                    reader = csv.reader(parked)
                    for row in reader:
                        if row[0] == regNo:
                            match = True
                            break
                    if not match:
                        try:
                                ## Set pointer to beginning of file object
                                parked.seek(0,0)
                            # with open('ParkedUsers31.csv','a+') as csvFile:
                                fWrite = csv.writer(parked)
                                reader = csv.reader(parked)

                                # Get the number of lines in file
                                for row in reader:
                                    lines = reader.line_num
                                if (lines < 10):
                                    fWrite.writerow([regNo,block,vehicleType,parkingTime])
                                    successMessage = wx.MessageDialog(None,'You order has been received.','Success',wx.OK)
                                    successMessage.ShowModal()
                                    successMessage.Destroy()
                                    
                                    self.parent.SetTitle('Parking Management')
                                    self.Hide()
                                    self.parent.panelOne.Show()
                                    self.regNoText.Clear()
                                    self.blockMenu.SetSelection(0)
                                    self.vehicleMenu.SetSelection(0)
                                    self.rupeeLabel.SetLabel('No Vehicle Selected')
                                    self.rupeeLabel.SetForegroundColour('red')
                                    
                                else:
                                    message = wx.MessageDialog(None,'Sorry, We have no vacant space in '+ block, 'Availability Error',wx.OK | wx.ICON_ERROR)
                                    message.ShowModal()
                                    message.Destroy()
                        except:
                            message = wx.MessageDialog(None,'Parked Users file not found','File not found',wx.OK)
                            message.ShowModal()
                            message.Destroy()
                    
                    elif match:    
                        messageNotRegistered = wx.MessageDialog(None, "You have already parked a vehicle" , 'Parking Request',wx.OK | wx.ICON_ERROR)    
                        messageNotRegistered.ShowModal()
                        messageNotRegistered.Destroy()
                        

            except:
                message = wx.MessageDialog(self,'File not found','Error',wx.OK)
                message.ShowModal()
                message.Destroy()
            

        ####  Clear all the entries
        # self.regNoText.Clear()
        # self.blockMenu.SetSelection(0)
        # self.vehicleMenu.SetSelection(0)
        # self.rupeeLabel.SetLabel('No Vehicle Selected')
        # self.rupeeLabel.SetForegroundColour('red')
    
    #----------------------------------------------------------------------
    def cancelRequest(self,event):
        reg = self.regNoText.GetValue()
        block = self.blockMenu.GetString(self.blockMenu.GetSelection())
        vehicle = self.vehicleMenu.GetString(self.vehicleMenu.GetSelection())
        if reg or block != '--Select--' or vehicle != '--Select--':
            message  = wx.MessageDialog(None,'All entered data will be lost!!!','Confirm', wx.CANCEL | wx.OK | wx.ICON_EXCLAMATION)
            #message.ShowModal()
            if message.ShowModal() == wx.ID_OK:
                message.Destroy()
                

                ## Clear the entries
                self.regNoText.Clear()
                self.blockMenu.SetSelection(0)
                self.vehicleMenu.SetSelection(0)
                self.rupeeLabel.SetLabel('No Vehicle Selected')
                self.rupeeLabel.SetForegroundColour('red')
                self.parent.SetTitle('Parking Management')
                self.Hide()
                self.parent.panelOne.Show()
            else:
                message.Destroy()

        else:
            self.parent.SetTitle('Parking Management')
            self.Hide()
            self.parent.panelOne.Show()




class panelAvailableParking(available_parking.checkVacancy):
    def __init__(self,parent):
        available_parking.checkVacancy.__init__(self,parent)
        self.parent = parent

    #----------------------------------------------------------------------
    def nextButton(self,event):
        block = self.blockMenu.GetString(self.blockMenu.GetSelection())
        vehicle = self.vehicleMenu.GetString(self.vehicleMenu.GetSelection())

      # if the selection is 0th element i.e. empty  
        if block == '--Select--' or vehicle == '--Select--':
            if block == '--Select--':
                #self.warningLabel.SetForegroundColour('red')
                #self.block.SetLabel('Block/Hostel '+self.warningLabel)
                self.block.SetForegroundColour('red')
            if vehicle == '--Select--':
                self.vehicle.SetForegroundColour('red')
        else:
            pass

    #----------------------------------------------------------------------
    def prevButton(self,event):
        if self.IsShown():
            self.block.SetForegroundColour('black')
            self.vehicle.SetForegroundColour('black')
            self.parent.SetTitle('Parking Management')
            self.blockMenu.SetSelection(0)
            self.vehicleMenu.SetSelection(0)
            self.Hide()
            self.parent.panelOne.Show()


    #----------------------------------------------------------------------
    def OnEraseBackground(self, evt):
        # Add a picture to the background
        dc = evt.GetDC()
 
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("image.jpg")
        dc.DrawBitmap(bmp, 0, 0)

class userCheckIn(check_in.check):
    def __init__(self,parent):
        check_in.check.__init__(self,parent)
        self.parent = parent
    
    #----------------------------------------------------------------------
    def payNow(self, event):
        regNo = self.regNoText.GetValue()
        found = False
        if regNo == '':
            self.regNo.SetForegroundColour('red')
        else:
            currentTime = datetime.datetime.now()
            #currentTime = datetime.datetime.strftime(currentTime,' %H:%M')
            currentDate = datetime.date.today()
            #currentDate = datetime.date.strftime(currentDate,'%d, %b')
            #checkTime   = currentDate + currentTime
            parkedTime  = ''
            #currentTime = time.ctime()

            try:
                with open('ParkedUsers31.csv','r') as inp:
                    for row in csv.reader(inp):
                        if row[0] == regNo:
                            found = True
                            Time = row[3]
                            vehicleType = row[2]
                            parkedDate = datetime.datetime.strptime(Time,'%d, %b  %H:%M')

                            totalDays = abs(currentDate.day - parkedDate.day)
                            totalHours = abs(currentTime.hour - parkedDate.hour)
                            totalMinute= abs(currentTime.minute - parkedDate.minute)

                            if vehicleType == 'Two Wheeler':
                                if totalDays <= 0:
                                    Cost = 5
                                else:
                                    Cost = totalDays * 5
                            elif vehicleType == 'Four Wheeler':
                                if totalDays <= 0:
                                    Cost = 10
                                else:
                                    Cost = totalDays * 10

            except:
                message = wx.MessageDialog(None,'Error occured while processing.','Check In', wx.OK | wx.ICON_ERROR)
                message.ShowModal()
                message.Destroy()
        
        if found:
            if totalDays <= 1:
                checkInTime = datetime.datetime.strftime(currentTime, '%-I:%M %p')
                text = 'You parked you vehicle today at %s. \n\
Parking Cost : %s %s' %(checkInTime,Cost,u"\u20B9")
                message = wx.MessageDialog(None, text,'Confirm', wx.YES_NO | wx.YES_DEFAULT)
                if message.ShowModal() == wx.ID_YES:
                    self.deleteRecord()
                    self.regNoText.SetValue('')
                    # self.regNo.SetForegroundColour('black')
                    self.parent.SetTitle('Parking Management')
                    self.Hide()
                    self.parent.panelOne.Show()
                message.Destroy()
            else:
                # convert string time into datetime format
                checkInTime = datetime.datetime.strptime(Time,'%d, %b %H:%M')

                # convert datetime format into string time format
                # it is converted into 12 hour format
                Time = datetime.datetime.strftime(checkInTime,'%d, %b %-I:%M %p')
                text = 'You parked you vehicle on %s.\n\
Parking Cost : %s %s' %(Time,Cost,u"\u20B9")
                message = wx.MessageDialog(None, text,'Confirm',wx.YES_NO | wx.YES_DEFAULT)
                if message.ShowModal() == wx.ID_YES:
                    self.deleteRecord()
                    self.regNoText.SetValue('')
                message.Destroy()
            
        elif not found and regNo != '':
            text = "%s, It seems you didn\'t parked your vehicle." %(regNo)
            message = wx.MessageDialog(None, text, 'Check In',wx.OK | wx.ICON_ERROR)
            message.ShowModal()
            message.Destroy()

    def deleteRecord(self):
        self.regNo = self.regNoText.GetValue()
        with open('ParkedUsers31.csv','r') as inp, open('Modified.csv','w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if row[0] == self.regNo:
                    pass
                else:
                     writer.writerow(row)
            os.rename('Modified.csv','ParkedUsers31.csv')
                        
    #----------------------------------------------------------------------
    def ViewDetails(self,event):
        found = False
        regNo = self.regNoText.GetValue()
        if not found:
            try:
                with open('ParkedUsers31.csv','r') as csvView:
                    read = csv.reader(csvView)
                    # Get the number of rows from file
                    # rows = list(read)
                    # rowCount = len(rows)
                    
                    for row in read: 
                        if row[0] == regNo:
                            found = True
                            vehicleType = row[2]
                            currentTime = datetime.datetime.now()
                            currentDate = datetime.date.today()
                            Time = row[3]
                            
                            #Format of strptime to convert date(string) into date(date)
                            parkedDate = datetime.datetime.strptime(Time,'%d, %b %H:%M')

                            totalDays = abs(currentDate.day - parkedDate.day)
                            totalHours = abs(currentTime.hour - parkedDate.hour)
                            totalMinute= abs(currentTime.minute - parkedDate.minute)
                            if vehicleType == 'Two Wheeler':
                                Cost = totalDays * 5
                            elif vehicleType == 'Four Wheeler':
                                Cost = totalDays * 10
                            
            except:
                    print ('File Not found')

        # if found = True, means that regNo is in the file 
        if regNo == '':
            self.regNo.SetForegroundColour('red')
        elif found:
            text = "Your vehicle is parked since \n\
 Days      :  %s \n Hours     :  %s \n Minutes  :  %s \n Cost       :  %s %s " %(totalDays,totalHours,totalMinute,Cost,u"\u20B9")
            message = wx.MessageDialog(None, text,'Details',wx.OK)
            message.ShowModal()
            message.Destroy()
                                                    
        # if not True, means that regNo is not in file, show the error message
        elif not found:
            text = "%s, It seems you didn\'t parked your vehicle." %(regNo)
            message = wx.MessageDialog(None, text, 'Check In',wx.OK | wx.ICON_ERROR)
            message.ShowModal()
            message.Destroy()

    #----------------------------------------------------------------------
    def back(self, event):
        self.regNoText.SetValue('')
        # self.regNo.SetForegroundColour('black')
        self.parent.SetTitle('Parking Management')
        self.Hide()
        self.parent.panelOne.Show()

#----------------------------------------------------------------------
def main():
    app = wx.App()
    window = MainApp(None)
    app.MainLoop()

if __name__ == '__main__':
    main()
