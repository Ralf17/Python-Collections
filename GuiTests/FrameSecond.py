#Boa:Frame:FrameSecond

import wx

def create(parent):
    return FrameSecond(parent)

[wxID_FRAMESECOND, wxID_FRAMESECONDBTNFSEXIT, wxID_FRAMESECONDPANEL1, 
 wxID_FRAMESECONDSTHITHERE, 
] = [wx.NewId() for _init_ctrls in range(4)]

class FrameSecond(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMESECOND, name=u'FrameSecond',
              parent=prnt, pos=wx.Point(341, 167), size=wx.Size(911, 445),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Second Frame')
        self.SetClientSize(wx.Size(911, 445))

        self.panel1 = wx.Panel(id=wxID_FRAMESECONDPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(911, 445),
              style=wx.TAB_TRAVERSAL)

        self.btnFSExit = wx.Button(id=wxID_FRAMESECONDBTNFSEXIT, label=u'Exit',
              name=u'btnFSExit', parent=self.panel1, pos=wx.Point(413, 209),
              size=wx.Size(85, 27), style=0)
        self.btnFSExit.Center(wx.BOTH)
        self.btnFSExit.Bind(wx.EVT_BUTTON, self.OnBtnFSExitButton,
              id=wxID_FRAMESECONDBTNFSEXIT)

        self.stHiThere = wx.StaticText(id=wxID_FRAMESECONDSTHITHERE,
              label=u"Hi there...I'm the second form!", name=u'stHiThere',
              parent=self.panel1, pos=wx.Point(304, 96), size=wx.Size(328, 23),
              style=wx.ALIGN_CENTRE)
        self.stHiThere.SetToolTipString(u'staticText1')
        self.stHiThere.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Sans'))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.parent = parent

    def OnBtnFSExitButton(self, event):
#        event.Skip()
        self.parent.Show()
        self.Hide()
