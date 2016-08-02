# -*- coding: cp936 -*-
#这个框架你需要复制一份再使用，使用方法就是根据注释自定义你的样式
#注意本框架设计出的的排版已经固定
"""-----------------------------------------------------------------"""
#请在这里添加你的事件函数要使用到的模块
import wx
#不能修改的内容 或调试内容

#基本配置
title='Application'#输入你的顶级窗口名字
size=(410,335)#顶级窗口尺寸（长，高）
Button1='Open'#第一个按钮名字
Button2='Save'#第二个按钮名字



def load(event):
    file=open(input1.GetValue())  #特别注意，从输入框这么得到的字符串是unicode
    show.SetValue(file.read())
    file.close()

def save(event):
    file=open(input1,GetValue(),'w')
    file.write(show.GetValue())
    file.close()

def Quit(event):#菜单项绑定事件
    show.AppendText(">please\n")

app=wx.App()
win=wx.Frame(None,title=title,size=size)
win.SetPosition((450,150))#设置窗口打开后在屏幕的位置

menubar = wx.MenuBar()
##这里开始生成一个
filemenu = wx.Menu()
###这里开始生成一个菜单项下拉下拉一项
qmi = wx.MenuItem(filemenu,1, "Quit")#修改名字  
filemenu.AppendItem(qmi)
menubar.Append(filemenu, "File")#修改名字
#
win.SetMenuBar(menubar)
#给id=1的项绑定事件
win.Bind(wx.EVT_MENU, Quit, id=1) #修改触发事件和调用函数，注意Quit名字除了函数以外绝对不能出现在任何地方

bkg=wx.Panel(win)



loadButton=wx.Button(bkg,label=Button1)
loadButton.Bind(wx.EVT_BUTTON,load)            #请修改触发事件和调用函数
saveButton=wx.Button(bkg,label=Button2)
saveButton.Bind(wx.EVT_BUTTON,save)          #请修改触发事件和调用函数


input1=wx.TextCtrl(bkg)
input1.Bind(wx.EVT_TEXT_ENTER,load)#当输入框检测到回车事件就调用函数load，必须和上面loadButton一致
show=wx.TextCtrl(bkg,value='',style=wx.TE_MULTILINE | wx.HSCROLL)#value设置初始显示内容

#布局
hbox=wx.BoxSizer()
hbox.Add(input1,proportion=1,flag=wx.EXPAND)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL,border=5)
vbox.Add(show,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

bkg.SetSizer(vbox)

win.Show()

app.MainLoop()
