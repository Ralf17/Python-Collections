#Boa:Frame:ScientificCalcFrame

import wx

def create(parent):
    return ScientificCalcFrame(parent)

[wxID_SCIENTIFICCALCFRAME, wxID_SCIENTIFICCALCFRAMEBTN0, 
 wxID_SCIENTIFICCALCFRAMEBTN1, wxID_SCIENTIFICCALCFRAMEBTN10RAISETOX, 
 wxID_SCIENTIFICCALCFRAMEBTN2, wxID_SCIENTIFICCALCFRAMEBTN3, 
 wxID_SCIENTIFICCALCFRAMEBTN4, wxID_SCIENTIFICCALCFRAMEBTN5, 
 wxID_SCIENTIFICCALCFRAMEBTN6, wxID_SCIENTIFICCALCFRAMEBTN7, 
 wxID_SCIENTIFICCALCFRAMEBTN8, wxID_SCIENTIFICCALCFRAMEBTN9, 
 wxID_SCIENTIFICCALCFRAMEBTNAC, wxID_SCIENTIFICCALCFRAMEBTNARCCOS, 
 wxID_SCIENTIFICCALCFRAMEBTNARCSIN, wxID_SCIENTIFICCALCFRAMEBTNARCTAN, 
 wxID_SCIENTIFICCALCFRAMEBTNBACKSPACE, wxID_SCIENTIFICCALCFRAMEBTNCE, 
 wxID_SCIENTIFICCALCFRAMEBTNCOS, wxID_SCIENTIFICCALCFRAMEBTNDIV, 
 wxID_SCIENTIFICCALCFRAMEBTNDOT, wxID_SCIENTIFICCALCFRAMEBTNE, 
 wxID_SCIENTIFICCALCFRAMEBTNEQUALS, wxID_SCIENTIFICCALCFRAMEBTNERAISETOX, 
 wxID_SCIENTIFICCALCFRAMEBTNFACTORIAL, wxID_SCIENTIFICCALCFRAMEBTNLEFTPAREN, 
 wxID_SCIENTIFICCALCFRAMEBTNLN, wxID_SCIENTIFICCALCFRAMEBTNLOG, 
 wxID_SCIENTIFICCALCFRAMEBTNM, wxID_SCIENTIFICCALCFRAMEBTNMINUS, 
 wxID_SCIENTIFICCALCFRAMEBTNMOD, wxID_SCIENTIFICCALCFRAMEBTNNSQUARED, 
 wxID_SCIENTIFICCALCFRAMEBTNPERCENTAGE, wxID_SCIENTIFICCALCFRAMEBTNPI, 
 wxID_SCIENTIFICCALCFRAMEBTNPLUS, wxID_SCIENTIFICCALCFRAMEBTNRECIPROCAL, 
 wxID_SCIENTIFICCALCFRAMEBTNRIGHTPAREN, wxID_SCIENTIFICCALCFRAMEBTNSGN, 
 wxID_SCIENTIFICCALCFRAMEBTNSIN, wxID_SCIENTIFICCALCFRAMEBTNSQUARED, 
 wxID_SCIENTIFICCALCFRAMEBTNTAN, wxID_SCIENTIFICCALCFRAMEBTNTIMES, 
 wxID_SCIENTIFICCALCFRAMEBTNXRAISETOY, wxID_SCIENTIFICCALCFRAMEBTNXSQUARE, 
 wxID_SCIENTIFICCALCFRAMECHOICE2, wxID_SCIENTIFICCALCFRAMEPANEL1, 
 wxID_SCIENTIFICCALCFRAMETEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(47)]

class ScientificCalcFrame(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SCIENTIFICCALCFRAME,
              name=u'ScientificCalcFrame', parent=prnt, pos=wx.Point(516, 160),
              size=wx.Size(746, 468), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Calculator')
        self.SetClientSize(wx.Size(746, 468))

        self.panel1 = wx.Panel(id=wxID_SCIENTIFICCALCFRAMEPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(746, 468),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_SCIENTIFICCALCFRAMETEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(55, 40),
              size=wx.Size(641, 72), style=0, value='textCtrl1')

        self.btnLeftParen = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNLEFTPAREN,
              label=u'(', name=u'btnLeftParen', parent=self.panel1,
              pos=wx.Point(187, 144), size=wx.Size(48, 43), style=0)

        self.btnRightParen = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNRIGHTPAREN,
              label=u')', name=u'btnRightParen', parent=self.panel1,
              pos=wx.Point(243, 144), size=wx.Size(48, 43), style=0)

        self.btnPercentage = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNPERCENTAGE,
              label=u'%', name=u'btnPercentage', parent=self.panel1,
              pos=wx.Point(299, 144), size=wx.Size(48, 43), style=0)

        self.btnPi = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNPI,
              label=u'\u03c0', name=u'btnPi', parent=self.panel1,
              pos=wx.Point(75, 200), size=wx.Size(48, 43), style=0)

        self.btnE = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNE, label=u'e',
              name=u'btnE', parent=self.panel1, pos=wx.Point(75, 256),
              size=wx.Size(48, 43), style=0)

        self.btnXRaiseToY = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNXRAISETOY,
              label=u'x\u02b8', name=u'btnXRaiseToY', parent=self.panel1,
              pos=wx.Point(75, 312), size=wx.Size(48, 43), style=0)
        self.btnXRaiseToY.Bind(wx.EVT_BUTTON, self.OnButton8Button,
              id=wxID_SCIENTIFICCALCFRAMEBTNXRAISETOY)

        self.btnNSquared = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNNSQUARED,
              label=u'\u02b8\u221a', name=u'btnNSquared', parent=self.panel1,
              pos=wx.Point(75, 368), size=wx.Size(48, 43), style=0)

        self.btnSin = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNSIN, label=u'sin',
              name=u'btnSin', parent=self.panel1, pos=wx.Point(131, 200),
              size=wx.Size(48, 43), style=0)

        self.btnCos = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNCOS, label=u'cos',
              name=u'btnCos', parent=self.panel1, pos=wx.Point(187, 200),
              size=wx.Size(48, 43), style=0)

        self.btnTan = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNTAN, label=u'tan',
              name=u'btnTan', parent=self.panel1, pos=wx.Point(243, 200),
              size=wx.Size(48, 43), style=0)

        self.btnSgn = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNSGN,
              label=u'\xb1', name=u'btnSgn', parent=self.panel1,
              pos=wx.Point(299, 200), size=wx.Size(48, 43), style=0)

        self.btnArcSin = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNARCSIN,
              label=u'sin-1', name=u'btnArcSin', parent=self.panel1,
              pos=wx.Point(131, 256), size=wx.Size(48, 43), style=0)

        self.btnArcCos = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNARCCOS,
              label=u'cos-1', name=u'btnArcCos', parent=self.panel1,
              pos=wx.Point(187, 256), size=wx.Size(48, 43), style=0)

        self.btnArcTan = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNARCTAN,
              label=u'tan-1', name=u'btnArcTan', parent=self.panel1,
              pos=wx.Point(243, 256), size=wx.Size(48, 43), style=0)

        self.btnSquared = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNSQUARED,
              label=u'\u221a', name=u'btnSquared', parent=self.panel1,
              pos=wx.Point(299, 256), size=wx.Size(48, 43), style=0)

        self.btn10RaiseToX = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN10RAISETOX,
              label=u'10\u02e3', name=u'btn10RaiseToX', parent=self.panel1,
              pos=wx.Point(131, 312), size=wx.Size(48, 43), style=0)

        self.btnERaiseToX = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNERAISETOX,
              label=u'e\u02e3', name=u'btnERaiseToX', parent=self.panel1,
              pos=wx.Point(187, 312), size=wx.Size(48, 43), style=0)

        self.btnMod = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNMOD, label=u'Mod',
              name=u'btnMod', parent=self.panel1, pos=wx.Point(243, 312),
              size=wx.Size(48, 43), style=0)

        self.btnXSquare = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNXSQUARE,
              label=u'x\xb2', name=u'btnXSquare', parent=self.panel1,
              pos=wx.Point(299, 312), size=wx.Size(48, 43), style=0)

        self.btnLog = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNLOG, label=u'log',
              name=u'btnLog', parent=self.panel1, pos=wx.Point(131, 368),
              size=wx.Size(48, 43), style=0)

        self.btnLn = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNLN, label=u'ln',
              name=u'btnLn', parent=self.panel1, pos=wx.Point(187, 368),
              size=wx.Size(48, 43), style=0)

        self.btnFactorial = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNFACTORIAL,
              label=u'n!', name=u'btnFactorial', parent=self.panel1,
              pos=wx.Point(243, 368), size=wx.Size(48, 43), style=0)

        self.btnReciprocal = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNRECIPROCAL,
              label=u'1/x', name=u'btnReciprocal', parent=self.panel1,
              pos=wx.Point(299, 368), size=wx.Size(48, 43), style=0)

        self.btnCE = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNCE, label=u'CE',
              name=u'btnCE', parent=self.panel1, pos=wx.Point(448, 144),
              size=wx.Size(48, 43), style=0)

        self.btn7 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN7, label=u'7',
              name=u'btn7', parent=self.panel1, pos=wx.Point(448, 200),
              size=wx.Size(48, 43), style=0)

        self.btn4 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN4, label=u'4',
              name=u'btn4', parent=self.panel1, pos=wx.Point(448, 256),
              size=wx.Size(48, 43), style=0)

        self.btn1 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN1, label=u'1',
              name=u'btn1', parent=self.panel1, pos=wx.Point(448, 312),
              size=wx.Size(48, 43), style=0)
        self.btn1.Bind(wx.EVT_BUTTON, self.OnButton29Button,
              id=wxID_SCIENTIFICCALCFRAMEBTN1)

        self.btn0 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN0, label=u'0',
              name=u'btn0', parent=self.panel1, pos=wx.Point(448, 368),
              size=wx.Size(48, 43), style=0)

        self.btnBackSpace = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNBACKSPACE,
              label=u'<=', name=u'btnBackSpace', parent=self.panel1,
              pos=wx.Point(504, 144), size=wx.Size(48, 43), style=0)

        self.btnM = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNM, label=u'M',
              name=u'btnM', parent=self.panel1, pos=wx.Point(560, 144),
              size=wx.Size(48, 43), style=0)

        self.btnAC = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNAC, label=u'AC',
              name=u'btnAC', parent=self.panel1, pos=wx.Point(616, 144),
              size=wx.Size(48, 43), style=0)

        self.btn8 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN8, label=u'8',
              name=u'btn8', parent=self.panel1, pos=wx.Point(504, 200),
              size=wx.Size(48, 43), style=0)

        self.btn9 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN9, label=u'9',
              name=u'btn9', parent=self.panel1, pos=wx.Point(560, 200),
              size=wx.Size(48, 43), style=0)

        self.btnDiv = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNDIV,
              label=u'\xf7', name=u'btnDiv', parent=self.panel1,
              pos=wx.Point(616, 200), size=wx.Size(48, 43), style=0)

        self.btn5 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN5, label=u'5',
              name=u'btn5', parent=self.panel1, pos=wx.Point(504, 256),
              size=wx.Size(48, 43), style=0)

        self.btn6 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN6, label=u'6',
              name=u'btn6', parent=self.panel1, pos=wx.Point(560, 256),
              size=wx.Size(48, 43), style=0)
        self.btn6.Bind(wx.EVT_BUTTON, self.OnButton38Button,
              id=wxID_SCIENTIFICCALCFRAMEBTN6)

        self.btnTimes = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNTIMES,
              label=u'x', name=u'btnTimes', parent=self.panel1,
              pos=wx.Point(616, 256), size=wx.Size(48, 43), style=0)
        self.btnTimes.Bind(wx.EVT_BUTTON, self.OnButton39Button,
              id=wxID_SCIENTIFICCALCFRAMEBTNTIMES)

        self.btn2 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN2, label=u'2',
              name=u'btn2', parent=self.panel1, pos=wx.Point(504, 312),
              size=wx.Size(48, 43), style=0)

        self.btn3 = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTN3, label=u'3',
              name=u'btn3', parent=self.panel1, pos=wx.Point(560, 312),
              size=wx.Size(48, 43), style=0)

        self.btnMinus = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNMINUS,
              label=u'-', name=u'btnMinus', parent=self.panel1,
              pos=wx.Point(616, 312), size=wx.Size(48, 43), style=0)

        self.btnDot = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNDOT, label=u'.',
              name=u'btnDot', parent=self.panel1, pos=wx.Point(504, 368),
              size=wx.Size(48, 43), style=0)

        self.btnEquals = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNEQUALS,
              label=u'=', name=u'btnEquals', parent=self.panel1,
              pos=wx.Point(560, 368), size=wx.Size(48, 43), style=0)

        self.btnPlus = wx.Button(id=wxID_SCIENTIFICCALCFRAMEBTNPLUS, label=u'+',
              name=u'btnPlus', parent=self.panel1, pos=wx.Point(616, 368),
              size=wx.Size(48, 43), style=0)

        self.choice2 = wx.Choice(choices=['Standard', 'Scientific'], id=wxID_SCIENTIFICCALCFRAMECHOICE2,
              name=u'choice2', parent=self.panel1, pos=wx.Point(523, 12),
              size=wx.Size(160, 25), style=0)
        self.choice2.Bind(wx.EVT_CHOICE, self.OnChoice2Choice,
              id=wxID_SCIENTIFICCALCFRAMECHOICE2)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.parent = parent

    def OnButton8Button(self, event):
        event.Skip()

    def OnButton29Button(self, event):
        event.Skip()

    def OnButton38Button(self, event):
        event.Skip()

    def OnButton39Button(self, event):
        event.Skip()

    def OnChoice2Choice(self, event):
        choice = self.choice2.GetStringSelection()
        if choice == "Standard":
            method = getattr(self, "OnSimple")
        elif choice == "Scientific":
            method = getattr(self, "OnScientific")        
        method()
  
    def OnSimple(self):
        self.parent.Show()
        self.Hide()
        
    def OnScientific(self):
        self.Show()
