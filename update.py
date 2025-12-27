from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QTextEdit, QInputDialog, QComboBox, QStatusBar, QProgressBar   
from PyQt6.QtCore import QProcess, QProcessEnvironment
from PyQt6.QtGui import QIcon
from time import sleep
import sys

class main_Windown(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Iniciar_Aplicacao()

    def Iniciar_Aplicacao(self):
        self.setFixedSize(750, 750) 
        self.setWindowTitle("Update System")
        self.setWindowIcon(QIcon('recursos/gemini_up_System.png'))
        self.Widgets_Definitions()
        self.Widgets_Settings()
        self.Widgets_Styles()
        self.Widgets_Layout()
        self.settings_Combo()
        self.show()

    def Widgets_Definitions(self):
        self.search_Packages_Combo = QComboBox(self)
        self.search_Packages_Line = QLineEdit(self)
        self.search_Packages_Button = QPushButton('Buscar', self)
        self.install_package_Button = QPushButton('Instalar', self)
        self.uninstall_package_Button = QPushButton(self)
        self.clear_Text_Button = QPushButton('Limpar', self)
        self.update_Button = QPushButton('Atualizar', self)
        self.content_Prompt = QTextEdit(self)
        self.prompt_Process = QProcess()


    def Widgets_Settings(self):
        self.search_Packages_Line.setPlaceholderText('Inserir Nome do Pacote')
        self.search_Packages_Line.setClearButtonEnabled(True)
        self.search_Packages_Line.textEdited.connect(self.place_Holder_Settings)
        self.search_Packages_Button.setEnabled(False)
        self.install_package_Button.setEnabled(False)
        self.uninstall_package_Button.setIcon(QIcon('recursos/lixeira.png'))
        self.install_package_Button.clicked.connect(self.install_Package)
        self.search_Packages_Button.clicked.connect(self.search_Package)
        self.install_package_Button.clicked.connect(self.install_Package)
        self.uninstall_package_Button.clicked.connect(self.uninstall_Package)
        self.clear_Text_Button.clicked.connect(self.clear_Text)
        self.update_Button.clicked.connect(self.update_System)
        self.content_Prompt.setReadOnly(True)



    def Widgets_Styles(self):
        self.search_Packages_Combo.setProperty('class', 'combo_Box')
        self.search_Packages_Button.setProperty('class', 'Button')
        self.update_Button.setProperty('class', 'Button')
        self.clear_Text_Button.setProperty('class', 'Button')
        self.install_package_Button.setProperty('class', 'Button')
        self.uninstall_package_Button.setProperty('class', 'Button')
        self.search_Packages_Line.setProperty('class', 'place_Holder')

        


    def Widgets_Layout(self):
        Main_Layout = QWidget()

        self.setCentralWidget(Main_Layout)
        self.update_Box_Layout = QVBoxLayout()
        self.search_Box_Layout = QHBoxLayout()
        self.search_Box_Layout.addWidget(self.search_Packages_Combo)
        self.search_Box_Layout.addWidget(self.search_Packages_Line)
        self.search_Box_Layout.addWidget(self.search_Packages_Button)
        self.search_Box_Layout.addWidget(self.install_package_Button)
        self.search_Box_Layout.addWidget(self.uninstall_package_Button)
        self.update_Box_Layout.addLayout(self.search_Box_Layout) 
        self.update_Box_Layout.addWidget(self.clear_Text_Button)   
        self.update_Box_Layout.addWidget(self.content_Prompt)
        self.update_Box_Layout.addWidget(self.update_Button)

        Main_Layout.setLayout(self.update_Box_Layout)



    def place_Holder_Settings(self, text_Check):
        if text_Check != '':
            self.search_Packages_Button.setEnabled(True)
            self.install_package_Button.setEnabled(True)
        else:
            self.search_Packages_Button.setEnabled(False)
            self.install_package_Button.setEnabled(False)


    def clear_Text(self):

        self.content_Prompt.clear()


    def settings_Combo(self):

        repo = ['Flathub', 'Fedora Linux']
        self.search_Packages_Combo.addItems(repo)

        
    def search_Package(self):

        if self.search_Packages_Combo.currentText() == 'Flathub':
            self.prompt_Process.start('flatpak', ['search', self.search_Packages_Line.text()])
            self.prompt_Process.readyReadStandardOutput.connect(self.stdout_search_Package) 
            self.prompt_Process.readyReadStandardError.connect(self.stdout_search_Package)

        elif self.search_Packages_Combo.currentText() == 'Fedora Linux':
            self.prompt_Process.start('dnf', ['search', self.search_Packages_Line.text()])
            self.prompt_Process.readyReadStandardOutput.connect(self.stdout_search_Package)



    def install_Package(self):
   
       if self.search_Packages_Combo.currentText() == 'Flathub':
           self.prompt_Process.start('pkexec', ['flatpak', 'install', 'flathub', self.search_Packages_Line.text(), '-y'])
           self.prompt_Process.readyReadStandardOutput.connect(self.stdout_install_Package)
           self.prompt_Process.readyReadStandardError.connect(self.stdout_install_Package)

       elif self.search_Packages_Combo.currentText() ==  'Fedora Linux':
           self.prompt_Process.start('pkexec', ['dnf', 'in', self.search_Packages_Line.text()])
           self.prompt_Process.readyReadStandardOutput.connect(self.stdout_install_Package)
           self.prompt_Process.readyReadStandardError.connect(self.stdout_install_Package)
           self.prompt_Process.readyReadStandardError.connect(self.stdout_search_Package)

    def uninstall_Package(self):
        
        if self.search_Packages_Combo.currentText() == 'Flathub':
            self.prompt_Process.start('flatpak', ['uninstall', self.search_Packages_Line.text(), '-y'])
            self.prompt_Process.readyReadStandardOutput.connect(self.stdout_uninstall_Package)
            self.prompt_Process.readyReadStandardError.connect(self.stdout_uninstall_Package)
        
        elif self.search_Packages_Combo.currentIndex() == 'Fedora Linux':
            self.prompt_Process.start('pkexec', ['remove', self.search_Packages_Line.text()])
            self.prompt_Process.readyReadStandardOutput.connect(self.stdout_uninstall_Package)
            self.prompt_Process.readyReadStandardError.connect(self.stdout_uninstall_Package)
    
    def update_System(self):

        self.prompt_Process.start('pkexec', ['dnf',  'up', '-y'])
        self.prompt_Process.start('flatpak', ['update', '-y'])
        self.prompt_Process.readyReadStandardOutput.connect(self.stdout_update)
        self.prompt_Process.readyReadStandardError.connect(self.stdout_update)

    

    def stdout_search_Package(self):
        
        self.content_Prompt.insertPlainText(self.prompt_Process.readAllStandardOutput().data().decode('utf-8'))
        self.content_Prompt.insertPlainText(self.prompt_Process.readAllStandardError().data().decode('utf-8'))

    def stdout_install_Package(self):

        self.content_Prompt.insertPlainText(self.prompt_Process.readAllStandardOutput().data().decode('utf-8'))
        self.content_Prompt.insertPlainText(self.prompt_Process.readAllStandardError().data().decode('utf-8'))
        self.content_Prompt.ensureCursorVisible()


    def stdout_uninstall_Package(self):
        self.content_Prompt.insertPlainText(self.prompt_Process.readAllStandardOutput().data().decode('uft-8'))
        self.content_Prompt.insertPlainText(self.prompt_Process.readAllStandardError().data().decode('utf-8'))

    def stdout_update(self):

        self.content_Prompt.insertPlainText(self.prompt_Process.readAllStandardOutput().data().decode('utf-8'))
        self.content_Prompt.insertPlainText(self.prompt_Process.readAllStandardError().data().decode('utf-8'))
        self.content_Prompt.ensureCursorVisible()


    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = main_Windown()
    with open("system_form.css") as form:
        style = form.read() 
    app.setStyleSheet(style)
    sys.exit(app.exec())