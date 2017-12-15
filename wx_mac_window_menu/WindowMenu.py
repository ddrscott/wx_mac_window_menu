import wx


class WindowMenu(wx.Menu):
    def __init__(self, *args, **kw):
        wx.Menu.__init__(self, *args, **kw)

    def on_activate_window(self, evt):
        evt.Skip()
        self.clear()
        for i, w in enumerate(wx.GetTopLevelWindows()):
            item = self.AppendRadioItem(w.Id, w.Title)
            self.Check(item.Id, evt.GetId() == w.Id and evt.Active)

        if evt.Active:
            self.Bind(wx.EVT_MENU, self.on_selected)
        else:
            self.Unbind(wx.EVT_MENU)

    def on_selected(self, evt=None):
        evt.Skip()
        selected_window = wx.FindWindowById(evt.GetId())
        wx.CallAfter(lambda: selected_window.Raise())

    def clear(self):
        for m in self.GetMenuItems():
            self.Remove(m)
            m.Destroy()
