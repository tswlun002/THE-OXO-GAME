import sys
import random
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from LoopThread import *
from GameClient import *


# from OXOTextClient import*
class mywidget(QWidget, GameClient):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        GameClient.__init__(self)
        self.setup_window()
        self.connectionLayout()
        self.add_keyboard_positions()

    """
    * Set up the window size, tittle, logo and background picture
    """

    def setup_window(self):
        self.shape = None
        self.setGeometry(100, 100, 100, 300)
        self.setWindowTitle('THE OXO GAME')
        self.setWindowIcon(QIcon("images.jfif"))  # sets the icon for the window
        back_pic = QPalette()
        # sets the background picture
        pixmap = QPixmap("time-lapse-moving-cloud-on-blue-sky-background_4s9ilq19e__F0000.png")
        pixmap = pixmap.scaledToWidth(2000)
        back_pic.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(back_pic)
        self.setPalette(back_pic)

    """
    * Design connection layout
    * User will able to enter address but its defaulted to local host connection
    """

    def connectionLayout(self):
        # make connection the client and horizontal layout
        self.server_IP = QLabel("SERVER:")
        self.server_IP.setFont(QFont('Times', 10, 10))  # set font
        self.IP_space = QLineEdit('localhost')
        self.IP_space.setPlaceholderText("Opponent's IP Address")
        self.conn_button = QPushButton("CONNECT", self)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.server_IP)
        hbox.addWidget(self.IP_space)
        hbox.addWidget(self.conn_button)
        self.hbox_widget0 = QWidget()
        self.hbox_widget0.setLayout(hbox)

        # make board with positions and make layout

    def makeBlankBackgroundGif(self):
        pixmap = QPixmap("blank.gif")
        pixmap = pixmap.scaledToWidth(50)
        return pixmap

    """
    * Set Blank git on button positions on the keyboard
    """

    def setBlankBackgroundGif(self, position: QLabel):
        self.pixmap = self.makeBlankBackgroundGif()
        position.setPixmap(self.pixmap)

    """
     *  Make keyboard position
     """

    def add_keyboard_positions(self):
        # zero ,1st, 2nd position
        self.position0 = QLabel()
        self.position1 = QLabel()
        self.position2 = QLabel()
        self.setBlankBackgroundGif(self.position0)
        self.setBlankBackgroundGif(self.position1)
        self.setBlankBackgroundGif(self.position2)
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.position0)
        hbox.addWidget(self.position1)
        hbox.addWidget(self.position2)
        self.hbox_widget2 = QWidget()
        self.hbox_widget2.setLayout(hbox)
        # 3rd,4th,5th positions
        self.position3 = QLabel()
        self.position4 = QLabel()
        self.position5 = QLabel()
        self.setBlankBackgroundGif(self.position3)
        self.setBlankBackgroundGif(self.position4)
        self.setBlankBackgroundGif(self.position5)
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.position3)
        hbox.addWidget(self.position4)
        hbox.addWidget(self.position5)
        self.hbox_widget3 = QWidget()
        self.hbox_widget3.setLayout(hbox)
        self.tool = QLabel()
        # 6th,7th,8th positions
        self.score = QLabel('')
        self.score.setFont(QFont('Courier', 20, 2))
        self.score_2 = QLabel('')
        self.score_2.setFont(QFont('Courier', 20, 2))
        # adds the blank pictures for the game board
        self.position6 = QLabel()
        self.position7 = QLabel()
        self.position8 = QLabel()
        self.setBlankBackgroundGif(self.position6)
        self.setBlankBackgroundGif(self.position7)
        self.setBlankBackgroundGif(self.position8)
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.position6)
        hbox.addWidget(self.position7)
        hbox.addWidget(self.position8)
        self.hbox_widget4 = QWidget()
        self.hbox_widget4.setLayout(hbox)

        # make positions vertical from each other
        self.board = QLabel("    GAME BOARD:")
        self.board.setFont(QFont('Times', 12, 2))
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.board)
        vbox.addWidget(self.hbox_widget2)
        vbox.addWidget(self.hbox_widget3)
        vbox.addWidget(self.hbox_widget4)
        vbox.addWidget(self.tool)
        self.vbox_widget_positions = QWidget()
        self.vbox_widget_positions.setLayout(vbox)
        # make my shape label  horizontal with the shape
        self.iput_move = QLabel('             POSITION KEY-BOARD:')
        self.iput_move.setFont(QFont('Times', 11, 1))
        # self.input_move_space = QLineEdit()

        # buttons that be used to play OXO GAME instead device keyboard
        self.button0 = QPushButton('0')
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        # makes the first row of the blank pictures for the Game Board
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.button0)
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        self.buttonsRow0 = QWidget()
        self.buttonsRow0.setLayout(hbox)
        # makes the second row of the blank pictures for the Game Board
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.button3)
        hbox.addWidget(self.button4)
        hbox.addWidget(self.button5)
        self.buttonRow1 = QWidget()
        self.buttonRow1.setLayout(hbox)

        # makes the third row of the blank pictures for the Game Board
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.button6)
        hbox.addWidget(self.button7)
        hbox.addWidget(self.button8)
        self.buttonRow2 = QWidget()
        self.buttonRow2.setLayout(hbox)
        # Make buttons at row zero, one and two vertically to each other
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.buttonsRow0)
        vbox.addWidget(self.buttonRow1)
        vbox.addWidget(self.buttonRow2)
        self.buttonsRow3 = QWidget()
        self.buttonsRow3.setLayout(vbox)

        hbox = QVBoxLayout(self)
        hbox.addWidget(self.iput_move)
        hbox.addWidget(self.buttonsRow3)
        self.move_space = QWidget()
        self.move_space.setLayout(hbox)

        # label of shape of each client and sets the font
        self.shape = QLabel("MY SHAPE:")
        self.score_1 = QLabel('SCORE O:')
        self.score_2 = QLabel('SCORE X:')
        self.score_1_X = QLabel('')
        self.score_2_O = QLabel('')
        self.score_1_X.setFont(QFont('Times', 12, 1))
        self.score_2_O.setFont(QFont('Times', 12, 1))
        self.shape.setFont(QFont('Times', 12, 1))
        self.score_1.setFont(QFont('Times', 12, 1))
        self.score_2.setFont(QFont('Times', 12, 1))
        self.lbl = QLabel(self)

        # makes the shape label and the player shape  vertically
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.shape)
        vbox.addWidget(self.lbl)
        self.B_10 = QWidget()
        self.B_10.setLayout(vbox)
        # makes the label of the scores for both users vertically
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.score_1)
        vbox.addWidget(self.score_2)
        self.C_10 = QWidget()
        self.C_10.setLayout(vbox)
        # makes the scores for both users vertically
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.score_1_X)
        vbox.addWidget(self.score_2_O)
        self.D_10 = QWidget()
        self.D_10.setLayout(vbox)
        # makes prints the above widgets horizontally
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.B_10)
        hbox.addWidget(self.C_10)
        hbox.addWidget(self.D_10)
        self.E_10 = QWidget()
        self.E_10.setLayout(hbox)
        # makes the scores
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.move_space)
        vbox.addWidget(self.E_10)
        self.shape_label = QWidget()
        self.shape_label.setLayout(vbox)
        # make shape of each client and layout positions & shape hozintally
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.vbox_widget_positions)
        hbox.addWidget(self.shape_label)
        self.hbox_widget5 = QWidget()
        self.hbox_widget5.setLayout(hbox)
        # make textedit to give appropriate messages
        self.message_label = QLabel(" MESSAGES:", self)
        self.message_label.setFont(QFont('Times', 12, 2))
        self.text_dit = QTextEdit()
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.message_label)
        vbox.addWidget(self.text_dit)
        self.vbox_widget_messages = QWidget()
        self.vbox_widget_messages.setLayout(vbox)
        # make combo for play again ,make exit button  and make vertical layout
        self.play_again_label = QLabel("PLAY AGAIN:", self)
        self.play_again_label.setFont(QFont('Times', 11, 2))
        # combo for play again
        combo = ['YES', 'NO']
        self.combo = QComboBox(self)
        self.combo.setEnabled(False)
        for x in combo:
            self.combo.addItem(x)
        self.combo.activated.connect(self.combo_box)  # connect close signal with combo box
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.play_again_label)
        hbox.addWidget(self.combo)
        self.play_again = QWidget()
        self.play_again.setLayout(hbox)

        # Init exit button and Handle Exit button event
        self.exit_button = QPushButton("EXIT", self)
        self.handleExitEvent(self.exit_button)
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.play_again)
        vbox.addWidget(self.exit_button)
        self.play_again_exit = QWidget()
        self.play_again_exit.setLayout(vbox)
        # make play again combo, exit button and text edit horizontal from each other
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.vbox_widget_messages)
        hbox.addWidget(self.play_again_exit)
        self.hbox_widget6 = QWidget()
        self.hbox_widget6.setLayout(hbox)
        # make all the layout in order and display them
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.hbox_widget0)
        vbox.addWidget(self.hbox_widget5)
        vbox.addWidget(self.hbox_widget6)
        self.hbox_widget7 = QWidget()
        self.setLayout(vbox)

        # self.game = OXOGameClient()
        # creat a thread
        self.enable_signal()
        self.startConnection()
        self.handle_keyBoardEvents()

        self.cross = QPixmap("cross.gif")
        self.nought = QPixmap("nought.gif")
        self.blank = QPixmap("blank.gif")
        self.icon_O = self.nought
        self.icon_X = self.cross
        self.positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]  # list for postions

        self.O_score = 0
        self.X_score = 0

    """
    * Enable signaling so that game can communicate with server
    """

    def enable_signal(self):
        self.thread = LoopThread()
        self.thread.game_signal.connect(self.loop_slot)  # connect signals to slots

    """
    * Handle connect button event by starting connection
    """

    def startConnection(self):
        self.conn_button.clicked.connect(self.conn)  # connect close signal with the connect  button

    """
    * Handle clicked button of each position the keyboard
    """

    def handle_keyBoardEvents(self):
        self.button0.clicked.connect(lambda:self.sendSignal(0))
        self.button1.clicked.connect(lambda:self.sendSignal(1))
        self.button2.clicked.connect(lambda:self.sendSignal(2))
        self.button3.clicked.connect(lambda:self.sendSignal(3))
        self.button4.clicked.connect(lambda:self.sendSignal(4))
        self.button5.clicked.connect(lambda:self.sendSignal(5))
        self.button6.clicked.connect(lambda:self.sendSignal(6))
        self.button7.clicked.connect(lambda:self.sendSignal(7))
        self.button8.clicked.connect(lambda:self.sendSignal(8))

    """
    * Handle the event of the exit button
    """

    def handleExitEvent(self, exit: QPushButton):
        exit.clicked.connect(
            self.exit_game)  # connect exit button with  exit fuction to close window if exit is clicked

    """
    * Get messages from server 
    """

    def loop_slot(self, msg):  # slot which handles signal from thread
        self.write_to_edit(msg)

    """
    * Start the connection by sending client address & port number 
    """

    def conn(self):
        try:
            self.thread.connect_(self.IP_space.displayText())  # connecting to server
            self.thread.start()  # starting thread for play loop to begin
            self.text_dit.setFontPointSize(12)
            self.text_dit.append("Connected to Client")  # set messege on text edit when you are connected
        except Exception as t:
            print(t)

    """
    * Handle game message or status of the game or user moves 
    """

    def write_to_edit(self, msg):  # Function to handle messages
        self.shape = msg[-1]
        if msg[:msg.find(",")] == "new game" and self.shape == 'O':
            self.icon_O = self.nought
            self.lbl.setPixmap(self.icon_O)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg[:8] + "\n")
            self.score_1_X.setText("{0} ".format((self.O_score)))
            self.score_2_O.setText("{0} ".format((self.X_score)))

        elif msg[:msg.find(",")] == "new game" and self.shape == 'X':
            self.icon_X = self.cross
            self.lbl.setPixmap(self.icon_X)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg[:8] + "\n")
            self.score_2_O.setText("{0} ".format((self.X_score)))
            self.score_1_X.setText("{0} ".format((self.O_score)))

        elif msg == 'your move':
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg + "\n")
            self.combo.setEnabled(False)
            self.enableButtons(True)

        elif msg == "opponents move":  # tell each it's oppenent move
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg + "\n")
            self.combo.setEnabled(False)
            self.enableButtons(False)

        elif msg == "invalid move":  # invalid and write invalid move
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg + "\n")

        elif msg[:msg.find(",")] == "game over":  # check game over
            self.conn_button.setEnabled(False)
            if msg[-1] == 'X' or msg[-1] == 'O':
                self.text_dit.setFontPointSize(16)
                redColor = QColor(255, 0, 0)
                self.text_dit.setTextColor(redColor)
                self.text_dit.append('***Game over, the winner is ' + (msg[-1]) + "***" + "\n")
                self.text_dit.setFontPointSize(12)
                blackColor = QColor(0, 0, 0)
                self.text_dit.setTextColor(blackColor)
                if msg[-1] == "X":
                    self.X_score += 1

                elif msg[-1] == "O":
                    self.O_score += 1

            else:
                self.text_dit.setFontPointSize(12)
                self.text_dit.append("Game over, It's a tie!" + "\n")

            self.score_1_X.setText("{0} ".format((self.O_score)))
            self.score_2_O.setText("{0} ".format((self.X_score)))

        elif msg == 'play again':
            self.conn_button.setEnabled(False)
            self.combo.setEnabled(True)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append("Click YES if you want to play again!!!" + "\n")
            # get answer from user
            # self.combo.activated.connect(self.ans)

        elif msg == 'exit game':  # play again game or exist game
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append("Press Exit button to Exit game!!!" + "\n")


        elif msg[:msg.find(",")] == "valid move":  # check valid move then apply method(play the game)
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append(msg[:10] + '\n')
            pixmap_x = QPixmap('cross.gif')
            pixmap_o = QPixmap('nought.gif')
            position = msg.split(",")[2]
            self.shape = msg[-3]
            # put shape on position if the position button is clicked
            keywordPositions = [self.position0,self.position1,self.position2,self.position3,self.position4
                                ,self.position5,self.position6,self.position7,self.position8]
            PixMaType = {"X":pixmap_x,"O": pixmap_o}

            keywordPositions[int(position)].setPixmap(PixMaType[self.shape])

    """
    * When enable is True, button are enable
    * Else disabled 
    """
    def enableButtons(self,enabler:bool):
        self.button0.setEnabled(enabler)
        self.button1.setEnabled(enabler)
        self.button2.setEnabled(enabler)
        self.button3.setEnabled(enabler)
        self.button4.setEnabled(enabler)
        self.button5.setEnabled(enabler)
        self.button6.setEnabled(enabler)
        self.button7.setEnabled(enabler)
        self.button8.setEnabled(enabler)
    """
    * Tell Sever which position is played 
    """
    def sendSignal(self,position:int):
        try:
            self.thread.send_message(self.positions[position])
        except Exception as r:
            print(r)
    """
    * Handle event of the combo box 
    * When user choose Yes, new game is started 
    * When user chooses No, exit game
    """
    def combo_box(self):
        self.conn_button.setEnabled(False)
        self.ans = self.combo.currentText()
        if self.ans == 'YES':  # if answer is yes , clear board and text edit an d write new game on text edit
            self.position0.setPixmap(self.blank)
            self.position1.setPixmap(self.blank)
            self.position2.setPixmap(self.blank)
            self.position3.setPixmap(self.blank)
            self.position4.setPixmap(self.blank)
            self.position5.setPixmap(self.blank)
            self.position6.setPixmap(self.blank)
            self.position7.setPixmap(self.blank)
            self.position8.setPixmap(self.blank)
            self.text_dit.clear()
            self.text_dit.setFontPointSize(12)
            self.text_dit.append('New game with same opponent.' + "\n")
            self.thread.send_message("y")

        # If a user chooses NO in the combobox
        elif self.ans == 'NO':
            self.conn_button.setEnabled(False)
            self.text_dit.setFontPointSize(12)
            self.text_dit.append('Game ended!!!!' + "\n")
            self.thread.send_message("n")

    # exit  fuction
    def exit_game(self):
        self.close()


"""
* Start the application 
"""
def main():
    app = QApplication(sys.argv)
    x = mywidget()
    x.show()
    sys.exit(app.exec_())


main()
