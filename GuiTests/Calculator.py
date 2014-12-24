#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import CalcFrame
import CalcFrame2

modules ={u'CalcFrame': [1, 'Main frame of Application', u'CalcFrame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = CalcFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
