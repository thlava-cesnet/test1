#!/usr/bin/env python

import wx

class MyPanel(wx.Panel): 
   def __init__(self, parent): 
      super(MyPanel, self).__init__(parent)
      b = wx.Button(self, label = 'Close', pos = (300,100)) 
      b.Bind(wx.EVT_BUTTON, self.btnclk) 
      self.Bind(wx.EVT_BUTTON, self.OnButtonClicked) 
		
   def OnButtonClicked(self, e): 
      print('Panel received click event. propagated to Frame class')
      e.Skip()  
		
   def btnclk(self,e): 
      print("Button received click event. propagated to Panel class")
      e.Skip()

class Example(wx.Frame): 
   def __init__(self, *args, **kw): 
      super(Example, self).__init__(*args, **kw)  
      self.InitUI() 
           
   def InitUI(self): 
      mpnl = MyPanel(self)
      self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
      self.Bind(wx.EVT_MOVE, self.OnMove) 
      
      self.SetSize((640, 480)) 
      self.SetTitle('wx test 1') 
      self.Centre() 
      self.Show(True)
		   
   def OnButtonClicked(self, e): 
      print('click event received by frame class')
      e.Skip()
      wx.CallAfter(self.Close)

   def OnMove(self, e): 
      x, y = e.GetPosition() 
      print(f"current window position x={x} y={y}")


app = wx.App() 
#window = wx.Frame(None, title = "wxPython Frame", size = (300,200)) 
#panel = wx.Panel(window) 
#label = wx.StaticText(panel, label = "Hello World", pos = (100,50)) 
#window.Show(True) 
Example(None)
app.MainLoop()
