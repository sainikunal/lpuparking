import wx


class MainFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,id=wx.ID_ANY,size=wx.Size(450,450),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER|wx.TAB_TRAVERSAL)
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        frameSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(frameSizer)
        #self.Center(wx.BOTH)
        self.SetBackgroundColour('#ededef')
        self.Show()
        #font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        #font.SetPointSize(9)

class panel_one(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,id=wx.ID_ANY,style=wx.TAB_TRAVERSAL)
        # flexGrid = wx.GridBagSizer(4,6)
        #self.SetSizer(panelSizer)
        #flexGrid = wx.FlexGridSizer(3,3,5,5)

        self.SetBackgroundStyle(wx.BG_STYLE_ERASE)

        mainBox = wx.BoxSizer(wx.VERTICAL)
        #textAndBox = wx.StaticBox(self, id = wx.ID_ANY,label='')
        #textAndBoxSizer = wx.StaticBoxSizer(textAndBox, wx.VERTICAL )
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        boxTextGui = wx.BoxSizer(wx.VERTICAL)

        # imagePath = 'newPhoto.jpg'
        # bitmap = wx.Bitmap(imagePath)
        # bitmap = scale_bitmap(bitmap, 600,600)
        # control = wx.StaticBitmap(self, -1, bitmap)

        self.loginButton = wx.Button(self,id=wx.ID_ANY,label='Login')
        self.newUserButton = wx.Button(self,id=wx.ID_ANY, label='New User')
        self.availableParkingButton = wx.Button(self,id=wx.ID_ANY, label='Available Parking')
        self.checkIn = wx.Button(self,id=wx.ID_ANY, label='Check In')

        self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        self.newUserButton.Bind(wx.EVT_BUTTON, self.newUser)
        self.availableParkingButton.Bind(wx.EVT_BUTTON, self.availableParking)
        self.checkIn.Bind(wx.EVT_BUTTON, self.checkInTime)

        boxTextGui.Add(self.loginButton,0,wx.ALL  | wx.EXPAND | wx.LEFT, 7)
        boxTextGui.Add(self.newUserButton,0,wx.ALL  | wx.EXPAND | wx.CENTER, 7)
        boxTextGui.Add(self.availableParkingButton,0,wx.ALL  | wx.CENTER | wx.EXPAND, 7)
        boxTextGui.Add(self.checkIn,0,wx.ALL  | wx.CENTER | wx.EXPAND, 7)


        #textAndBoxSizer.Add(boxTextGui,0,wx.ALL | wx.CENTER, 60)
        sizer.Add(boxTextGui,0, wx.ALL  | wx.CENTER, 70)
        mainBox.Add(sizer, 0, wx.ALL | wx.CENTER, 90)
        
        self.SetSizerAndFit(mainBox)
        self.SetBackgroundColour('#ededef')

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

