"""
The default is to display several frames.
"""
import wx
from wx_mac_window_menu.WindowMenu import WindowMenu


def main():
    app = wx.App()
    for i in range(1, 5):
        frm = wx.Frame(None, title="Frame #{0}".format(i), size=(300, 300))
        mb = wx.MenuBar()
        window_menu = WindowMenu()
        mb.Append(window_menu, "&Window #{0}".format(i))
        frm.Bind(wx.EVT_ACTIVATE, window_menu.on_activate_window)
        frm.SetMenuBar(mb)
        # print("!!!!!!!       {2} : {0} : {1}".format(repr(frm), frm.Title, frm.Id))
        # cascade the windows for testing
        frm.SetPosition((i * 24 + 350, i * 24 + 150))
        frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
