#Boa:Frame:MyFirstGUI

import wx

def create(parent):
    return MyFirstGUI(parent)

[wxID_MYFIRSTGUI, wxID_MYFIRSTGUIBTNSHOWDIALOG, wxID_MYFIRSTGUIPANEL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class MyFirstGUI(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MYFIRSTGUI, name=u'MyFirstGUI',
              parent=prnt, pos=wx.Point(341, 167), size=wx.Size(911, 445),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(911, 445))

        self.panel1 = wx.Panel(id=wxID_MYFIRSTGUIPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(911, 445),
              style=wx.TAB_TRAVERSAL)

        self.btnShowDialog = wx.Button(id=wxID_MYFIRSTGUIBTNSHOWDIALOG,
              label=u'Click Me', name=u'btnShowDialog', parent=self.panel1,
              pos=wx.Point(401, 182), size=wx.Size(85, 35), style=0)
        self.btnShowDialog.Bind(wx.EVT_BUTTON, self.OnBtnShowDialogButton,
              id=wxID_MYFIRSTGUIBTNSHOWDIALOG)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtnShowDialogButton(self, event):
  #      event.Skip()
        wx.MessageBox('You Clicked the button', 'Info', wx.ICON_INFORMATION)