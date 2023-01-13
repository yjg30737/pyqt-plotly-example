import os.path
import posixpath

import plotly.graph_objects as go
import plotly.offline as offline
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('PyQt & Plotly')

        fig = go.Figure(data=go.Choropleth())

        cur_dir = os.path.dirname(__file__)
        filename = os.path.join(cur_dir, 'map.html').replace(os.path.sep, posixpath.sep)

        offline.plot(fig, filename=filename, auto_open=False)

        view = QWebEngineView()
        view.load(QUrl.fromLocalFile(filename))

        self.setCentralWidget(view)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()