import wx

class panel_Login(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)
        

        mainBox = wx.BoxSizer(wx.VERTICAL)
        textAndBox = wx.StaticBox(self, id = wx.ID_ANY,label='Login')
        textAndBoxSizer = wx.StaticBoxSizer(textAndBox, wx.HORIZONTAL )
        boxTextGui = wx.BoxSizer(wx.VERTICAL)

        # buttonAndBox = wx.StaticBox(self, id=wx.ID_ANY, label='')
        # buttonAndBoxSizer = wx.StaticBoxSizer(buttonAndBox,wx.VERTICAL)
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
        

        self.username = wx.StaticText(self,label='Username')
        self.username.SetFont(font)
        self.username.SetForegroundColour('#00aa00')

        self.usernameText = wx.TextCtrl(self)
        self.password = wx.StaticText(self,label='Password')
        self.password.SetFont(font)
        self.password.SetForegroundColour('#00aa00')

        self.passwordText = wx.TextCtrl(self,style=wx.TE_PASSWORD)
        self.back = wx.Button(self,label='< Back')
        self.back.Bind(wx.EVT_BUTTON, self.backButton)
        self.login = wx.Button(self,label='Login')
        self.login.Bind(wx.EVT_BUTTON,self.loginAction)
        self.newUser = wx.Button(self,label='New User')
        self.newUser.Bind(wx.EVT_BUTTON,self.newUserAction)

        boxTextGui.Add(self.username,1,wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER,70)
        boxTextGui.AddStretchSpacer(1)

        boxTextGui.Add(self.usernameText,0, wx.LEFT | wx.RIGHT | wx.EXPAND,10)
        boxTextGui.AddStretchSpacer(1)
        boxTextGui.Add(self.password,0,wx.ALL | wx.CENTER,5)
        boxTextGui.AddStretchSpacer(1)

        boxTextGui.Add(self.passwordText,0,wx.LEFT | wx.RIGHT | wx.EXPAND,10)

        buttonSizer.Add(self.back ,0,wx.ALL | wx.ALIGN_BOTTOM, 20)
        buttonSizer.Add(self.login,0,wx.ALL | wx.ALIGN_BOTTOM,20)
        buttonSizer.Add(self.newUser,0,wx.ALL| wx.ALIGN_BOTTOM,20)
        
        #boxnew.Add(12,0,wx.EXPAND,0)
        #gridSizer.Add(boxnew,1,wx.ALL | wx.EXPAND)
        #self.SetSizer(gridSizer)
        

        #self.SetBackgroundColour('#ededef')
        #self.SetSizerAndFit(gridSizer)
        textAndBoxSizer.Add(boxTextGui,0, wx.ALL ,20)
        # buttonAndBoxSizer.Add(buttonSizer,0,wx.ALL ,5)

        mainBox.Add(textAndBoxSizer,0, wx.LEFT | wx.RIGHT | wx.BOTTOM  , 90)
        # mainBox.Add(buttonAndBoxSizer,0,wx.ALL ,5)
        mainBox.Add(buttonSizer,0, wx.LEFT | wx.RIGHT | wx.BOTTOM ,60)
        self.SetSizerAndFit(mainBox)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # panelSizer = wx.BoxSizer(wx.HORIZONTAL)
        # gridSizer = wx.GridBagSizer(5,6)

        # self.username = wx.StaticText(self,label='Reg ID/Email')
        # self.password = wx.StaticText(self,label='Password')
        # self.usernameText = wx.TextCtrl(self)
        # #self.Bind(wx.MOUSE_BTN_LEFT,self.erasePlaceHolderText)
        # self.passwordText = wx.TextCtrl(self,style=wx.TE_PASSWORD)
        # self.back = wx.Button(self, label='< Back')
        # self.back.Bind(wx.EVT_BUTTON, self.backButton)
        # self.login = wx.Button(self,label='Login')
        # self.login.Bind(wx.EVT_BUTTON,self.loginAction)
        # self.newUser = wx.Button(self,label='New User')
        # self.newUser.Bind(wx.EVT_BUTTON,self.newUserAction)

        # self.Line = wx.StaticLine(self,id=wx.ID_ANY, style=wx.LI_HORIZONTAL)
        # self.Line.SetSize((100,100))
    
        # gridSizer.Add(self.username,pos=(1,1),span=(1,1))
        # gridSizer.Add(self.usernameText,pos=(1,3),span=(1,3),flag=wx.EXPAND | wx.LEFT|wx.RIGHT, border=10)
        # gridSizer.Add(self.password,pos=(2,1),span=(1,1))
        # gridSizer.Add(self.passwordText,pos=(2,3),span=(1,3),flag=wx.EXPAND | wx.LEFT|wx.RIGHT, border=10)
        # gridSizer.Add(self.Line, pos=(3,1), span=(1,10),flag=wx.EXPAND)
        # gridSizer.Add(self.back,pos=(4,1),span=(1,1))
        # gridSizer.Add(self.login,pos=(4,4),span=(1,1))
        # gridSizer.Add(self.newUser,pos=(4,5),span=(1,1),flag=wx.LEFT|wx.RIGHT, border=5)

        # self.SetBackgroundColour('#ededef')
        # self.SetSizerAndFit(gridSizer)
        
        # panelSizer.Add(gridSizer,flag=wx.ALL,border=15)
        
