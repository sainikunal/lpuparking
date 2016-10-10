import wx


class parking(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)

        panelSizer = wx.BoxSizer(wx.VERTICAL)
        gridBagSizer = wx.GridBagSizer(10,10)

####    Text and TextBox declaration
        self.regNo = wx.StaticText(self,label='Reg no')
        self.block = wx.StaticText(self,label='Block')
        self.rupees = wx.StaticText(self,label='Price')
        self.vehicelType = wx.StaticText(self,label='Vehicle Type')
        self.rupeeLabel = wx.StaticText(self,label='No vehicle selected',style=wx.ALIGN_CENTER) 
        self.rupeeLabel.SetForegroundColour('red')
        self.regNoText = wx.TextCtrl(self)
        blocks = ['--Select--','Block 31','Block 32','Block 33']
        self.blockMenu = wx.Choice(self,choices=blocks)       
        

####    Set the default choice as 1st element and Bind the events
        self.blockMenu.SetSelection(0)
        self.blockMenu.Bind(wx.EVT_CHOICE, self.chooseBlock)
        vehicle = ['--Select--','Two Wheeler','Four Wheeler']
        self.vehicleMenu = wx.Choice(self,choices=vehicle)
        self.vehicleMenu.Bind(wx.EVT_CHOICE,self.chosenVehicle)
        self.vehicleMenu.SetSelection(0)

####    Create Buttons and Bind them
        self.order = wx.Button(self,label='Order')
        self.order.Bind(wx.EVT_BUTTON,self.newParkingRequest)
        self.cancel = wx.Button(self,label='Cancel')
        self.Bind(wx.EVT_BUTTON,self.cancelRequest)
        

        gridBagSizer.Add(self.regNo,pos=(1,1),span=(1,1),flag= wx.LEFT|wx.RIGHT, border=5)
        gridBagSizer.Add(self.regNoText,pos=(1,3),span=(1,5),flag=wx.EXPAND | wx.LEFT|wx.RIGHT, border=5)
        gridBagSizer.Add(self.block,pos=(2,1),span=(1,1),flag= wx.LEFT|wx.RIGHT, border=5)
        gridBagSizer.Add(self.blockMenu,pos=(2,3),span=(1,5),flag=wx.EXPAND | wx.LEFT|wx.RIGHT, border=5)
        gridBagSizer.Add(self.vehicelType,pos=(3,1),span=(1,1),flag= wx.LEFT|wx.RIGHT, border=5)
        gridBagSizer.Add(self.vehicleMenu,pos=(3,3),span=(1,5),flag=wx.EXPAND | wx.LEFT|wx.RIGHT, border=5)
        gridBagSizer.Add(self.rupees,pos=(4,1),span=(1,1),flag= wx.LEFT|wx.RIGHT, border=5)
        gridBagSizer.Add(self.rupeeLabel,pos=(4,3),span=(1,4),flag=wx.EXPAND | wx.LEFT, border=20)
        gridBagSizer.Add(self.order, pos=(6,4),span=(1,1))
        gridBagSizer.Add(self.cancel,pos=(6,5),span=(1,1),flag=wx.LEFT | wx.RIGHT, border=5)


        self.SetSizerAndFit(gridBagSizer)
        self.SetBackgroundColour('#ededef')
        panelSizer.Add(gridBagSizer)