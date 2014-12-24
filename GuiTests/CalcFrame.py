#Boa:Frame:SimpleCalcFrame

import wx

import CalcFrame2

def create(parent):
    return SimpleCalcFrame(parent)

[wxID_SIMPLECALCFRAME, wxID_SIMPLECALCFRAMEBTN0, wxID_SIMPLECALCFRAMEBTN1, 
 wxID_SIMPLECALCFRAMEBTN2, wxID_SIMPLECALCFRAMEBTN3, wxID_SIMPLECALCFRAMEBTN4, 
 wxID_SIMPLECALCFRAMEBTN5, wxID_SIMPLECALCFRAMEBTN6, wxID_SIMPLECALCFRAMEBTN7, 
 wxID_SIMPLECALCFRAMEBTN8, wxID_SIMPLECALCFRAMEBTN9, 
 wxID_SIMPLECALCFRAMEBTNCLEAR, wxID_SIMPLECALCFRAMEBTNDIV, 
 wxID_SIMPLECALCFRAMEBTNDOT, wxID_SIMPLECALCFRAMEBTNEQUALS, 
 wxID_SIMPLECALCFRAMEBTNMINUS, wxID_SIMPLECALCFRAMEBTNPLUS, 
 wxID_SIMPLECALCFRAMEBTNSIGN, wxID_SIMPLECALCFRAMEBTNTIMES, 
 wxID_SIMPLECALCFRAMECHOICE1, wxID_SIMPLECALCFRAMEEDIT, 
 wxID_SIMPLECALCFRAMEPANEL1, 
] = [wx.NewId() for _init_ctrls in range(22)]

class SimpleCalcFrame(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SIMPLECALCFRAME,
              name=u'SimpleCalcFrame', parent=prnt, pos=wx.Point(882, 167),
              size=wx.Size(264, 444), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Calculator')
        self.SetClientSize(wx.Size(264, 444))

        self.panel1 = wx.Panel(id=wxID_SIMPLECALCFRAMEPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(264, 444),
              style=wx.TAB_TRAVERSAL)

        self.edit = wx.TextCtrl(id=wxID_SIMPLECALCFRAMEEDIT, name='edit',
              parent=self.panel1, pos=wx.Point(21, 50), size=wx.Size(220, 66),
              style=wx.TE_LEFT, value='')

        self.btnClear = wx.Button(id=wxID_SIMPLECALCFRAMEBTNCLEAR, label=u'C',
              name='btnClear', parent=self.panel1, pos=wx.Point(23, 144),
              size=wx.Size(48, 43), style=0)
        self.btnClear.Bind(wx.EVT_BUTTON, self.OnBtnClearButton,
              id=wxID_SIMPLECALCFRAMEBTNCLEAR)

        self.btnSign = wx.Button(id=wxID_SIMPLECALCFRAMEBTNSIGN, label=u'\xb1',
              name='btnSign', parent=self.panel1, pos=wx.Point(79, 144),
              size=wx.Size(48, 43), style=0)
        self.btnSign.Bind(wx.EVT_BUTTON, self.OnBtnSignButton,
              id=wxID_SIMPLECALCFRAMEBTNSIGN)

        self.btnDiv = wx.Button(id=wxID_SIMPLECALCFRAMEBTNDIV, label=u'\xf7',
              name='btnDiv', parent=self.panel1, pos=wx.Point(135, 144),
              size=wx.Size(48, 43), style=0)
        self.btnDiv.Bind(wx.EVT_BUTTON, self.OnBtnDivButton,
              id=wxID_SIMPLECALCFRAMEBTNDIV)

        self.btn7 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN7, label=u'7',
              name='btn7', parent=self.panel1, pos=wx.Point(23, 200),
              size=wx.Size(48, 43), style=0)
        self.btn7.Bind(wx.EVT_BUTTON, self.OnBtn7Button,
              id=wxID_SIMPLECALCFRAMEBTN7)

        self.btn8 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN8, label=u'8',
              name='btn8', parent=self.panel1, pos=wx.Point(79, 200),
              size=wx.Size(48, 43), style=0)
        self.btn8.Bind(wx.EVT_BUTTON, self.OnBtn8Button,
              id=wxID_SIMPLECALCFRAMEBTN8)

        self.btn9 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN9, label=u'9',
              name='btn9', parent=self.panel1, pos=wx.Point(135, 200),
              size=wx.Size(48, 43), style=0)
        self.btn9.Bind(wx.EVT_BUTTON, self.OnBtn9Button,
              id=wxID_SIMPLECALCFRAMEBTN9)

        self.btn4 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN4, label=u'4',
              name='btn4', parent=self.panel1, pos=wx.Point(23, 256),
              size=wx.Size(48, 43), style=0)
        self.btn4.Bind(wx.EVT_BUTTON, self.OnBtn4Button,
              id=wxID_SIMPLECALCFRAMEBTN4)

        self.btn5 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN5, label=u'5',
              name='btn5', parent=self.panel1, pos=wx.Point(79, 256),
              size=wx.Size(48, 43), style=0)
        self.btn5.Bind(wx.EVT_BUTTON, self.OnBtn5Button,
              id=wxID_SIMPLECALCFRAMEBTN5)

        self.btn6 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN6, label=u'6',
              name='btn6', parent=self.panel1, pos=wx.Point(135, 256),
              size=wx.Size(48, 43), style=0)
        self.btn6.Bind(wx.EVT_BUTTON, self.OnBtn6Button,
              id=wxID_SIMPLECALCFRAMEBTN6)

        self.btn1 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN1, label=u'1',
              name='btn1', parent=self.panel1, pos=wx.Point(23, 312),
              size=wx.Size(48, 43), style=0)
        self.btn1.Bind(wx.EVT_BUTTON, self.OnBtn1Button,
              id=wxID_SIMPLECALCFRAMEBTN1)

        self.btn2 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN2, label=u'2',
              name='btn2', parent=self.panel1, pos=wx.Point(79, 312),
              size=wx.Size(48, 43), style=0)
        self.btn2.Bind(wx.EVT_BUTTON, self.OnBtn2Button,
              id=wxID_SIMPLECALCFRAMEBTN2)

        self.btn3 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN3, label=u'3',
              name='btn3', parent=self.panel1, pos=wx.Point(135, 312),
              size=wx.Size(48, 43), style=0)
        self.btn3.Bind(wx.EVT_BUTTON, self.OnBtn3Button,
              id=wxID_SIMPLECALCFRAMEBTN3)

        self.btn0 = wx.Button(id=wxID_SIMPLECALCFRAMEBTN0, label=u'0',
              name='btn0', parent=self.panel1, pos=wx.Point(23, 368),
              size=wx.Size(103, 43), style=0)
        self.btn0.Bind(wx.EVT_BUTTON, self.OnBtn0Button,
              id=wxID_SIMPLECALCFRAMEBTN0)

        self.btnTimes = wx.Button(id=wxID_SIMPLECALCFRAMEBTNTIMES, label=u'x',
              name='btnTimes', parent=self.panel1, pos=wx.Point(191, 144),
              size=wx.Size(48, 43), style=0)
        self.btnTimes.Bind(wx.EVT_BUTTON, self.OnBtnTimesButton,
              id=wxID_SIMPLECALCFRAMEBTNTIMES)

        self.btnMinus = wx.Button(id=wxID_SIMPLECALCFRAMEBTNMINUS, label=u'-',
              name='btnMinus', parent=self.panel1, pos=wx.Point(191, 200),
              size=wx.Size(48, 43), style=0)
        self.btnMinus.Bind(wx.EVT_BUTTON, self.OnBtnMinusButton,
              id=wxID_SIMPLECALCFRAMEBTNMINUS)

        self.btnPlus = wx.Button(id=wxID_SIMPLECALCFRAMEBTNPLUS, label=u'+',
              name='btnPlus', parent=self.panel1, pos=wx.Point(191, 256),
              size=wx.Size(48, 43), style=0)
        self.btnPlus.Bind(wx.EVT_BUTTON, self.OnBtnPlusButton,
              id=wxID_SIMPLECALCFRAMEBTNPLUS)

        self.btnDot = wx.Button(id=wxID_SIMPLECALCFRAMEBTNDOT, label=u'.',
              name='btnDot', parent=self.panel1, pos=wx.Point(135, 368),
              size=wx.Size(48, 43), style=0)
        self.btnDot.Bind(wx.EVT_BUTTON, self.OnBtnDotButton,
              id=wxID_SIMPLECALCFRAMEBTNDOT)

        self.btnEquals = wx.Button(id=wxID_SIMPLECALCFRAMEBTNEQUALS, label=u'=',
              name='btnEquals', parent=self.panel1, pos=wx.Point(191, 312),
              size=wx.Size(48, 100), style=0)
        self.btnEquals.Bind(wx.EVT_BUTTON, self.OnBtnEqualsButton,
              id=wxID_SIMPLECALCFRAMEBTNEQUALS)

        self.choice1 = wx.Choice(choices=['Standard',
              'Scientific'], id=wxID_SIMPLECALCFRAMECHOICE1,
              name='choice1', parent=self.panel1, pos=wx.Point(80, 24),
              size=wx.Size(160, 25), style=0)
        self.choice1.Bind(wx.EVT_CHOICE, self.OnChoice1Choice,
              id=wxID_SIMPLECALCFRAMECHOICE1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.SciCal = CalcFrame2.ScientificCalcFrame(self)

    def OnBtn7Button(self, event):
        val = '7'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn8Button(self, event):
        val = '8'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn9Button(self, event):
        val = '9'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn4Button(self, event):
        val = '4'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn5Button(self, event):
        val = '5'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn6Button(self, event):
        val = '6'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn1Button(self, event):
        val = '1'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn2Button(self, event):
        val = '2'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn3Button(self, event):
        val = '3'
        txt = self.edit.GetValue()
        txt += val
        self.edit.SetValue(txt)

    def OnBtn0Button(self, event):
        val = '0'
        txt = self.edit.GetValue()
        if txt != '':
            txt += val
            self.edit.SetValue(txt)

    def OnBtnClearButton(self, event):
        self.edit.SetValue('')


    def OnBtnSignButton(self, event):
        val = '-'
        txt = self.edit.GetValue()
        if txt != '':
            txt = val + txt
            self.edit.SetValue(txt)
            

    def OnBtnDivButton(self, event):
        val = u'\xf7'
        txt = self.edit.GetValue()
        if txt != '':
            txt += val
            self.edit.SetValue(txt)

    def OnBtnTimesButton(self, event):
        val = 'x'
        txt = self.edit.GetValue()
        if txt != '':
            txt += val
            self.edit.SetValue(txt)

    def OnBtnMinusButton(self, event):
        val = '-'
        txt = self.edit.GetValue()
        if txt != '':
            txt += val
            self.edit.SetValue(txt)

    def OnBtnPlusButton(self, event):
        val = '+'
        txt = self.edit.GetValue()
        if txt != '':
            txt += val
            self.edit.SetValue(txt)

    def OnBtnDotButton(self, event):
        val = '.'
        txt = self.edit.GetValue()
        if txt != '':
            txt += val
            self.edit.SetValue(txt)

    def OnBtnEqualsButton(self, event):
        txt = self.edit.GetValue()

        if u'\xf7' in txt:
            pos = txt.index(u'\xf7')
            txt = txt[:pos] + '/' + txt[(pos + 1):]
        
        if '/' in txt:
            if '.' not in txt:
                txt += '.0'
        
        if 'x' in txt:
            pos = txt.index('x')
            txt = txt[:pos] + '*' + txt[(pos + 1):]

        txt = repr(eval(txt))
        self.edit.SetValue(txt)

    def OnChoice1Choice(self, event):
        choice = self.choice1.GetStringSelection()
        if choice == "Standard":
            method = getattr(self, "OnSimple")
        elif choice == "Scientific":
            method = getattr(self, "OnScientific")        
        method()
  
    def OnSimple(self):
        self.Show()
        
    def OnScientific(self):
        self.SciCal.Show()
        self.Hide()

