import wx

class panel_newUser(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,id=wx.ID_ANY,style=wx.TAB_TRAVERSAL)

        #self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
        #vSizer = wx.BoxSizer(wx.VERTICAL)
        #hSizer = wx.BoxSizer(wx.HORIZONTAL)

        #font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        #font.SetPointSize(12)
        panelSizer = wx.BoxSizer(wx.HORIZONTAL)

        flexGrid = wx.GridBagSizer(10,10)

        #### Static Text
        self.name = wx.StaticText(self,label='Name')
        # self.name.SetFont(font)
        self.regNo = wx.StaticText(self,label='Reg No.')
        # self.hostel = wx.StaticText(self,label='Hostel/Block')
        self.gender = wx.StaticText(self, label='Gender')
        self.radioButton1 = wx.RadioButton(self,id=wx.ID_ANY,label='Male')
        self.radioButton2 = wx.RadioButton(self,id=wx.ID_ANY,label='Female')
        self.mobile = wx.StaticText(self,label='Mobile')
        self.email = wx.StaticText(self,label='Email')
        self.newPassword = wx.StaticText(self,label='New Password')
        self.newPasswordConfirm = wx.StaticText(self,label='Confirm Password')

        self.line = wx.StaticLine(self)

        #self.warningLabel = '!'
        #self.warningLabel.SetForegroundColour('red')

        #### Input fields
        self.nameText = wx.TextCtrl(self,id=wx.ID_ANY)
        self.regNoText = wx.TextCtrl(self)
        # blocks = ['--Select--','Block 34','Block 33','Block 32']
        # self.hostelText  = wx.Choice(self,choices=blocks)

        #set the default value of choice as 1st element
        # self.hostelText.SetSelection(0)
        # self.Bind(wx.EVT_CHOICE,self.onCheck)
        self.mobileText  = wx.TextCtrl(self)
        self.emailText  = wx.TextCtrl(self)
        self.newPasswordText = wx.TextCtrl(self,style=wx.TE_PASSWORD)
        self.newPasswordConfirmText = wx.TextCtrl(self,style=wx.TE_PASSWORD)
        
        #### Button declaration
        #imageButton = wx.Image('image.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #self.register = wx.BitmapButton(self,wx.ID_ANY,imageButton)
        boxForButton = wx.BoxSizer(wx.HORIZONTAL)
        self.register = wx.Button(self,label='Register')
        self.register.Bind(wx.EVT_BUTTON,self.registerUser)
        self.back = wx.Button(self,label='< Back')
        self.back.Bind(wx.EVT_BUTTON, self.backButton)

        
        boxForButton.Add(self.back,0,wx.ALL | wx.CENTER,5)
        boxForButton.Add(self.register,0,wx.ALL | wx.CENTER,5)


        #### Adding Text and Input to the GridBagSizer
        flexGrid.Add(self.name,pos=(1,1),span=(1,1),flag=wx.RIGHT, border=4)
        flexGrid.Add(self.nameText,pos=(1,3),span=(1,4),flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=4)
        flexGrid.Add(self.regNo,pos=(2,1),span=(1,1))
        flexGrid.Add(self.regNoText,pos=(2,3),span=(1,3),flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=4)
        # flexGrid.Add(self.hostel,pos=(3,1),span=(1,1))
        # flexGrid.Add(self.hostelText,pos=(3,3),span=(1,4),flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=4)
        flexGrid.Add(self.gender,pos=(3,1),span=(1,1))
        flexGrid.Add(self.radioButton1,pos=(3,3),span=(1,1))
        flexGrid.Add(self.radioButton2,pos=(3,4),span=(1,4),flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=4)
        flexGrid.Add(self.mobile,pos=(4,1),span=(1,1))
        flexGrid.Add(self.mobileText,pos=(4,3),span=(1,3),flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=4)    
        flexGrid.Add(self.email,pos=(5,1),span=(1,1))
        flexGrid.Add(self.emailText,pos=(5,3),span=(1,5),flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=4)
        flexGrid.Add(self.newPassword,pos=(6,1),span=(1,1))
        flexGrid.Add(self.newPasswordText,pos=(6,3),span=(1,5),flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=4)
        flexGrid.Add(self.newPasswordConfirm,pos=(7,1),span=(1,1))
        flexGrid.Add(self.newPasswordConfirmText,pos=(7,3),span=(1,5),flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=4)

        #flexGrid.Add(self.line,pos=(8,0),span=(1,5),flag=wx.RIGHT|wx.LEFT,border=5)
        flexGrid.Add(self.back,pos=(10,1),span=(1,1))
        flexGrid.Add(self.register,pos=(10,6),span=(1,1),flag=wx.LEFT | wx.RIGHT, border=4)

        self.SetSizerAndFit(flexGrid)
        self.SetBackgroundColour('#ededef')
        panelSizer.Add(flexGrid,proportion=0,flag=wx.ALL|wx.EXPAND,border=15)
