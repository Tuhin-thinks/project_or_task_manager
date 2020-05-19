import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QPushButton
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from package import explore_window
from package import project_manager as PM
from package import edit_entries as EDIT
from package import entrylist
from package import input_dialog
from package import detailswindow
import threading
import sqlite3
from sqlite3 import Error
from functools import partial
import datetime


def create_connection():
    DataBaseName = "project_data.db"  # data base name
    try:
        con = sqlite3.connect(DataBaseName)
        return con
    except Error:
        pass


def table_col_info(cursor, tablename):  # return all avaiaable column names in a table
    cursor.execute('PRAGMA TABLE_INFO({})'.format(tablename))
    info = cursor.fetchall()
    column_names = []
    for col in info:
        column_names.append(col[1])


def createtable(conn, query):
    try:
        cursor_obj = conn.cursor()
        cursor_obj.execute(query)
        conn.commit()
        return "success"
    # print('Table Successfully Created!')
    except:
        return "failure"


def deleterow(tablename, item_id):  # delete a row in a table
    conn = create_connection()
    delete_query = f"DELETE FROM {tablename} WHERE id={item_id}"
    cursor_obj = conn.cursor()
    cursor_obj.execute(delete_query)
    conn.commit()
    conn.close()


def insertintotable(conn, query, value):
    cursor = conn.cursor()
    cursor.execute(query, value)
    conn.commit()
    print('Data Inserted successfully!')


def fetchfromdb(conn):
    query = "SELECT * FROM Project_Data"
    curson_obj = conn.cursor()
    curson_obj.execute(query)
    rows = curson_obj.fetchall()

    entry_list = []
    for row in rows:
        entry_list.append(row)
    return entry_list


class EditDB(QMainWindow):
    def __init__(self, parent, data_list, item_id):
        super().__init__()
        self.ui = EDIT.Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent_window = parent
        self.data_list = data_list
        self.item_id = item_id
        self.database = "project_data.db"
        self.tablename = "Project_data"

        self.fill_data()
        self.ui.pushButton_cancel.clicked.connect(self.returntoparent)
        self.ui.pushButton_confirm.clicked.connect(self.startupdate)
        self.ui.pushButton_delete.clicked.connect(self.deleterow)

    def deleterow(self):
        deleterow(self.tablename, self.item_id)

    def startupdate(self):
        updatedb = threading.Thread(target=self.updateDB)
        updatedb.start()

    def updateDB(self):
        conn = create_connection()
        cursor_obj = conn.cursor()
        table_col_info(cursor_obj, self.tablename)

        project_name = self.ui.lineEdit_projectname.text()
        definition = self.ui.textEdit_projectdef.toHtml()
        price = self.ui.lineEdit_price.text()
        submitdate = self.ui.lineEdit_submitdate.text()
        complete_status = self.ui.comboBox_completestatus.currentText()

        try:
            update_query = f'''UPDATE Project_data SET project_name=?, definition=?, price=?, submitDate=?, 
complete_status=? WHERE id=? '''
            cursor_obj.execute(update_query,
                               tuple([project_name, definition, price, submitdate, complete_status, self.item_id]))
            conn.commit()
            print("DataBase Updated Successfully...")
            # return 1
        except Exception as e:
            print("Some error occurred! ", e)
            sys.exit()
        self.returntoparent()
        conn.close()

    def returntoparent(self):
        self.parent_window.show()
        self.close()

    def fill_data(self):
        self.ui.lineEdit_projectname.setText(self.data_list[1])
        self.ui.lineEdit_price.setText(self.data_list[3])
        self.ui.lineEdit_submitdate.setText(self.data_list[4])
        if self.data_list[-1] == 'complete':
            self.ui.comboBox_completestatus.setCurrentIndex(0)
        else:  # for pending case
            self.ui.comboBox_completestatus.setCurrentIndex(1)
        self.ui.textEdit_projectdef.setHtml(self.data_list[2])


class DetailsWindow(QDialog):
    def __init__(self, display_text, parent_window):
        super().__init__()
        self.ui = detailswindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.display_text = display_text
        self.parent_window = parent_window
        self.ui.textEdit_details.setHtml(display_text)
        self.ui.pushButton_close.clicked.connect(self.returntoparent)

    def returntoparent(self):
        self.parent_window.show()
        self.close()


class EntryListwindow(QMainWindow):
    def __init__(self, parent, data):
        super().__init__()
        self.ui = entrylist.Ui_MainWindow()
        self.ui.setupUi(self)

        self.data = data
        self.parentwindow = parent
        for i in self.data:
            self.ui.item_list.addItem(f"{i[0]}.{i[1]} -- {i[3]}")

        self.ui.pushButton_cancel.clicked.connect(self.returntoparent)
        self.ui.item_list.itemClicked.connect(self.edit_db)

    def edit_db(self, item):
        item_id = item.text().split('.')[0]
        item_data = []
        for item in self.data:
            item_values = item[0]
            if int(item_values) == int(item_id):
                item_data = item

        self.editwindow = EditDB(parent=self.parentwindow, item_id=item_id, data_list=item_data)
        self.editwindow.show()
        self.close()

    def returntoparent(self):
        self.parentwindow.show()
        self.close()


class FetchFromDataBase():
    def __init__(self, parent):
        self.sharedict = {}
        self.parentwindow = parent
        self.manageoperations()

    def manageoperations(self):
        conn = create_connection()
        self.entry_list = fetchfromdb(conn)
        self.parentwindow.ui.pushButton_editentriest.setEnabled(True)  # enable the edit button
        self.showentrylistwindow = EntryListwindow(self.parentwindow, self.entry_list)
        self.showentrylistwindow.show()
        self.parentwindow.hide()


class AddToDataBase:
    success_signal = pyqtSignal()
    close_signal = pyqtSignal(str, str)

    def __init__(self, share_dict):
        self.share_dict = share_dict
        self.manageOperations()

    def manageOperations(self):
        query_insert = "INSERT INTO Project_Data(project_name,definition,price,submitDate,complete_status) VALUES(?,?,?,?,?)"
        # id = self.share_dict['id']
        project_name = self.share_dict['project_name']
        definition = self.share_dict['definition']
        price = self.share_dict['price']
        submitDate = self.share_dict['submitDate']
        completestatus = self.share_dict['complete_status']

        conn = create_connection()
        cursor = conn.cursor()
        table_name = 'Project_Data'

        # see if table exists or not
        search_table = f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        search = cursor.execute(search_table)

        if search.fetchone()[0] == 0:
            query_create = "CREATE TABLE Project_Data(id integer PRIMARY KEY,project_name text, definition text, price text, submitDate text, complete_status VARCHAR(30))"
            response = createtable(conn, query_create)
            if response == 'success':
                print("Table Created Successfully!")
            else:
                print("Cannot Create Table!")
        else:  # insert into table, if table is non-existant
            value = [project_name, definition, price, submitDate, completestatus]
            insertintotable(conn, query_insert, tuple(value))


class ExploreWindow(QDialog):
    def __init__(self, parent_win):
        super().__init__()
        self.ui = explore_window.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.parent_win = parent_win
        # print("I am here")
        self.ui.pushButton_cancel.clicked.connect(self.returnToParent)
        self.ui.pushButton_ok.clicked.connect(self.displayDetails)
        self.show()

    def displayDetails(self):
        curr_index = self.ui.options.currentIndex()
        display_text = ''
        tot_value = 0.0
        if curr_index != 0:
            operation_type = self.ui.options.currentText()
            if 'pending jobs' in operation_type.lower():
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                for project in entry_list:
                    if project[5].lower().strip() == 'pending':
                        display_text += f'{project[1]}\n'
                        if 'worth' in operation_type.lower():
                            worth = project[3]
                            if worth.strip(' USD').isdigit():
                                value = float(worth.strip(' USD'))
                                tot_value += value
                    else:
                        pass
                if curr_index in [1, 10]:
                    pass
                elif curr_index == 2:
                    display_text = f'Total Worth of all pending project are {tot_value} USD'
            elif 'last submission' in operation_type.lower():
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                for project in entry_list:
                    display_text = ''
                    if project[-1] == 'complete':
                        mod_list = list(map(str, project[1:]))
                        for item in mod_list:
                            display_text += f'<p>{item}</p>'
                display_text = 'You last submission details is as follows:<p>' + display_text + '</p>'
            elif 'nearest submission' in operation_type.lower():
                min_diff = datetime.timedelta(0)
                current_date = datetime.datetime.strptime(
                    datetime.datetime.strftime(datetime.datetime.today(), '%d.%m.%Y'), '%d.%m.%Y')
                conn = create_connection()
                entry_list = fetchfromdb(conn)
                for pos, project in enumerate(entry_list):
                    submit_date = project[-2]
                    complete_status = project[-1]
                    if complete_status == 'pending':
                        print(submit_date)
                        submit_date = datetime.datetime.strptime(str(submit_date), '%d.%m.%Y')
                        if min_diff == 0 and pos == 0:
                            min_diff = current_date - submit_date
                        else:
                            diff = current_date - submit_date
                            if diff < min_diff:
                                min_diff = diff
                                display_text = f'Project "{project[1]}" has to be submitted nearly.'  # project name
                if display_text == '':
                    display_text = "No Projects Left To be Submitted."

            self.displaywindow = DetailsWindow(display_text, self)
            self.displaywindow.show()
        # self.

    def returnToParent(self):
        self.parent_win.show()
        self.close()


class AcceptWindow(QMainWindow):
    close_signal = pyqtSignal(str, str)

    def __init__(self, key_string):
        super().__init__()
        self.ui = input_dialog.Ui_MainWindow()
        self.ui.setupUi(self)

        self.key_string = key_string
        self.ui.pushButton_confirm.clicked.connect(self.input_validation)
        self.ui.pushButton_reset.clicked.connect(partial(self.ui.lineEdit_input.setText, ''))
        self.show()
        if self.key_string == "complete_status":
            self.ui.label_message.setText("Enter Project Status:\ncomplete or pending")
        elif self.key_string == "submitDate":
            self.ui.label_message.setText(
                "Enter Complete By Date in: dd.mm.yyyy format\n(and don't try to be creative\npress reset when needed)")
            self.ui.lineEdit_input.textEdited.connect(self.modifyinput)
        elif self.key_string == 'project_name':
            self.ui.label_message.setText("Enter The Project Name in short (under 30 chars)")
        elif self.key_string == 'price':
            self.ui.label_message.setText('Enter the amount of money you are receiving for the Project')
        # else:
        #     self.ui.lineEdit_input.textEdited.connect(self.input_validation)

    def modifyinput(self):
        text = self.ui.lineEdit_input.text()
        if len(text) == 2 or len(text) == 5:
            text += '.'
            self.ui.lineEdit_input.setText(text)

    def input_validation(self):
        if self.ui.lineEdit_input.text().strip(' ') != '' and len(self.ui.lineEdit_input.text()) >= 1:
            if self.key_string == 'submitDate':
                if len(self.ui.lineEdit_input.text()) == 10 and len(self.ui.lineEdit_input.text().split('.')) == 3:
                    self.close_signal.emit(self.ui.lineEdit_input.text(), self.key_string)
            elif self.key_string == "complete_status":
                if self.ui.lineEdit_input.text() == 'complete' or self.ui.lineEdit_input.text() == 'pending':
                    self.close_signal.emit(self.ui.lineEdit_input.text(), self.key_string)
                else:
                    self.ui.statusbar.showMessage('complete status has to be "complete" or "pending" in lower-case')
            else:
                self.close_signal.emit(self.ui.lineEdit_input.text(), self.key_string)


class manager_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = PM.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionClose_File.triggered.connect(self.close)
        self.ui.actionExplore.triggered.connect(self.exploreWindow)
        # add project definition to the dictionary and resets the instance
        self.ui.pushButton_addprojdef.clicked.connect(self.definition_validation)
        self.project_def = ""
        self.input_dict = {}

        self.ui.pushButton_completebytime.clicked.connect(self.accept_datetime)
        self.ui.pushButton_projectprice.clicked.connect(self.add_price)
        self.ui.pushButton_editentriest.clicked.connect(self.load_file_path)
        self.ui.pushButton_completestatus.clicked.connect(self.getCompleteStatus)
        self.ui.pushButton_loadprojectdef.clicked.connect(self.accept_projectname)
        self.ui.pushButton_addproject.clicked.connect(self.settodatabase)
        self.ui.pushButton_editentriest.clicked.connect(self.edittodatabase)

    def exploreWindow(self):
        self.openexplore = ExploreWindow(self)
        self.openexplore.show()
        self.hide()

    def edittodatabase(self):
        self.ui.pushButton_editentriest.setDisabled(True)
        self.fetchdata = FetchFromDataBase(self)

    def getCompleteStatus(self):
        self.ui.pushButton_completestatus.setDisabled(True)
        self.accept_window = AcceptWindow('complete_status')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        self.hide()

    def settodatabase(self):
        if len(self.input_dict.keys()) == 5:  # ['project_name,definition,price,submitDate,complete_status]
            self.ui.textEdit_projectdefinition.clear()

            # write and reset
            db_thread = threading.Thread(target=AddToDataBase, args=(self.input_dict,))
            db_thread.start()
            with open('database.txt', 'a') as ff:
                ff.write(str(self.input_dict) + '\n')
            self.input_dict = {}  # clearing input dict
            for pushbutton in self.findChildren(QPushButton):
                if not pushbutton.isEnabled():
                    pushbutton.setEnabled(True)
        else:
            self.ui.statusBar.setStyleSheet('color: red')
            self.ui.statusBar.showMessage('Details are not valid to add to Data Base. Please RECHECK!!!')

    def accept_projectname(self):
        self.ui.pushButton_loadprojectdef.setDisabled(True)
        self.accept_window = AcceptWindow('project_name')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        # self.accept_window.close_signal.connect(self.show)
        self.hide()

    def destroy_inputwindow(self, input_string, key_string):  # also this saves the input data to the respective key
        self.accept_window.close()
        self.show()
        self.input_string = input_string
        self.input_dict[key_string] = self.input_string.strip()

    def increase_counter(self):
        pass

    def load_file_path(self):
        pass

    def add_price(self):
        self.ui.pushButton_projectprice.setDisabled(True)
        self.accept_window = AcceptWindow('price')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        self.hide()

    def accept_datetime(self):
        self.ui.pushButton_completebytime.setDisabled(True)
        self.accept_window = AcceptWindow('submitDate')
        self.accept_window.close_signal.connect(self.destroy_inputwindow)
        self.hide()

    def definition_validation(self):
        text = self.ui.textEdit_projectdefinition.toHtml()
        if len(text) != 0:
            self.input_dict['definition'] = text

            self.ui.pushButton_addprojdef.setDisabled(True)
            self.ui.textEdit_projectdefinition.clear()

    def closeEvent(self, event):  # function to implement code confirmation
        close = QMessageBox()
        close.setWindowTitle("Exit")
        close.setText("Are You Sure You Want To Quit?")
        close.setIcon(QMessageBox.Information)
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = manager_window()
    w.show()
    sys.exit(app.exec_())
