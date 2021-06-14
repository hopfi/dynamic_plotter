
class dynamicPlotter:

    def __init__(self, fig, **kwargs):
        # generate axes object
        self.xdata = []
        self.ydata = []

        self.dataWindowSize = 100
        lineStyle = "r-"
        for key, value in kwargs.items():
            if key == "windowSize":
                self.dataWindowSize = value
            if key == "lineStyle":
                lineStyle = value

        self.fig_ref = fig
        self.axes = self.fig_ref.gca()
        self.fig_ref.show()

        self.line, = self.axes.plot(self.xdata, self.ydata, lineStyle)

    def update_data(self, x, y):
        self.xdata.append(x)
        self.ydata.append(y)

        if len(self.xdata) >= self.dataWindowSize:
            self.xdata.pop(0)
        
        if len(self.ydata) >= self.dataWindowSize:
            self.ydata.pop(0)

    def update_window(self):
        self.fig_ref.canvas.draw()
        self.fig_ref.canvas.flush_events()

    def update_graph(self):
        self.line.set_xdata(self.xdata)
        self.line.set_ydata(self.ydata)
        self.axes.set_xlim(min(self.xdata), max(self.xdata))
        self.axes.set_ylim(min(self.ydata)-5, max(self.ydata)+5)

    def add_data(self, x, y):
        self.update_data(x,y)
        self.update_graph()
        self.update_window()

    def clear_plot(self):
        pass

if __name__== "__main__":
    pass