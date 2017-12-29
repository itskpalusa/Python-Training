import sqlite3
import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoMixin

import sys

class MyDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Student Records", size = (600, 400))

        lbl = wb.StaticText(self, label="Please Enter Info Below", pos=(10, 10))

        self.first_name = wx.TextCtrl(self, -1, ' ', pos=(25, 40)) #1
        wx.StaticText(self, -1, 'First Name', pos=(150, 40))

        self.last_name = wx.TextCtrl(self, -1, ' ', pos=(275, 40)) #2
        wx.StaticText(self, -1, 'Last Name', pos=(400, 40))

        self.hrs_comleted = wx.TextCtrl(self, -1, ' ', pos=(25, 100)) # 1
        wx.StaticText(self, -1, 'Hours Completed', pos=(150, 100))

        self.hrs_attempted = wx.TextCtrl(self, -1, ' ', pos=(275, 100))
        wx.StaticText(self, -1, 'Hours Attempted', pos=(400, 100))


        self.gpa = wx.TextCtrl(self, -1, ' ', pos=(25, 160))
        wx.StaticText(self, -1, 'GPA', pos=(150, 160))

        self.major = wx.TextCtrl(self, -1, ' ', pos=(275, 160))
        wx.StaticText(self, -1, 'Major', pos=(400, 160))

        self.advisor = wx.TextCtrl(self, -1, ' ', pos=(25, 220))
        wx.StaticText(self, -1, 'Advisor', pos=(150, 220))

        self.email = wx.TextCtrl(self, -1, ' ', pos=(275, 220))
        wx.StaticText(self, -1, 'Email', pos=(400, 220))

        okBtn = wx.Button(self, id=wx.ID_OK, pos=(274, 300)) #add wx.OK Button

class MajorCombobox(wx.Combobox):
    def __init__(self, parent, value, majorList):
        wx.Combobox.__init__(self, parent, choices=majorList, style=wx.CB_READONLY,
                                                                            size=(100, -1))
        self.SetSelection(0)

class MyListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__ (self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(830, 440))





        # instance var

        self.major = ""

        panel = wx.Panel(self, -1)


        uber_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.table_name = wx.StaticBox(panel, -1, 'Student REcords', pos=(50, 5))

        lest_sizer = wx.StaticBoxSizer(self.table_name, wx.VERTICAL)
        right_sizer = wx.BoxSizer(wx.VERTICAL)



        majorList = ["Select Major", "CIS", "BUS", "EET", "WEB"]
        self.cbMajor = MajorCombobox(panel, -1, majorList)

        dispAll = wx.Button(panel, -1, 'Display All', size=(100, -1))
        getAdvisor = wx.Button(panel, -1, 'Advisor Info', size=(100, -1))
        deselect = wx.Button(panel, -1, 'Deselect All', size=(100, -1))
        newStudent = wx.Button(panel, -1, 'New Student', size=(100, -1))
        lessthanThree = wx.Button(panel, -1, 'GPA < 3.0', size=(100, -1))
        self.lessthanTwo = wx.RadioButton(panel, -1, 'GPA < 2.0', size=(100, -1))

        # Binds the Combobox and Buttons

        self.cbMajor.Bind(wx.EVT_COMBOBOX, self.OnSelectMajor)
        dispAll.Bind(wx.EVT_COMBOBOX, self.displayAll)
        getAdvisor.Bind(wx.EVT_COMBOBOX, self.getAdvisor)
        deselect.Bind(wx.EVT_COMBOBOX, self.OnDeselectAll)
        newStudent.Bind(wx.EVT_COMBOBOX, self.OnAdd)
        lessthanThree.Bind(wx.EVT_COMBOBOX, self.lessThree)
        self.lessthanTwo.Bind(wx.EVT_COMBOBOX, self.lessThanTwo)
