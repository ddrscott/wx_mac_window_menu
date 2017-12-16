import wx


class WindowMenu(wx.Menu):
    def __init__(self, frame, *args, **kw):
        wx.Menu.__init__(self, *args, **kw)
        frame.Bind(wx.EVT_ACTIVATE, self.on_activate_window)
        frame.Bind(wx.EVT_CLOSE, self.on_close_window)
        self.frame = frame

    def on_close_window(self, evt):
        self.frame.Unbind(wx.EVT_CLOSE, handler=self.on_close_window)
        self.frame.Unbind(wx.EVT_ACTIVATE, handler=self.on_activate_window)
        self.frame._wx_mac_window_menu__frame_closing = True
        evt.Skip()

    def on_activate_window(self, evt):
        self.clear()
        open_windows = [w for w in wx.GetTopLevelWindows() if not (hasattr(w, '_wx_mac_window_menu__frame_closing'))]
        for i, w in enumerate(open_windows):
            shortcut = "\tCTRL+{0}".format(i+1) if i < 9 else ''
            item = self.AppendRadioItem(w.Id, w.Title + shortcut)
            self.Check(item.Id, evt.GetId() == w.Id and evt.Active)
        if evt.Active:
            self.Bind(wx.EVT_MENU, self.on_selected)
        else:
            self.Unbind(wx.EVT_MENU)
        evt.Skip()

    def on_selected(self, evt=None):
        evt.Skip()
        selected_window = wx.FindWindowById(evt.GetId())
        wx.CallAfter(lambda: selected_window.Raise())

    def clear(self):
        for m in self.GetMenuItems():
            self.Remove(m)
            m.Destroy()
