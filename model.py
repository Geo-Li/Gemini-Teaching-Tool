import sys
from configparser import ConfigParser
from bing_search import *
from gemini_model import *
from PyQt5.QtWidgets import QApplication, QLineEdit,\
                            QPushButton, QVBoxLayout,\
                            QLabel, QWidget, QDialog,\
                            QMessageBox, QMainWindow,\
                            QScrollArea, QGroupBox,\
                            QHBoxLayout

config = ConfigParser()
config.read('config.ini')

BING_SEARCH_API_KEY = config['BingAPI']['api_key']
BING_SEARCH_ENDPOINT = config['BingAPI']['endpoint']
GEMINI_API_KEY = config['Gemini']['api_key']


class UI(QMainWindow):
    def __init__(self):
        self.bing_search = BingSearch(BING_SEARCH_API_KEY, BING_SEARCH_ENDPOINT)
        self.gemini_model = GeminiModel(GEMINI_API_KEY)
        
        super().__init__()
        self.setWindowTitle("MyEdMaster Gemini UI")
        
        # Set maximum size of the window
        self.setMaximumSize(800, 600)

        # Widgets
        self.inputBox = QLineEdit()
        self.searchButton = QPushButton("Search")
        self.resultLabel = QLabel()
        self.resultLabel.setWordWrap(True)
        
        # Scrollable area for the result label
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.resultLabel)
        
        # GroupBox for buttons
        self.buttonGroup = QGroupBox()
        buttonLayout = QHBoxLayout()  # Horizontal layout for the buttons

        self.criteria = set()
        self.button_states = {}
        button_names = ['knows nothing about math', '5 year old', 'math expert']
        for criterion in button_names:
            btn = QPushButton(criterion)
            btn.setCheckable(True)
            self.button_states[criterion] = False
            btn.clicked.connect(lambda checked, btn = btn: self.toggleCriterion(btn))
            buttonLayout.addWidget(btn)
            
        self.buttonGroup.setLayout(buttonLayout)
        
        # Layout
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.inputBox)
        self.layout.addWidget(self.buttonGroup)
        self.layout.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.handleSearch)  # Connect the button's clicked signal
        self.layout.addWidget(scroll_area)
        
        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
        
        # Variable to store the result
        self.result = ""
        
        # Styling
        self.setStyleSheet("""
            QWidget {
                font-size: 16px;
            }
            QLineEdit, QPushButton, QGroupBox {
                height: 40px;
                margin: 5px;
            }
            QScrollArea {
                border: 2px solid #0078D7;
            }
        """)

    def handleSearch(self):
        # Get the text from the input box
        inputText = self.inputBox.text()
        
        params = {
            'q': inputText,
            'count': 50, 
            'offset': 0,
            'mkt': 'en-US',
            'freshness': 'Month'
        }
        response = self.bing_search.search(params)
        urls = self.bing_search.parse_url(response)
        htmls = self.bing_search.parse_html(urls, range(len(urls)))
        
        # for i in range
        resultText = self.gemini_model.eval_website(list(htmls.values())[0], ["correctness"])
        # convo.last.text        
        # Update the label with the result
        self.resultLabel.setText(f"Result:\n{list(htmls.values())[0]}")

    def toggleCriterion(self, button):
        criterion = button.text()
        # Toggle the state
        self.button_states[criterion] = not self.button_states[criterion]
        # Update the button style based on the state
        if self.button_states[criterion]:
            button.setStyleSheet("background-color: gray;")
            self.criteria.add(criterion)
        else:
            button.setStyleSheet("")
            self.criteria.remove(criterion)
        # Reflect the text change to the button
        self.inputBox.setText(", ".join(self.criteria))


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QPushButton {
            background-color: green;
            color: white;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            padding: 6px;
        }
        QPushButton:hover {
            background-color: #5FAD41;
        }
        QPushButton:pressed {
            background-color: #407A2E;
        }
    """)
    window = UI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    print("Start of the main process of the project")
    main()
    