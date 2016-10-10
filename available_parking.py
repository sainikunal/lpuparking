import wx

class checkVacancy(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.frame = parent
        wx.Display_GetFromWindow
        self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
        #mainBox = wx.BoxSizer(wx.HORIZONTAL)
        
        #panel = wx.StaticBox(self)
        #panelSizer = wx.StaticBoxSizer(panel,wx.VERTICAL)
        widgetSizer = wx.GridBagSizer(40,40)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        self.block = wx.StaticText(self,label='Block/Hostel')
        #self.block.SetForegroundColour('green')
        self.block.SetFont(font)
        blocks = ['--Select--','Block 31','Block 32','Block 33','Block 34']
        self.blockMenu = wx.Choice(self,choices=blocks)
        self.vehicle = wx.StaticText(self,label='Vehicle Type')
        #self.vehicle.SetForegroundColour('green')
        self.vehicle.SetFont(font)
        vehicleCategory = ['--Select--','Two Wheeler','Four Wheeler']
        self.vehicleMenu = wx.Choice(self,choices=vehicleCategory)

        #self.warningLabel = wx.StaticText(self,label=' *')
        #self.warningLabel.SetForegroundColour('red')

        self.next = wx.Button(self,label='Next >')
        self.next.Bind(wx.EVT_BUTTON, self.nextButton)
        self.prev = wx.Button(self,label='< Back')
        self.prev.Bind(wx.EVT_BUTTON, self.prevButton)
        self.Exit = wx.Button(self,label='Exit')
        self.Exit.Bind(wx.EVT_BUTTON, lambda event: self.parent.Destroy())
        

        widgetSizer.Add(self.block,pos=(1,1),span=(1,1))
        widgetSizer.Add(self.blockMenu,pos=(1,2),span=(1,1),flag=wx.EXPAND)
        #widgetSizer.Add(self.warningLabel,pos=(1,3),span=(1,1))
        widgetSizer.Add(self.vehicle,pos=(2,1),span=(1,1))
        widgetSizer.Add(self.vehicleMenu,pos=(2,2),span=(1,1))
        widgetSizer.Add(self.prev, pos=(5,1),span=(1,1))
        widgetSizer.Add(self.next, pos=(5,2),span=(1,1))
        widgetSizer.Add(self.Exit, pos=(5,3),span=(1,1))

        self.vehicleMenu.SetSelection(0)
        self.blockMenu.SetSelection(0)
        #widgetSizer.AddGrowableRow(2)
        #panelSizer.Add(widgetSizer,0,wx.ALL | wx.CENTER,5)
        #mainBox.Add(panelSizer,0,wx.ALL | wx.CENTER,5)
        self.SetSizerAndFit(widgetSizer)
        self.SetBackgroundColour('#ededef')

        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)