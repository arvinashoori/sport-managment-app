import tkinter as tk
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as sql
from tkinter import filedialog as fd
import tksheet
from  tksheet import Sheet
import jdatetime
import pyautogui
import random
from fpdf import FPDF







con=sql.connect('mydb.db')
cur=con.cursor()

###################################################################################################

command1 =  '''CREATE TABLE IF NOT EXISTS harekata(shenase INTEGER PRIMARY KEY ,
                                                          gp_tamrini TEXT NOT NULL ,
                                                          azole_hadaf TEXT NOT NULL ,
                                                          harekat TEXT NOT NULL

                                                          )'''
        
cur.execute(command1) 
con.commit()

command3 =  '''CREATE TABLE IF NOT EXISTS athlee('athlee_code' INTEGER PRIMARY KEY ,
                                                          'athlee_name' TEXT NOT NULL ,                                                        
                                                          athlee_age INTEGER NOT NULL,
                                                          athlee_wheight INTEGER NOT NULL,
                                                          athlee_height INTEGER NOT NULL,
                                                          athlee_new_wheight INTEGER NOT NULL,
                                                          athlee_number INTEGER NOT NULL,
                                                          athlee_reshte INTEGER NOT NULL,
                                                          athlee_type INTEGER NOT NULL,
                                                          athlee_blood INTEGER NOT NULL,
                                                          athlee_surgery INTEGER NOT NULL

                                                          )'''
        
cur.execute(command3) 
con.commit()

command44 =  '''CREATE TABLE IF NOT EXISTS barname1(
                                                          b_name TEXT NOT NULL ,                                                        
                                                          b_azole_hadaf text NOT NULL,
                                                          b_gp_tamrini text NOT NULL ,
                                                          tekrar TEXT NULL ,
                                                          rest TEXT ,
                                                          tozih TEXT,
                                                          sett TEXT ,
                                                          onvan TEXT,
                                                          tozih_bar TEXT
                                                          )'''
        
cur.execute(command44) 
con.commit()

command55 =  '''CREATE TABLE IF NOT EXISTS barname_personal(person_date TEXT NOT NULL,
                                                          harekat_name TEXT NOT NULL,
                                                          person_name TEXT NOT NULL,                                                         
                                                          person_number INTEGER NOT NULL,
                                                          onvan  TEXT NOT NULL,
                                                          person_set TEXT NOT NULL,
                                                          person_tekrar TEXT NOT NULL,
                                                          person_tozi TEXT NOT NULL,
                                                          person_shenase TEXT NOT NULL,
                                                          person_rest TEXT NOT NULL
                                                                                                               

                                                          )'''
        
cur.execute(command55) 
con.commit()
###################################################################################################


def login(event = None):

    name1 = ent1.get()
    pass1 = ent2.get()
    if name1 == 'admin' and pass1 == 'admin':
       win2.state('normal')
       win.state('withdrawn')
       message_welcom = messagebox.showinfo('welcome','خوش آمديد')

    else:
       ent1.delete(0,END)
       ent2.delete(0,END)
       message_error = messagebox.showerror('Error','نام کاربري يا رمز عبور اشتباه')
       ent1.focus()

def eye():
    if ent2['show'] == '*':
        ent2['show'] = ''
    else :
        ent2['show'] = '*'

def emp(event = None):
            win3.state('normal')
            win3.lift()
            win.state('withdrawn')


            global name_ath1
            global onvan_ath1
            name_ath1 = lstro[0][1]
            onvan_ath1 = ent1105.get()
            tozi_ath1 = ent1106.get()

            row1100 = '''SELECT b_name FROM barname1  '''
            rf00 = cur.execute(row1100)
            lst1100 = list(rf00)


            row2200 = '''SELECT tekrar FROM barname1  '''
            rf2200 = cur.execute(row2200)
            lst2200 = list(rf2200)

            row3300 = '''SELECT rest FROM barname1  '''
            rf3300 = cur.execute(row3300)
            lst3300 = list(rf3300)

            row4400 = '''SELECT tozih FROM barname1  '''
            rf4400 = cur.execute(row4400)
            lst4400 = list(rf4400)

            row5500 = '''SELECT sett FROM barname1  '''
            rf5500 = cur.execute(row5500)
            lst5500 = list(rf5500)


            if len(lst1100)== 6 :

                  lbl11['text'] = lst1100[0][0]
                  lbl12['text'] = lst1100[1][0]
                  lbl13['text'] = lst1100[2][0]
                  lbl14['text'] = lst1100[3][0]
                  lbl15['text'] = lst1100[4][0]
                  lbl16['text'] = lst1100[5][0]
                #   lbl17['text'] = lst1100[6][0]
                #   lbl18['text'] = lst1100[7][0]
                #   lbl19['text'] = lst1100[8][0]
                #   lbl110['text'] = lst1100[9][0]
                #   lbl111['text'] = lst1100[10][0]

                  lblt11['text'] = lst2200[0][0]
                  lblt12['text'] = lst2200[1][0]
                  lblt13['text'] = lst2200[2][0]
                  lblt14['text'] = lst2200[3][0]
                  lblt15['text'] = lst2200[4][0]
                  lblt16['text'] = lst2200[5][0]
                #   lblt17['text'] = lst2200[6][0]
                #   lblt18['text'] = lst2200[7][0]
                #   lblt19['text'] = lst2200[8][0]
                #   lblt110['text'] = lst2200[9][0]
                #   lblt111['text'] = lst2200[10][0]

                  lblr11['text'] = lst3300[0][0]
                  lblr12['text'] = lst3300[1][0]
                  lblr13['text'] = lst3300[2][0]
                  lblr14['text'] = lst3300[3][0]
                  lblr15['text'] = lst3300[4][0]
                  lblr16['text'] = lst3300[5][0]
                #   lblr17['text'] = lst3300[6][0]
                #   lblr18['text'] = lst3300[7][0]
                #   lblr19['text'] = lst3300[8][0]
                #   lblr110['text'] = lst3300[9][0]
                #   lblr111['text'] = lst3300[10][0]

                  lblto11['text'] = lst4400[0][0]
                  lblto12['text'] = lst4400[1][0]
                  lblto13['text'] = lst4400[2][0]
                  lblto14['text'] = lst4400[3][0]
                  lblto15['text'] = lst4400[4][0]
                  lblto16['text'] = lst4400[5][0]
                #   lblto17['text'] = lst4400[6][0]
                #   lblto18['text'] = lst4400[7][0]
                #   lblto19['text'] = lst4400[8][0]
                #   lblto110['text'] = lst4400[9][0]
                #   lblto111['text'] = lst4400[10][0]

                  lblse11['text'] = lst5500[0][0]
                  lblse12['text'] = lst5500[1][0]
                  lblse13['text'] = lst5500[2][0]
                  lblse14['text'] = lst5500[3][0]
                  lblse15['text'] = lst5500[4][0]
                  lblse16['text'] = lst5500[5][0]
                #   lblse17['text'] = lst5500[6][0]
                #   lblse18['text'] = lst5500[7][0]
                #   lblse19['text'] = lst5500[8][0]
                #   lblse110['text'] = ls55400[9][0]
                #   lblse111['text'] = ls55400[10][0]

            elif len(lst1100)== 7 :
                  
                  lbl11['text'] = lst1100[0][0]
                  lbl12['text'] = lst1100[1][0]
                  lbl13['text'] = lst1100[2][0]
                  lbl14['text'] = lst1100[3][0]
                  lbl15['text'] = lst1100[4][0]
                  lbl16['text'] = lst1100[5][0]
                  lbl17['text'] = lst1100[6][0]
                #  lbl18['text'] = lst1100[7][0]
                #  lbl19['text'] = lst1100[8][0]
                #   lbl110['text'] = lst1100[9][0]
                #   lbl111['text'] = lst1100[10][0]

                  lblt11['text'] = lst2200[0][0]
                  lblt12['text'] = lst2200[1][0]
                  lblt13['text'] = lst2200[2][0]
                  lblt14['text'] = lst2200[3][0]
                  lblt15['text'] = lst2200[4][0]
                  lblt16['text'] = lst2200[5][0]
                  lblt17['text'] = lst2200[6][0]
                #  lblt18['text'] = lst2200[7][0]
                #  lblt19['text'] = lst2200[8][0]
                #   lblt110['text'] = lst2200[9][0]
                #   lblt111['text'] = lst2200[10][0]

                  lblr11['text'] = lst3300[0][0]
                  lblr12['text'] = lst3300[1][0]
                  lblr13['text'] = lst3300[2][0]
                  lblr14['text'] = lst3300[3][0]
                  lblr15['text'] = lst3300[4][0]
                  lblr16['text'] = lst3300[5][0]
                  lblr17['text'] = lst3300[6][0]
                 # lblr18['text'] = lst3300[7][0]
                 # lblr19['text'] = lst3300[8][0]
                #   lblr110['text'] = lst3300[9][0]
                #   lblr111['text'] = lst3300[10][0]

                  lblto11['text'] = lst4400[0][0]
                  lblto12['text'] = lst4400[1][0]
                  lblto13['text'] = lst4400[2][0]
                  lblto14['text'] = lst4400[3][0]
                  lblto15['text'] = lst4400[4][0]
                  lblto16['text'] = lst4400[5][0]
                  lblto17['text'] = lst4400[6][0]
                 # lblto18['text'] = lst4400[7][0]
                 # lblto19['text'] = lst4400[8][0]
                #   lblto110['text'] = lst4400[9][0]
                #   lblto111['text'] = lst4400[10][0]

            elif len(lst1100)== 8 :
                  
                  lbl11['text'] = lst1100[0][0]
                  lbl12['text'] = lst1100[1][0]
                  lbl13['text'] = lst1100[2][0]
                  lbl14['text'] = lst1100[3][0]
                  lbl15['text'] = lst1100[4][0]
                  lbl16['text'] = lst1100[5][0]
                  lbl17['text'] = lst1100[6][0]
                  lbl18['text'] = lst1100[7][0]
                #  lbl19['text'] = lst1100[8][0]
                #   lbl110['text'] = lst1100[9][0]
                #   lbl111['text'] = lst1100[10][0]

                  lblt11['text'] = lst2200[0][0]
                  lblt12['text'] = lst2200[1][0]
                  lblt13['text'] = lst2200[2][0]
                  lblt14['text'] = lst2200[3][0]
                  lblt15['text'] = lst2200[4][0]
                  lblt16['text'] = lst2200[5][0]
                  lblt17['text'] = lst2200[6][0]
                  lblt18['text'] = lst2200[7][0]
                #  lblt19['text'] = lst2200[8][0]
                #   lblt110['text'] = lst2200[9][0]
                #   lblt111['text'] = lst2200[10][0]

                  lblr11['text'] = lst3300[0][0]
                  lblr12['text'] = lst3300[1][0]
                  lblr13['text'] = lst3300[2][0]
                  lblr14['text'] = lst3300[3][0]
                  lblr15['text'] = lst3300[4][0]
                  lblr16['text'] = lst3300[5][0]
                  lblr17['text'] = lst3300[6][0]
                  lblr18['text'] = lst3300[7][0]
                #  lblr19['text'] = lst3300[8][0]
                #   lblr110['text'] = lst3300[9][0]
                #   lblr111['text'] = lst3300[10][0]

                  lblto11['text'] = lst4400[0][0]
                  lblto12['text'] = lst4400[1][0]
                  lblto13['text'] = lst4400[2][0]
                  lblto14['text'] = lst4400[3][0]
                  lblto15['text'] = lst4400[4][0]
                  lblto16['text'] = lst4400[5][0]
                  lblto17['text'] = lst4400[6][0]
                  lblto18['text'] = lst4400[7][0]
                #   lblto19['text'] = lst4400[8][0]
                #   lblto110['text'] = lst4400[9][0]
                #   lblto111['text'] = lst4400[10][0]

            elif len(lst1100)== 9 :
                  lbl11['text'] = lst1100[0][0]
                  lbl12['text'] = lst1100[1][0]
                  lbl13['text'] = lst1100[2][0]
                  lbl14['text'] = lst1100[3][0]
                  lbl15['text'] = lst1100[4][0]
                  lbl16['text'] = lst1100[5][0]
                  lbl17['text'] = lst1100[6][0]
                  lbl18['text'] = lst1100[7][0]
                  lbl19['text'] = lst1100[8][0]
                #   lbl110['text'] = lst1100[9][0]
                #   lbl111['text'] = lst1100[10][0]

                  lblt11['text'] = lst2200[0][0]
                  lblt12['text'] = lst2200[1][0]
                  lblt13['text'] = lst2200[2][0]
                  lblt14['text'] = lst2200[3][0]
                  lblt15['text'] = lst2200[4][0]
                  lblt16['text'] = lst2200[5][0]
                  lblt17['text'] = lst2200[6][0]
                  lblt18['text'] = lst2200[7][0]
                  lblt19['text'] = lst2200[8][0]
                #   lblt110['text'] = lst2200[9][0]
                #   lblt111['text'] = lst2200[10][0]

                  lblr11['text'] = lst3300[0][0]
                  lblr12['text'] = lst3300[1][0]
                  lblr13['text'] = lst3300[2][0]
                  lblr14['text'] = lst3300[3][0]
                  lblr15['text'] = lst3300[4][0]
                  lblr16['text'] = lst3300[5][0]
                  lblr17['text'] = lst3300[6][0]
                  lblr18['text'] = lst3300[7][0]
                  lblr19['text'] = lst3300[8][0]
                #   lblr110['text'] = lst3300[9][0]
                #   lblr111['text'] = lst3300[10][0]

                  lblto11['text'] = lst4400[0][0]
                  lblto12['text'] = lst4400[1][0]
                  lblto13['text'] = lst4400[2][0]
                  lblto14['text'] = lst4400[3][0]
                  lblto15['text'] = lst4400[4][0]
                  lblto16['text'] = lst4400[5][0]
                  lblto17['text'] = lst4400[6][0]
                  lblto18['text'] = lst4400[7][0]
                  lblto19['text'] = lst4400[8][0]
                #   lblto110['text'] = lst4400[9][0]
                #   lblto111['text'] = lst4400[10][0]
                  
            elif len(lst1100)== 10 :
                  lbl11['text'] = lst1100[0][0]
                  lbl12['text'] = lst1100[1][0]
                  lbl13['text'] = lst1100[2][0]
                  lbl14['text'] = lst1100[3][0]
                  lbl15['text'] = lst1100[4][0]
                  lbl16['text'] = lst1100[5][0]
                  lbl17['text'] = lst1100[6][0]
                  lbl18['text'] = lst1100[7][0]
                  lbl19['text'] = lst1100[8][0]
                  lbl110['text'] = lst1100[9][0]
                  #lbl111['text'] = lst1100[10][0]

                  lblt11['text'] = lst2200[0][0]
                  lblt12['text'] = lst2200[1][0]
                  lblt13['text'] = lst2200[2][0]
                  lblt14['text'] = lst2200[3][0]
                  lblt15['text'] = lst2200[4][0]
                  lblt16['text'] = lst2200[5][0]
                  lblt17['text'] = lst2200[6][0]
                  lblt18['text'] = lst2200[7][0]
                  lblt19['text'] = lst2200[8][0]
                  lblt110['text'] = lst2200[9][0]
                  #lblt111['text'] = lst2200[10][0]

                  lblr11['text'] = lst3300[0][0]
                  lblr12['text'] = lst3300[1][0]
                  lblr13['text'] = lst3300[2][0]
                  lblr14['text'] = lst3300[3][0]
                  lblr15['text'] = lst3300[4][0]
                  lblr16['text'] = lst3300[5][0]
                  lblr17['text'] = lst3300[6][0]
                  lblr18['text'] = lst3300[7][0]
                  lblr19['text'] = lst3300[8][0]
                  lblr110['text'] = lst3300[9][0]
                  #lblr111['text'] = lst3300[10][0]

                  lblto11['text'] = lst4400[0][0]
                  lblto12['text'] = lst4400[1][0]
                  lblto13['text'] = lst4400[2][0]
                  lblto14['text'] = lst4400[3][0]
                  lblto15['text'] = lst4400[4][0]
                  lblto16['text'] = lst4400[5][0]
                  lblto17['text'] = lst4400[6][0]
                  lblto18['text'] = lst4400[7][0]
                  lblto19['text'] = lst4400[8][0]
                  lblto110['text'] = lst4400[9][0]
                  #lblto111['text'] = lst4400[10][0]
                  
            elif len(lst1100)== 11 :
                  lbl11['text'] = lst1100[0][0]
                  lbl12['text'] = lst1100[1][0]
                  lbl13['text'] = lst1100[2][0]
                  lbl14['text'] = lst1100[3][0]
                  lbl15['text'] = lst1100[4][0]
                  lbl16['text'] = lst1100[5][0]
                  lbl17['text'] = lst1100[6][0]
                  lbl18['text'] = lst1100[7][0]
                  lbl19['text'] = lst1100[8][0]
                  lbl110['text'] = lst1100[9][0]
                  lbl111['text'] = lst1100[10][0]

                  lblt11['text'] = lst2200[0][0]
                  lblt12['text'] = lst2200[1][0]
                  lblt13['text'] = lst2200[2][0]
                  lblt14['text'] = lst2200[3][0]
                  lblt15['text'] = lst2200[4][0]
                  lblt16['text'] = lst2200[5][0]
                  lblt17['text'] = lst2200[6][0]
                  lblt18['text'] = lst2200[7][0]
                  lblt19['text'] = lst2200[8][0]
                  lblt110['text'] = lst2200[9][0]
                  lblt111['text'] = lst2200[10][0]

                  lblr11['text'] = lst3300[0][0]
                  lblr12['text'] = lst3300[1][0]
                  lblr13['text'] = lst3300[2][0]
                  lblr14['text'] = lst3300[3][0]
                  lblr15['text'] = lst3300[4][0]
                  lblr16['text'] = lst3300[5][0]
                  lblr17['text'] = lst3300[6][0]
                  lblr18['text'] = lst3300[7][0]
                  lblr19['text'] = lst3300[8][0]
                  lblr110['text'] = lst3300[9][0]
                  lblr111['text'] = lst3300[10][0]

                  lblto11['text'] = lst4400[0][0]
                  lblto12['text'] = lst4400[1][0]
                  lblto13['text'] = lst4400[2][0]
                  lblto14['text'] = lst4400[3][0]
                  lblto15['text'] = lst4400[4][0]
                  lblto16['text'] = lst4400[5][0]
                  lblto17['text'] = lst4400[6][0]
                  lblto18['text'] = lst4400[7][0]
                  lblto19['text'] = lst4400[8][0]
                  lblto110['text'] = lst4400[9][0]
                  lblto111['text'] = lst4400[10][0]
                  
            else:
                    
                     messagebox.showerror(title = 'Error' , message = 'مشخصات نادرست میباشد')          
            if len (name_ath1) != 0:
                  lbltox11['text'] = name_ath1
                  lblonvan11['text'] = onvan_ath1
                  lbltozi11['text'] = tozi_ath1 





def func1():
    if win4.state()=='normal':
        win4.state('withdrawn')
    else:
        win4.state('normal')
        win4.lift(win)

def func2():
    if win5.state()=='normal':
        win5.state('withdrawn')
    else:
        win5.state('normal')
        win5.lift()

def func3():
    if win6.state()=='normal':
        win6.state('withdrawn')
    else:
        win6.state('normal')
        win6.lift()
def func4():
    if win7.state()=='normal':
        win7.state('withdrawn')
    else:
        win7.state('normal')
        win7.lift()        

def func5():
    if win8.state()=='normal':
        win8.state('withdrawn')
    else:
        win8.state('normal')
        win8.lift()        

def func6():
    if win9.state()=='normal':
        win9.state('withdrawn')
    else:
        win9.state('normal')
        win9.lift()        

def func7():
    if win11.state()=='normal':
        win11.state('withdrawn')
    else:
        win11.state('normal')
        win11.lift()        

def func10():
    if win3.state()=='normal':
        win3.state('withdrawn')
    else:
        win3.state('normal')
        win3.lift()        
def func12():
    if win12.state()=='normal':
        win12.state('withdrawn')
    else:
        win12.state('normal')
        win12.lift()    

def func11():
    if win13.state()=='normal':
        win13.state('withdrawn')
    else:
        win13.state('normal')
        win13.lift()    


def fish2(event = None):
    win4.state('normal')
    win4.lift(win2)
    win.state('withdrawn')

    lst1 = []
    row = cur.execute('SELECT shenase , harekat , azole_hadaf , gp_tamrini FROM harekata')
    for i in row :
         lst1.append(i)
            
   
    global sheet1                  
    sheet1 = Sheet(frm__1 , data = [[f'{j}' for j in i] for i in lst1] , auto_resize_columns=TRUE,
                                width=width, height=700, total_columns=5, total_rows=20 ,
                                show_x_scrollbar=True, show_y_scrollbar=True ,column_width=200,
                                headers = ['شناسه',' حرکت',' عضله هدف','گروه تمرینی'] ,
                                header_bg = 'lightskyblue2' , header_border_fg = 'black' , header_grid_fg = 'gray50' ,
                                table_bg = 'azure' , index_bg = 'lightskyblue2',index_fg='black',header_fg = 'black' , index_grid_fg = 'gray50' )
        
    sheet1.place(x=0 , y=0)
        
    
    sheet1.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                         'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                         'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                         'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                         'rc_delete_row','copy','cut','paste','delete','undo','edit_cell'))




def new(event = None):
    win5.state('normal')
    win5.lift()
    win.state('withdrawn')
    combo1000.focus()
    combo1000.bind('<Return>',lambda event : ent___2.focus())
    ent___2.bind('<Return>',lambda event : ent___3.focus())


def fish3():
    win12.state('normal')
    win12.lift()
    win.state('withdrawn')   
  

def fish():
    win6.state('normal')
    win6.lift(win2)
    win.state('withdrawn')

    lst2 = []
    row = cur.execute('SELECT athlee_code , athlee_name , athlee_age , athlee_number  FROM athlee')
    for i in row :
            lst2.append(i)
            
    global sheet2                   
    sheet2 = Sheet(frm____1 , data = [[f'{j}' for j in i] for i in lst2] , auto_resize_columns=TRUE,
                                width=width, height=700, total_columns=5, total_rows=200 , 
                                show_x_scrollbar=True, show_y_scrollbar=True ,column_width=200,
                                headers = ['کدملی' , 'نام' ,  'تاریخ تولد' ,'شماره موبایل'] ,
                                header_bg = 'lightskyblue2' , header_border_fg = 'black' , header_grid_fg = 'gray50' ,
                                table_bg = 'azure' , index_bg = 'lightskyblue2',index_fg='black',header_fg = 'black' , index_grid_fg = 'gray50',
                                )
        
    sheet2.place(x=0 , y=0)
        
            
    sheet2.enable_bindings(('single_select',
                              'copy','cut'))
    sheet2.bind("<Double-Button-1>" , double_click)


def double_click(event):
        
        row1     = sheet2.identify_row(event, exclude_index = False, allow_end = True)
        column1  = sheet2.identify_column(event, exclude_header = False, allow_end = True) 
          
        sheet2.cell_selected(row1,column1) 
        global ro
        ro = sheet2.get_cell_data(row1,column1)
        if len(ro) != 0:


            rowro = '''SELECT * FROM athlee WHERE athlee_code = {} '''.format(ro)
            rfro = cur.execute(rowro)
            global lstro
            lstro = list(rfro)

            
            win11.state('normal')
            win11.lift()
            if len(lstro)!=0 :
                  
                  lbl01['text'] = lstro[0][0]
                  lbl02['text'] = lstro[0][1]
                  lbl03['text'] = lstro[0][2]
                  lbl04['text'] = lstro[0][3]
                  lbl05['text'] = lstro[0][4]
                  lbl06['text'] = lstro[0][5]
                  lbl07['text'] = lstro[0][6]
                  lbl08['text'] = lstro[0][7]
                  lbl09['text'] = lstro[0][8]
                  lbl010['text'] = lstro[0][9]
                  lbl011['text'] = lstro[0][10]

            else:
                    
                     messagebox.showerror(title = 'Error' , message = 'مشخصات نادرست میباشد')
        else:
            messagebox.showerror(title = 'Error' , message = 'مشخصات نادرست میباشد')



                  



def record2():
        
        athlee_name  = ent_____1.get()
    
        athlee_age  = ent_____3.get()
        athlee_wheight  = ent_____4.get()
        athlee_height  = ent_____5.get()
        athlee_code = ent_____6.get()
        athlee_surgery = ent_____12.get()
        athlee_blood = ent_____10.get()
        athlee_type = ent_____11.get()
        athlee_number = ent_____7.get()
        athlee_reshte = ent_____9.get()
        athlee_new_wheight = ent_____8.get()

        
        
        if len(athlee_code)!=0 and len(athlee_height)!=0  and len(athlee_wheight)!=0 and len( athlee_age)!=0 and len(athlee_name)!=0 and len(athlee_number)!=0 and len(athlee_new_wheight)!=0 and len(athlee_reshte)!=0 and len(athlee_blood)!=0 and len(athlee_type)!=0 and len(athlee_surgery)!=0:
            data1 = [athlee_code , athlee_name  , athlee_age ,athlee_height,athlee_wheight , athlee_surgery , athlee_blood , athlee_type , athlee_number , athlee_reshte , athlee_new_wheight]
            con = sql.connect('mydb.db')
            cur = con.cursor()
            command4 = 'INSERT INTO athlee (athlee_code , athlee_name  , athlee_age , athlee_height , athlee_wheight , athlee_surgery , athlee_blood , athlee_type , athlee_number , athlee_reshte , athlee_new_wheight) VALUES (?,?,?,?,?,?,?,?,?,?,?)'
            cur.execute(command4 , data1)
            con.commit()
            
        else:
            messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')


def record1():
        

        for i in range(1):
             number = random.randint(0,999999)
             
             
        
        gp_tamrini  = combo1000.get()
        azole_hadaf  = ent___2.get()
        harekat  = ent___3.get()
        shenase  = number


                                     
         
        if len(gp_tamrini)!=0 and len(azole_hadaf)!=0 and len(harekat)!=0:


            data1 = [shenase , gp_tamrini , azole_hadaf , harekat]
            con = sql.connect('mydb.db')
            cur = con.cursor()

            command2 = 'INSERT INTO harekata (shenase , gp_tamrini , azole_hadaf ,harekat) VALUES (?,?,?,?)'
            cur.execute(command2 , data1)
            con.commit()
            win5.state('withdrawn')
        else:
            messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')


def new2():
    win7.state('normal')
    win7.lift(win6)
    win.state('withdrawn')

    ent_____1.focus()
    ent_____1.bind('<Return>',lambda event : ent_____3.focus())
    ent_____3.bind('<Return>',lambda event : ent_____4.focus())
    ent_____4.bind('<Return>',lambda event : ent_____5.focus())
    ent_____5.bind('<Return>',lambda event : ent_____6.focus())
    ent_____6.bind('<Return>',lambda event : ent_____7.focus())
    ent_____7.bind('<Return>',lambda event : ent_____8.focus())
    ent_____8.bind('<Return>',lambda event : ent_____9.focus())
    ent_____9.bind('<Return>',lambda event : ent_____10.focus())
    ent_____10.bind('<Return>',lambda event : ent_____11.focus())
    ent_____11.bind('<Return>',lambda event : ent_____12.focus())
    ent_____12.bind('<Return>',lambda event : btn_____1.focus())


def takeScreenshot ():

    for i in range(1):
             number1 = random.randint(1,99999)


    today = jdatetime.date.today()
    f_d = today.strftime('%Y-%m-%d')

    lst99=[]
    row99 = cur.execute('SELECT b_name FROM barname1')
    for i in row99 :
            lst99.append(i)

    lst999=[]
    for i in lst99:
         lst999.extend(i) 
    
    str1 = ','.join(lst999)

    lstse=[]
    rowse = cur.execute('SELECT sett FROM barname1')
    for i in rowse :
            lstse.append(i)
    lstse999=[]
    for i in lstse:
         lstse999.extend(i) 
    
    strse = ','.join(lstse999)

    lstte=[]
    rowte = cur.execute('SELECT tekrar FROM barname1')
    for i in rowte :
            lstte.append(i)

    lstte999=[]
    for i in lstte:
         lstte999.extend(i) 
    
    strte = ','.join(lstte999)

    lstto=[]
    rowto = cur.execute('SELECT tozih FROM barname1')
    for i in rowto :
            lstto.append(i)

    lstto999=[]
    for i in lstto:
         lstto999.extend(i) 
    
    strto = ','.join(lstto999)

    lstre=[]
    rowre = cur.execute('SELECT rest FROM barname1')
    for i in rowre :
            lstre.append(i)

    lstre999=[]
    for i in lstre:
         lstre999.extend(i) 
    
    strre = ','.join(lstto999)

    data99 = [f_d,str1,name_ath1,ro,onvan_ath1,strse,strte,strto,number1,strre]
    command99 = 'INSERT INTO barname_personal (person_date,harekat_name,person_name ,person_number,onvan,person_set,person_tekrar,person_tozi,person_shenase,person_rest ) VALUES (?,?,?,?,?,?,?,?,?,?)'
    cur.execute(command99 , data99)
    con.commit()
    


    myScreenshot = pyautogui.screenshot()
    filename= f'{name_ath1}-{f_d}.pdf'
    # myScreenshot.save (filename)

    myScreenshot.save ('sc.png')
    pdf = FPDF()
    pdf.add_page()
    pdf.image('sc.png',x= 5,y=5,w=180)
    pdf.output(filename)






def exit ():
    if messagebox.askyesno("؟","آيا از خروج اطمينان داريد؟") >0 :
            
         win.destroy()
         return
            

def back():
    win3.state('withdrawn')
    win2.lift(win3)
    win.state('withdrawn')

def back2():
    win8.state('withdrawn')
    win2.state('normal')
    win2.lift()  
    win.state('withdrawn')  

def back3():
    win6.state('withdrawn')
    win.state('withdrawn')
  
def back4():
    win7.state('withdrawn')
    win6.state('normal')
    win.state('withdrawn')

def back5():
    win4.state('withdrawn')
    win.state('withdrawn')


def back6():
    win5.state('withdrawn')
    win4.state('normal')
    win.state('withdrawn')

def delete():
    win9.state('normal')
    win9.lift() 
    ent1111.focus()   
    win.state('withdrawn')

def delete_finally():
    delx = ent1111.get()
    command = ''' DELETE FROM harekata WHERE shenase="{}" ''' .format(delx)
    cur.execute(command) 
    con.commit()
    win9.state('withdrawn')



def delete_finally_athlee():
    del0x = ent01111.get()
    command = ''' DELETE FROM athlee WHERE athlee_code="{}" ''' .format(del0x)
    cur.execute(command) 
    con.commit()
    win12.state('withdrawn')

def serchhh():
    win10.state('normal')
    win10.lift()
    win.state('withdrawn')

def final_serch():

    shomare = ent11111.get()


    if len(shomare)!=0  :
              con = sql.connect('mydb.db')
              cur = con.cursor()

              row11 = '''SELECT * FROM athlee WHERE athlee_number = {} '''.format(shomare)
              rf = cur.execute(row11)
              global lst11
              lst11 = list(rf)

              if len(lst11)!=0 :
                  
                  win10.state('withdrawn')
                  win11.state('normal')
                  win11.lift()

                  lbl01['text'] = lst11[0][0]
                  lbl02['text'] = lst11[0][1]
                  lbl03['text'] = lst11[0][2]
                  lbl04['text'] = lst11[0][3]
                  lbl05['text'] = lst11[0][4]
                  lbl06['text'] = lst11[0][5]
                  lbl07['text'] = lst11[0][6]
                  lbl08['text'] = lst11[0][7]
                  lbl09['text'] = lst11[0][8]
                  lbl010['text'] = lst11[0][9]
                  lbl011['text'] = lst11[0][10]

              else:
                    
                     messagebox.showerror(title = 'Error' , message = 'مشخصات نادرست میباشد')

                       
              
                     
    else:
         messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')




def create(event = None):
    
    win11.state('withdrawn')
    win6.state('withdrawn')
    win8.state('normal')
    win.state('withdrawn')
    win8.lift()
    combo22.focus()
    combo22.bind('<Return>',lambda event : btn113.focus())
    btn113.bind('<Return>',nextt)
 


def nextt(event = None):
     
     ch = combo22.get()
     
     global combo33,combo44,combo55,combo55x,combo55z

     
     if ch == 'فانکشنال':
          lst5 = []
          row5 = cur.execute('SELECT  azole_hadaf  FROM harekata  WHERE gp_tamrini = "{}"'.format(ch))

          for i in row5 :
               lst5.append(i)
               
          

               combo33 = ttk.Combobox(frm111,width=25,values = lst5)
               combo33.set('لطفا انتخاب کنيد')
               combo33.place(x=1350,y=200)
               btn114=Button(frm111,width=10,text=' بعدی',bd=2,padx=5,pady=0,command=nextt2)
               btn114.place(x=1400,y=250)

               combo33.focus()
               combo33.bind('<Return>',lambda event : btn114.focus())
               btn114.bind('<Return>',nextt2)

          
          

     elif ch  =='پایین تنه':
          ch1 =  'پایین تنه'            
          lst6 = []
          row6 = cur.execute('SELECT  azole_hadaf  FROM harekata  WHERE gp_tamrini = "{}"'.format(ch1))

          for i in row6 :
               lst6.append(i)
               

               
               combo44 = ttk.Combobox(frm111,width=25,values = lst6)
               combo44.set('لطفا انتخاب کنيد')
               combo44.place(x=1350,y=200)
               btn115=Button(frm111,width=10,text=' تایید',bd=2,padx=5,pady=0,command=nextt3)
               btn115.place(x=1400,y=250) 

               combo44.focus()
               combo44.bind('<Return>',lambda event : btn115.focus())
               btn115.bind('<Return>',nextt3)
         

     elif ch  == 'بالا تنه' :
          ch2 =  'بالا تنه'
          lst7=[]
          row7 = cur.execute('SELECT  azole_hadaf  FROM harekata  WHERE gp_tamrini = "{}"'.format(ch2))

          for i in row7 :
               lst7.append(i)

               
               combo55 = ttk.Combobox(frm111,width=25,values = lst7)
               combo55.set('لطفا انتخاب کنيد')
               combo55.place(x=1350,y=200) 
               btn116=Button(frm111,width=10,text=' تایید',bd=2,padx=5,pady=0,command=nextt4)
               btn116.place(x=1400,y=250)

               combo55.focus()
               combo55.bind('<Return>',lambda event : btn116.focus())
               btn116.bind('<Return>',nextt4)


     elif ch  == 'میان تنه' :
          ch2x =  'میان تنه'
          lst7x=[]
          row7x = cur.execute('SELECT  azole_hadaf  FROM harekata  WHERE gp_tamrini = "{}"'.format(ch2x))

          for i in row7x :
               lst7x.append(i)

               
               combo55x = ttk.Combobox(frm111,width=25,values = lst7x)
               combo55x.set('لطفا انتخاب کنيد')
               combo55x.place(x=1350,y=200) 
               btn116x=Button(frm111,width=10,text=' تایید',bd=2,padx=5,pady=0,command=nextt4x)
               btn116x.place(x=1400,y=250)

               combo55x.focus()
               combo55x.bind('<Return>',lambda event : btn116x.focus())
               btn116x.bind('<Return>',nextt4x)


     elif ch  == 'عضلات کور' :
          ch2z =  'عضلات کور'
          lst7z=[]
          row7z = cur.execute('SELECT  azole_hadaf  FROM harekata  WHERE gp_tamrini = "{}"'.format(ch2z))

          for i in row7z :
               lst7z.append(i)

               
               combo55z = ttk.Combobox(frm111,width=25,values = lst7z)
               combo55z.set('لطفا انتخاب کنيد')
               combo55z.place(x=1350,y=200) 
               btn116z=Button(frm111,width=10,text=' تایید',bd=2,padx=5,pady=0,command=nextt4z)
               btn116z.place(x=1400,y=250)

               combo55z.focus()
               combo55z.bind('<Return>',lambda event : btn116z.focus())
               btn116z.bind('<Return>',nextt4z)


     else:
         win8.state('withdrawn')



def nextt2(event = None):
             
          nh =  combo33.get() 
          global combo66

          
          if nh  != 0 :
                  lst55 = []
                  row55 = cur.execute('SELECT  harekat  FROM harekata  WHERE azole_hadaf = "{}"'.format(nh))

                  for i in row55 :
                      lst55.append(i)
                      
                      combo66 = ttk.Combobox(frm111,width=25,values = lst55,foreground='black')
                      combo66.set('لطفا انتخاب کنيد')
                      combo66.place(x=1350,y=320)
                      btn117=Button(frm111,width=10,text=' تایید',bd=2,padx=5,pady=0,command=saz3)
                      btn117.place(x=900,y=270)     

                      combo66.focus()
                      combo66.bind('<Return>',lambda event : ent1101.focus())
                      ent1101.bind('<Return>',lambda event : ent1102.focus())
                      ent1102.bind('<Return>',lambda event : ent1103.focus())
                      ent1103.bind('<Return>',lambda event : btn117.focus())
                      btn117.bind('<Return>',saz3)  
                





def nextt3(event = None):
     sh =  combo44.get()
     global combo444
     
     
     if sh  != 0 :
           
                     lst444 = []
                     row444 = cur.execute('SELECT  harekat  FROM harekata  WHERE azole_hadaf = "{}"'.format(sh))

                     for i in row444 :
                         lst444.append(i)

                         
                         combo444 = ttk.Combobox(frm111,width=25,values = lst444,foreground='black')
                         combo444.set('لطفا انتخاب کنيد')
                         combo444.place(x=1350,y=320)
                         btn118=Button(frm111,width=10,text=' بعدی',bd=2,padx=5,pady=0,command=saz2)
                         btn118.place(x=900,y=270)

                         combo444.focus()
                         combo444.bind('<Return>',lambda event : ent1101.focus())
                         ent1101.bind('<Return>',lambda event : ent1102.focus())
                         ent1102.bind('<Return>',lambda event : ent1103.focus())
                         ent1103.bind('<Return>',lambda event : btn118.focus())
                         btn118.bind('<Return>',saz2)  
                         

def nextt4(event = None):
     mh =  combo55.get()
     global combo555

     if mh  != 0 :
           
                     lst555 = []
                     row555 = cur.execute('SELECT  harekat  FROM harekata  WHERE azole_hadaf = "{}"'.format(mh))

                     for i in row555 :
                         lst555.append(i)

                         
                         combo555 = ttk.Combobox(frm111,width=25,values = lst555,foreground='black')
                         combo555.set('لطفا انتخاب کنيد')
                         combo555.place(x=1350,y=320)  
                         btn119=Button(frm111,width=10,text=' بعدی',bd=2,padx=5,pady=0,command=saz)
                         btn119.place(x=900,y=270)   

                         combo555.focus()
                         combo555.bind('<Return>',lambda event : ent1101.focus())
                         ent1101.bind('<Return>',lambda event : ent1102.focus())
                         ent1102.bind('<Return>',lambda event : ent1103.focus())
                         ent1103.bind('<Return>',lambda event : btn119.focus())
                         btn119.bind('<Return>',saz)   

def nextt4x(event = None):
     mhx =  combo55x.get()
     global combo555x

     if mhx  != 0 :
           
                     lst555x = []
                     row555x = cur.execute('SELECT  harekat  FROM harekata  WHERE azole_hadaf = "{}"'.format(mhx))

                     for i in row555x :
                         lst555x.append(i)

                         
                         combo555x = ttk.Combobox(frm111,width=25,values = lst555x,foreground='black')
                         combo555x.set('لطفا انتخاب کنيد')
                         combo555x.place(x=1350,y=320)  
                         btn119x=Button(frm111,width=10,text=' بعدی',bd=2,padx=5,pady=0,command=sazx)
                         btn119x.place(x=900,y=270)   

                         combo555x.focus()
                         combo555x.bind('<Return>',lambda event : ent1101.focus())
                         ent1101.bind('<Return>',lambda event : ent1102.focus())
                         ent1102.bind('<Return>',lambda event : ent1103.focus())
                         ent1103.bind('<Return>',lambda event : btn119x.focus())
                         btn119x.bind('<Return>',sazx)                            


def nextt4z(event = None):
     mhz =  combo55z.get()
     global combo555z

     if mhz  != 0 :
           
                     lst555z = []
                     row555z = cur.execute('SELECT  harekat  FROM harekata  WHERE azole_hadaf = "{}"'.format(mhz))

                     for i in row555z :
                         lst555z.append(i)

                         
                         combo555z = ttk.Combobox(frm111,width=25,values = lst555z,foreground='black')
                         combo555z.set('لطفا انتخاب کنيد')
                         combo555z.place(x=1350,y=320)  
                         btn119z=Button(frm111,width=10,text=' بعدی',bd=2,padx=5,pady=0,command=sazz)
                         btn119z.place(x=900,y=270)   

                         combo555z.focus()
                         combo555z.bind('<Return>',lambda event : ent1101.focus())
                         ent1101.bind('<Return>',lambda event : ent1102.focus())
                         ent1102.bind('<Return>',lambda event : ent1103.focus())
                         ent1103.bind('<Return>',lambda event : btn119z.focus())
                         btn119z.bind('<Return>',sazz)   

def saz(event = None):
     
     harekat_asli = combo555.get()
     azhadaf = combo55.get() 
     gp = combo22.get()
     rest = ent1101.get()
     tekrar = ent1102.get()
     tozih = ent1103.get()
     set1 = ent1104.get()
     onvan = ent1105.get()
     tozih_bar = ent1106.get()



     if len(harekat_asli)!=0 and len(azhadaf)!=0 and len(gp)!=0:


            data00 = [harekat_asli , azhadaf , gp, tekrar, rest, tozih,set1,onvan,tozih_bar]
            con = sql.connect('mydb.db')
            cur = con.cursor()

            command2 =  'INSERT INTO barname1 (b_name , b_azole_hadaf, b_gp_tamrini ,tekrar,rest,tozih,sett,onvan,tozih_bar ) VALUES (?,?,?,?,?,?,?,?,?)'
            cur.execute(command2 , data00)
            con.commit()
            ent1101.delete(0,END)
            ent1102.delete(0,END)
            ent1103.delete(0,END)
            ent1104.delete(0,END)
            combo22.delete(0,END)
            combo55.delete(0,END)
            combo555.delete(0,END) 

     else:
            messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')

def sazz(event = None):
     
     harekat_asliz = combo555z.get()
     azhadafz = combo55z.get() 
     gpz = combo22.get()
     restz = ent1101.get()
     tekrarz = ent1102.get()
     tozihz = ent1103.get()
     set1z = ent1104.get()
     onvanz = ent1105.get()
     tozih_barz = ent1106.get()



     if len(harekat_asliz)!=0 and len(azhadafz)!=0 and len(gpz)!=0:


            data00z = [harekat_asliz , azhadafz , gpz, tekrarz, restz, tozihz,set1z,onvanz,tozih_barz]
            con = sql.connect('mydb.db')
            cur = con.cursor()

            command2z =  'INSERT INTO barname1 (b_name , b_azole_hadaf, b_gp_tamrini ,tekrar,rest,tozih,sett,onvan,tozih_bar ) VALUES (?,?,?,?,?,?,?,?,?)'
            cur.execute(command2z , data00z)
            con.commit()
            ent1101.delete(0,END)
            ent1102.delete(0,END)
            ent1103.delete(0,END)
            ent1104.delete(0,END)
            combo22.delete(0,END)
            combo55z.delete(0,END)
            combo555z.delete(0,END) 

     else:
            messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')



def sazx(event = None):
     
     harekat_aslix = combo555x.get()
     azhadafx = combo55x.get() 
     gpx = combo22.get()
     restx = ent1101.get()
     tekrarx = ent1102.get()
     tozihx = ent1103.get()
     set1x = ent1104.get()
     onvanx = ent1105.get()
     tozih_barx = ent1106.get()



     if len(harekat_aslix)!=0 and len(azhadafx)!=0 and len(gpx)!=0:


            data00x = [harekat_aslix , azhadafx , gpx, tekrarx, restx, tozihx,set1x,onvanx,tozih_barx]
            con = sql.connect('mydb.db')
            cur = con.cursor()

            command2x =  'INSERT INTO barname1 (b_name , b_azole_hadaf, b_gp_tamrini ,tekrar,rest,tozih,sett,onvan,tozih_bar ) VALUES (?,?,?,?,?,?,?,?,?)'
            cur.execute(command2x , data00x)
            con.commit()
            ent1101.delete(0,END)
            ent1102.delete(0,END)
            ent1103.delete(0,END)
            ent1104.delete(0,END)
            combo22.delete(0,END)
            combo55x.delete(0,END)
            combo555x.delete(0,END) 

     else:
            messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')

def saz2(event = None):
     
     harekat_asli2 = combo444.get()
     azhadaf2 = combo44.get() 
     gp2 = combo22.get()
     rest1 = ent1101.get()
     tekrar1 = ent1102.get()
     tozih1 = ent1103.get()
     set2 = ent1104.get()
     onvan1 = ent1105.get()
     tozih_bar1 = ent1106.get()


     if len(harekat_asli2)!=0 and len(azhadaf2)!=0 and len(gp2)!=0:


            data00 = [harekat_asli2 , azhadaf2 , gp2, tekrar1, rest1, tozih1,set2,onvan1,tozih_bar1]
            con = sql.connect('mydb.db')
            cur = con.cursor()

            command2 = 'INSERT INTO barname1 (b_name , b_azole_hadaf, b_gp_tamrini ,tekrar,rest,tozih,sett,onvan,tozih_bar ) VALUES (?,?,?,?,?,?,?,?,?)'
            cur.execute(command2 , data00)
            con.commit()
            ent1101.delete(0,END)
            ent1102.delete(0,END)
            ent1103.delete(0,END)
            ent1104.delete(0,END)
            combo22.delete(0,END)
            combo44.delete(0,END)
            combo444.delete(0,END) 

     else:
            messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')


                      
def saz3(event = None):
     
     harekat_asli3 = combo66.get()
     azhadaf3 = combo33.get() 
     gp3 = combo22.get()
     rest2 = ent1101.get()
     tekrar2 = ent1102.get()
     tozih2 = ent1103.get()
     set3 = ent1104.get()
     onvan2 = ent1105.get()
     tozih_bar2 = ent1106.get()


     if len(harekat_asli3)!=0 and len(azhadaf3)!=0 and len(gp3)!=0:


            data00 = [harekat_asli3 , azhadaf3 , gp3, tekrar2, rest2, tozih2,set3,onvan2,tozih_bar2]
            con = sql.connect('mydb.db')
            cur = con.cursor()

            command2 =  'INSERT INTO barname1 (b_name , b_azole_hadaf, b_gp_tamrini ,tekrar,rest,tozih,sett,onvan,tozih_bar ) VALUES (?,?,?,?,?,?,?,?,?)'
            cur.execute(command2 , data00)
            con.commit()
            ent1101.delete(0,END)
            ent1102.delete(0,END)
            ent1103.delete(0,END)
            ent1104.delete(0,END)
            combo22.delete(0,END)
            combo33.delete(0,END)
            combo66.delete(0,END)            
            
     else:
            messagebox.showerror(title = 'Error' , message = 'لطفا مشخصات را کامل کنيد ')


                      

def listmaker():
        
        lst101=[]
        row101 = cur.execute('SELECT b_name , tekrar , sett ,tozih , rest   FROM barname1')
        for i in row101 :
               lst101.append(i)
        
        global sheet00
        sheet00 = Sheet(frm111 , data = [[f'{j}' for j in i] for i in lst101] ,#auto_resize_columns =TRUE,
                                width=550, height=900, total_columns=5, cell_auto_resize_enabled=TRUE, 
                                show_x_scrollbar=True, show_y_scrollbar=True ,column_width=100,
                                headers = ['حرکت' , 'تکرار ' ,  'ست  ',"توضیحات ", 'استراحت'] ,
                                header_bg = 'lightskyblue2' , header_border_fg = 'black' , header_grid_fg = 'gray50' ,
                                table_bg = 'azure' , index_bg = 'lightskyblue2',index_fg='black',header_fg = 'black' , index_grid_fg = 'gray50',
                                )
        
        sheet00.place(x=0 , y=0)
        sheet00.enable_bindings(('single_select',
                              'copy','cut'))
        sheet00.bind("<Double-Button-1>" , double_click2)



def double_click2(event):

        row00   = sheet00.identify_row(event, exclude_index = False, allow_end = True)
        column00  = sheet00.identify_column(event, exclude_header = False, allow_end = True) 
          
        sheet00.cell_selected(row00,column00) 
        global ro00
        ro00 = sheet00.get_cell_data(row00,column00)

        if len(ro00) != 0:

            if messagebox.askyesno("؟","آيا از حذف این رکورد اطمينان داريد؟") >0 :
 
                command00 = ''' DELETE FROM barname1 WHERE b_name="{}" ''' .format(ro00)
                cur.execute(command00) 
                con.commit()
        else:

             message_error = messagebox.showerror('Error','')


def listcleaner():

    command00 = ''' DELETE FROM barname1 '''
    cur.execute(command00) 
    con.commit()     

def old():
     
        lst33=[]
        row33 = cur.execute('SELECT person_shenase,person_date,onvan,person_name FROM barname_personal WHERE person_number = "{}"'.format(ro))
        for i in row33 :
               lst33.append(i)
        
      

        global sheet33
        sheet33 = Sheet(frm01 , data = [[f'{j}' for j in i] for i in lst33] ,#auto_resize_columns =TRUE,
                                width=1350, height=790, total_columns=6, cell_auto_resize_enabled=TRUE, 
                                show_x_scrollbar=True, show_y_scrollbar=True ,column_width=380,
                                headers = ['شناسه','تاریخ', 'عنوان','نام'] ,
                                header_bg = 'lightskyblue2' , header_border_fg = 'black' , header_grid_fg = 'gray50' ,
                                table_bg = 'azure' , index_bg = 'lightskyblue2',index_fg='black',header_fg = 'black' , index_grid_fg = 'gray50',
                                )
       
        sheet33.place(x=500 , y=0) 
        sheet33.enable_bindings(('single','drag_select','column_drag_and_drop','row_drag_and_drop','column_select',
                                         'row_select','column_width_resize','double_click_column_resize','row_width_resize',
                                         'column_height_resize','arrowkeys','row_height_resize','double_click_row_resize',
                                         'right_click_popup_menu','rc_insert_column','rc_delete_column','rc_insert_row',
                                         'rc_delete_row','copy'))    
        sheet33.bind("<Double-Button-1>" , double_click3)

def double_click3(event):
        
        row03     = sheet33.identify_row(event, exclude_index = False, allow_end = True)
        column03  = sheet33.identify_column(event, exclude_header = False, allow_end = True) 
          
        sheet33.cell_selected(row03,column03) 
        global ro03
        ro03 = sheet33.get_cell_data(row03,column03)


        if len(ro03) != 0:

            win13.state('normal')
            win13.lift()

            row03ro = '''SELECT harekat_name FROM barname_personal WHERE person_shenase = {} '''.format(ro03)
            rf03ro = cur.execute(row03ro)
            lst03ro = list(rf03ro)        
            n = [item for tuple in lst03ro for item in tuple]
            str_to = n[0]
            god_arvin = str_to.split(',')


            row04ro = '''SELECT person_tekrar FROM barname_personal WHERE person_shenase = {} '''.format(ro03)
            rf04ro = cur.execute(row04ro)
            lst04ro = list(rf04ro)        
            n4 = [item for tuple in lst04ro for item in tuple]
            str_to4 = n4[0]
            god_arvin4 = str_to4.split(',')

            row05ro = '''SELECT person_rest FROM barname_personal WHERE person_shenase = {} '''.format(ro03)
            rf05ro = cur.execute(row05ro)
            lst05ro = list(rf05ro)        
            n5 = [item for tuple in lst05ro for item in tuple]
            str_to5 = n5[0]
            god_arvin5 = str_to5.split(',')

            row06ro = '''SELECT person_tozi FROM barname_personal WHERE person_shenase = {} '''.format(ro03)
            rf06ro = cur.execute(row06ro)
            lst06ro = list(rf06ro)        
            n6 = [item for tuple in lst06ro for item in tuple]
            str_to6 = n6[0]
            god_arvin6 = str_to6.split(',')

            row07ro = '''SELECT person_set FROM barname_personal WHERE person_shenase = {} '''.format(ro03)
            rf07ro = cur.execute(row07ro)
            lst07ro = list(rf07ro)        
            n7 = [item for tuple in lst07ro for item in tuple]
            str_to7 = n7[0]
            god_arvin7 = str_to7.split(',')

            row08ro = '''SELECT person_name FROM barname_personal WHERE person_shenase = {} '''.format(ro03)
            rf08ro = cur.execute(row08ro)
            lst08ro = list(rf08ro)    

            row09ro = '''SELECT onvan FROM barname_personal WHERE person_shenase = {} '''.format(ro03)
            rf09ro = cur.execute(row09ro)
            lst09ro = list(rf09ro)    

            lbl_tox11['text'] = lst08ro
            lbl_onvan11['text'] = lst09ro  
            
                
            if len(god_arvin) == 6 :
                

                  lbl_11['text'] = god_arvin[0]
                  lbl_12['text'] = god_arvin[1]
                  lbl_13['text'] = god_arvin[2]
                  lbl_14['text'] = god_arvin[3]
                  lbl_15['text'] = god_arvin[4]
                  lbl_16['text'] = god_arvin[5]

                #   lbl_17['text'] = lst1100[6]
                #   lbl_18['text'] = lst1100[7]
                #   lbl_19['text'] = lst1100[8]
                #   lbl_110['text'] = lst1100[9]
                #   lbl_111['text'] = lst1100[10]

                  lbl_t11['text'] = god_arvin4[0]
                  lbl_t12['text'] = god_arvin4[1]
                  lbl_t13['text'] = god_arvin4[2]
                  lbl_t14['text'] = god_arvin4[3]
                  lbl_t15['text'] = god_arvin4[4]
                  lbl_t16['text'] = god_arvin4[5]
                #   lbl_t17['text'] = god_arvin4[6]
                #   lbl_t18['text'] = god_arvin4[7]
                #   lbl_t19['text'] = god_arvin4[8]
                #   lbl_t110['text'] = god_arvin4[9]
                #   lbl_t111['text'] = god_arvin4[10]

                  lbl_r11['text'] = god_arvin5[0]
                  lbl_r12['text'] = god_arvin5[1]
                  lbl_r13['text'] = god_arvin5[2]
                  lbl_r14['text'] = god_arvin5[3]
                  lbl_r15['text'] = god_arvin5[4]
                  lbl_r16['text'] = god_arvin5[5]
                #   lbl_r17['text'] = god_arvin5[6]
                #   lbl_r18['text'] = god_arvin5[7]
                #   lbl_r19['text'] = god_arvin5[8]
                #   lbl_r110['text'] = god_arvin5[9]
                #   lbl_r111['text'] = god_arvin5[10]

                  lbl_to11['text'] = god_arvin6[0]
                  lbl_to12['text'] = god_arvin6[1]
                  lbl_to13['text'] = god_arvin6[2]
                  lbl_to14['text'] = god_arvin6[3]
                  lbl_to15['text'] = god_arvin6[4]
                  lbl_to16['text'] = god_arvin6[5]
                #   lbl_to17['text'] = god_arvin6[6]
                #   lbl_to18['text'] = god_arvin6[7]
                #   lbl_to19['text'] = god_arvin6[8]
                #   lbl_to110['text'] = god_arvin6[9]
                #   lbl_to111['text'] = god_arvin6[10]

                  lbl_se11['text'] = god_arvin7[0]
                  lbl_se12['text'] = god_arvin7[1]
                  lbl_se13['text'] = god_arvin7[2]
                  lbl_se14['text'] = god_arvin7[3]
                  lbl_se15['text'] = god_arvin7[4]
                  lbl_se16['text'] = god_arvin7[5]
                #   lbl_se17['text'] = god_arvin7[6]
                #   lbl_se18['text'] = god_arvin7[7]
                #   lbl_se19['text'] = god_arvin7[8]
                #   lbl_se110['text'] = god_arvin7[9]
                #   lbl_se111['text'] = god_arvin7[10]      
         
            elif len(god_arvin) == 7 :
                 
                  lbl_11['text'] = god_arvin[0]
                  lbl_12['text'] = god_arvin[1]
                  lbl_13['text'] = god_arvin[2]
                  lbl_14['text'] = god_arvin[3]
                  lbl_15['text'] = god_arvin[4]
                  lbl_16['text'] = god_arvin[5]
                  lbl_17['text'] = god_arvin[6]
                #   lbl_18['text'] = god_arvin[7]
                #   lbl_19['text'] = god_arvin[8]
                #   lbl_110['text'] = god_arvin[9]
                #   lbl_111['text'] = god_arvin[10]

                  lbl_t11['text'] = god_arvin4[0]
                  lbl_t12['text'] = god_arvin4[1]
                  lbl_t13['text'] = god_arvin4[2]
                  lbl_t14['text'] = god_arvin4[3]
                  lbl_t15['text'] = god_arvin4[4]
                  lbl_t16['text'] = god_arvin4[5]
                  lbl_t17['text'] = god_arvin4[6]
                #   lbl_t18['text'] = god_arvin4[7]
                #   lbl_t19['text'] = god_arvin4[8]
                #   lbl_t110['text'] = god_arvin4[9]
                #   lbl_t111['text'] = god_arvin4[10]

                  lbl_r11['text'] = god_arvin5[0]
                  lbl_r12['text'] = god_arvin5[1]
                  lbl_r13['text'] = god_arvin5[2]
                  lbl_r14['text'] = god_arvin5[3]
                  lbl_r15['text'] = god_arvin5[4]
                  lbl_r16['text'] = god_arvin5[5]
                  lbl_r17['text'] = god_arvin5[6]
                #   lbl_r18['text'] = god_arvin5[7]
                #   lbl_r19['text'] = god_arvin5[8]
                #   lbl_r110['text'] = god_arvin5[9]
                #   lbl_r111['text'] = god_arvin5[10]

                  lbl_to11['text'] = god_arvin6[0]
                  lbl_to12['text'] = god_arvin6[1]
                  lbl_to13['text'] = god_arvin6[2]
                  lbl_to14['text'] = god_arvin6[3]
                  lbl_to15['text'] = god_arvin6[4]
                  lbl_to16['text'] = god_arvin6[5]
                  lbl_to17['text'] = god_arvin6[6]
                #   lbl_to18['text'] = god_arvin6[7]
                #   lbl_to19['text'] = god_arvin6[8]
                #   lbl_to110['text'] = god_arvin6[9]
                #   lbl_to111['text'] = god_arvin6[10]

                  lbl_se11['text'] = god_arvin7[0]
                  lbl_se12['text'] = god_arvin7[1]
                  lbl_se13['text'] = god_arvin7[2]
                  lbl_se14['text'] = god_arvin7[3]
                  lbl_se15['text'] = god_arvin7[4]
                  lbl_se16['text'] = god_arvin7[5]
                  lbl_se17['text'] = god_arvin7[6]
                #   lbl_se18['text'] = god_arvin7[7]
                #   lbl_se19['text'] = god_arvin7[8]
                #   lbl_se110['text'] = god_arvin7[9]
                #   lbl_se111['text'] = god_arvin7[10]      
                         
            elif len(god_arvin) == 8 :
                 
                  lbl_11['text'] = god_arvin[0]
                  lbl_12['text'] = god_arvin[1]
                  lbl_13['text'] = god_arvin[2]
                  lbl_14['text'] = god_arvin[3]
                  lbl_15['text'] = god_arvin[4]
                  lbl_16['text'] = god_arvin[5]
                  lbl_17['text'] = god_arvin[6]
                  lbl_18['text'] = god_arvin[7]
                #   lbl_19['text'] = god_arvin[8]
                #   lbl_110['text'] = god_arvin[9]
                #   lbl_111['text'] = god_arvin[10]

                  lbl_t11['text'] = god_arvin4[0]
                  lbl_t12['text'] = god_arvin4[1]
                  lbl_t13['text'] = god_arvin4[2]
                  lbl_t14['text'] = god_arvin4[3]
                  lbl_t15['text'] = god_arvin4[4]
                  lbl_t16['text'] = god_arvin4[5]
                  lbl_t17['text'] = god_arvin4[6]
                  lbl_t18['text'] = god_arvin4[7]
                #   lbl_t19['text'] = god_arvin4[8]
                #   lbl_t110['text'] = god_arvin4[9]
                #   lbl_t111['text'] = god_arvin4[10]

                  lbl_r11['text'] = god_arvin5[0]
                  lbl_r12['text'] = god_arvin5[1]
                  lbl_r13['text'] = god_arvin5[2]
                  lbl_r14['text'] = god_arvin5[3]
                  lbl_r15['text'] = god_arvin5[4]
                  lbl_r16['text'] = god_arvin5[5]
                  lbl_r17['text'] = god_arvin5[6]
                  lbl_r18['text'] = god_arvin5[7]
                #   lbl_r19['text'] = god_arvin5[8]
                #   lbl_r110['text'] = god_arvin5[9]
                #   lbl_r111['text'] = god_arvin5[10]

                  lbl_to11['text'] = god_arvin6[0]
                  lbl_to12['text'] = god_arvin6[1]
                  lbl_to13['text'] = god_arvin6[2]
                  lbl_to14['text'] = god_arvin6[3]
                  lbl_to15['text'] = god_arvin6[4]
                  lbl_to16['text'] = god_arvin6[5]
                  lbl_to17['text'] = god_arvin6[6]
                  lbl_to18['text'] = god_arvin6[7]
                #   lbl_to19['text'] = god_arvin6[8]
                #   lbl_to110['text'] = god_arvin6[9]
                #   lbl_to111['text'] = god_arvin6[10]

                  lbl_se11['text'] = god_arvin7[0]
                  lbl_se12['text'] = god_arvin7[1]
                  lbl_se13['text'] = god_arvin7[2]
                  lbl_se14['text'] = god_arvin7[3]
                  lbl_se15['text'] = god_arvin7[4]
                  lbl_se16['text'] = god_arvin7[5]
                  lbl_se17['text'] = god_arvin7[6]
                  lbl_se18['text'] = god_arvin7[7]
                #   lbl_se19['text'] = god_arvin7[8]
                #   lbl_se110['text'] = god_arvin7[9]
                #   lbl_se111['text'] = god_arvin7[10]      
                         
            
            elif len(god_arvin) == 9 :
                 
                  lbl_11['text'] = god_arvin[0]
                  lbl_12['text'] = god_arvin[1]
                  lbl_13['text'] = god_arvin[2]
                  lbl_14['text'] = god_arvin[3]
                  lbl_15['text'] = god_arvin[4]
                  lbl_16['text'] = god_arvin[5]
                  lbl_17['text'] = god_arvin[6]
                  lbl_18['text'] = god_arvin[7]
                  lbl_19['text'] = god_arvin[8]
                #   lbl_110['text'] = god_arvin[9]
                #   lbl_111['text'] = god_arvin[10]

                  lbl_t11['text'] = god_arvin4[0]
                  lbl_t12['text'] = god_arvin4[1]
                  lbl_t13['text'] = god_arvin4[2]
                  lbl_t14['text'] = god_arvin4[3]
                  lbl_t15['text'] = god_arvin4[4]
                  lbl_t16['text'] = god_arvin4[5]
                  lbl_t17['text'] = god_arvin4[6]
                  lbl_t18['text'] = god_arvin4[7]
                  lbl_t19['text'] = god_arvin4[8]
                #   lbl_t110['text'] = god_arvin4[9]
                #   lbl_t111['text'] = god_arvin4[10]

                  lbl_r11['text'] = god_arvin5[0]
                  lbl_r12['text'] = god_arvin5[1]
                  lbl_r13['text'] = god_arvin5[2]
                  lbl_r14['text'] = god_arvin5[3]
                  lbl_r15['text'] = god_arvin5[4]
                  lbl_r16['text'] = god_arvin5[5]
                  lbl_r17['text'] = god_arvin5[6]
                  lbl_r18['text'] = god_arvin5[7]
                  lbl_r19['text'] = god_arvin5[8]
                #   lbl_r110['text'] = god_arvin5[9]
                #   lbl_r111['text'] = god_arvin5[10]

                  lbl_to11['text'] = god_arvin6[0]
                  lbl_to12['text'] = god_arvin6[1]
                  lbl_to13['text'] = god_arvin6[2]
                  lbl_to14['text'] = god_arvin6[3]
                  lbl_to15['text'] = god_arvin6[4]
                  lbl_to16['text'] = god_arvin6[5]
                  lbl_to17['text'] = god_arvin6[6]
                  lbl_to18['text'] = god_arvin6[7]
                  lbl_to19['text'] = god_arvin6[8]
                #   lbl_to110['text'] = god_arvin6[9]
                #   lbl_to111['text'] = god_arvin6[10]

                  lbl_se11['text'] = god_arvin7[0]
                  lbl_se12['text'] = god_arvin7[1]
                  lbl_se13['text'] = god_arvin7[2]
                  lbl_se14['text'] = god_arvin7[3]
                  lbl_se15['text'] = god_arvin7[4]
                  lbl_se16['text'] = god_arvin7[5]
                  lbl_se17['text'] = god_arvin7[6]
                  lbl_se18['text'] = god_arvin7[7]
                  lbl_se19['text'] = god_arvin7[8]
                #   lbl_se110['text'] = god_arvin7[9]
                #   lbl_se111['text'] = god_arvin7[10]      
                         
            elif len(god_arvin) == 10 :
                 
                  lbl_11['text'] = god_arvin[0]
                  lbl_12['text'] = god_arvin[1]
                  lbl_13['text'] = god_arvin[2]
                  lbl_14['text'] = god_arvin[3]
                  lbl_15['text'] = god_arvin[4]
                  lbl_16['text'] = god_arvin[5]
                  lbl_17['text'] = god_arvin[6]
                  lbl_18['text'] = god_arvin[7]
                  lbl_19['text'] = god_arvin[8]
                  lbl_110['text'] = god_arvin[9]
                #   lbl_111['text'] = god_arvin[10]

                  lbl_t11['text'] = god_arvin4[0]
                  lbl_t12['text'] = god_arvin4[1]
                  lbl_t13['text'] = god_arvin4[2]
                  lbl_t14['text'] = god_arvin4[3]
                  lbl_t15['text'] = god_arvin4[4]
                  lbl_t16['text'] = god_arvin4[5]
                  lbl_t17['text'] = god_arvin4[6]
                  lbl_t18['text'] = god_arvin4[7]
                  lbl_t19['text'] = god_arvin4[8]
                  lbl_t110['text'] = god_arvin4[9]
                #   lbl_t111['text'] = god_arvin4[10]

                  lbl_r11['text'] = god_arvin5[0]
                  lbl_r12['text'] = god_arvin5[1]
                  lbl_r13['text'] = god_arvin5[2]
                  lbl_r14['text'] = god_arvin5[3]
                  lbl_r15['text'] = god_arvin5[4]
                  lbl_r16['text'] = god_arvin5[5]
                  lbl_r17['text'] = god_arvin5[6]
                  lbl_r18['text'] = god_arvin5[7]
                  lbl_r19['text'] = god_arvin5[8]
                  lbl_r110['text'] = god_arvin5[9]
                #   lbl_r111['text'] = god_arvin5[10]

                  lbl_to11['text'] = god_arvin6[0]
                  lbl_to12['text'] = god_arvin6[1]
                  lbl_to13['text'] = god_arvin6[2]
                  lbl_to14['text'] = god_arvin6[3]
                  lbl_to15['text'] = god_arvin6[4]
                  lbl_to16['text'] = god_arvin6[5]
                  lbl_to17['text'] = god_arvin6[6]
                  lbl_to18['text'] = god_arvin6[7]
                  lbl_to19['text'] = god_arvin6[8]
                  lbl_to110['text'] = god_arvin6[9]
                #   lbl_to111['text'] = god_arvin6[10]

                  lbl_se11['text'] = god_arvin7[0]
                  lbl_se12['text'] = god_arvin7[1]
                  lbl_se13['text'] = god_arvin7[2]
                  lbl_se14['text'] = god_arvin7[3]
                  lbl_se15['text'] = god_arvin7[4]
                  lbl_se16['text'] = god_arvin7[5]
                  lbl_se17['text'] = god_arvin7[6]
                  lbl_se18['text'] = god_arvin7[7]
                  lbl_se19['text'] = god_arvin7[8]
                  lbl_se110['text'] = god_arvin7[9]
                #   lbl_se111['text'] = god_arvin7[10]              


            elif len(god_arvin) == 11 :
                 
                  lbl_11['text'] = god_arvin[0]
                  lbl_12['text'] = god_arvin[1]
                  lbl_13['text'] = god_arvin[2]
                  lbl_14['text'] = god_arvin[3]
                  lbl_15['text'] = god_arvin[4]
                  lbl_16['text'] = god_arvin[5]
                  lbl_17['text'] = god_arvin[6]
                  lbl_18['text'] = god_arvin[7]
                  lbl_19['text'] = god_arvin[8]
                  lbl_110['text'] = god_arvin[9]
                  lbl_111['text'] = god_arvin[10]

                  lbl_t11['text'] = god_arvin4[0]
                  lbl_t12['text'] = god_arvin4[1]
                  lbl_t13['text'] = god_arvin4[2]
                  lbl_t14['text'] = god_arvin4[3]
                  lbl_t15['text'] = god_arvin4[4]
                  lbl_t16['text'] = god_arvin4[5]
                  lbl_t17['text'] = god_arvin4[6]
                  lbl_t18['text'] = god_arvin4[7]
                  lbl_t19['text'] = god_arvin4[8]
                  lbl_t110['text'] = god_arvin4[9]
                  lbl_t111['text'] = god_arvin4[10]

                  lbl_r11['text'] = god_arvin5[0]
                  lbl_r12['text'] = god_arvin5[1]
                  lbl_r13['text'] = god_arvin5[2]
                  lbl_r14['text'] = god_arvin5[3]
                  lbl_r15['text'] = god_arvin5[4]
                  lbl_r16['text'] = god_arvin5[5]
                  lbl_r17['text'] = god_arvin5[6]
                  lbl_r18['text'] = god_arvin5[7]
                  lbl_r19['text'] = god_arvin5[8]
                  lbl_r110['text'] = god_arvin5[9]
                  lbl_r111['text'] = god_arvin5[10]

                  lbl_to11['text'] = god_arvin6[0]
                  lbl_to12['text'] = god_arvin6[1]
                  lbl_to13['text'] = god_arvin6[2]
                  lbl_to14['text'] = god_arvin6[3]
                  lbl_to15['text'] = god_arvin6[4]
                  lbl_to16['text'] = god_arvin6[5]
                  lbl_to17['text'] = god_arvin6[6]
                  lbl_to18['text'] = god_arvin6[7]
                  lbl_to19['text'] = god_arvin6[8]
                  lbl_to110['text'] = god_arvin6[9]
                  lbl_to111['text'] = god_arvin6[10]

                  lbl_se11['text'] = god_arvin7[0]
                  lbl_se12['text'] = god_arvin7[1]
                  lbl_se13['text'] = god_arvin7[2]
                  lbl_se14['text'] = god_arvin7[3]
                  lbl_se15['text'] = god_arvin7[4]
                  lbl_se16['text'] = god_arvin7[5]
                  lbl_se17['text'] = god_arvin7[6]
                  lbl_se18['text'] = god_arvin7[7]
                  lbl_se19['text'] = god_arvin7[8]
                  lbl_se110['text'] = god_arvin7[9]
                  lbl_se111['text'] = god_arvin7[10]              


            else:
                message_error = messagebox.showerror('Error','')   
















        else:
            message_error = messagebox.showerror('Error','')    
                  


#######################################  login ##############################################



win=Tk()
win.title(' logiin')
win.geometry('500x400+150+150')
win.resizable(False,False)
win.state('normal')


img=PhotoImage(file='02.png')
lbl=Label(win,image=img)
frm=Frame(win,bd=2,padx=5,pady=5,bg='#1d3f5c')
lbl1=Label(frm,width=15,font=('tahoma',12),text=':نام کاربري',fg='lightgray',bg='#1d3f5c')
lbl2=Label(frm,width=15,font=('tahoma',12),text=':رمز ورود',fg='lightgray',bg='#1d3f5c')
ent1=Entry(frm,width=20,bg='lightgray')
ent2=Entry(frm,width=20,show='*',bg='lightgray')
btn1=Button(frm,width=5,text='ورود',bg='lightgray',command=login)
img2 = PhotoImage(file='01.png')
btn2=Button(frm,image=img2,relief='flat',bg='lightgray',command=eye)

#######################################  main  ##############################################


win2=Toplevel()
width=win2.winfo_screenwidth()
height=win2.winfo_screenheight()
win2.geometry('%dx%d' % (width,height))
win2.title('main')
win2.state('withdrawn')
win2.configure(bg='gray12')

#frm_1=Frame(win2,bd=2,padx=40,pady=60,bg='gray25')
lbl_1=Label(win2,width=30,height=2,font=('tahoma',18),text='به سامانه مدیریت ورزشی خوش آمديد',fg='white',bg='gray25')
#btn_1=Button(win2,width=30,text=' تولید برنامه',bd=1,padx=20,pady=10,command=create)
btn_2=Button(win2,width=30,text='لیست ورزشکاران',bd=1,padx=20,pady=10,command=fish)
btn_3=Button(win2,width=30,text='لیست حرکات ورزشی',bd=1,padx=20,pady=10,command=fish2)
btn_4=Button(win2,width=30,text='خروج',bd=1,padx=20,pady=10,command=exit)

#######################################  tolid  ##############################################


win3=Toplevel()
width=win3.winfo_screenwidth()
height=win3.winfo_screenheight()
win3.geometry('%dx%d' % (width,height))
win3.title('tahvil')
win3.state('withdrawn')
win3.protocol('WM_DELETE_WINDOW',func10)

d9 = {'width' : 23  , 'font' : ('courier new' , 13) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl name
d8 = {'width' : 10  , 'font' : ('courier new' , 10) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl tekrar
d7 = {'width' : 18  , 'font' : ('courier new' , 10) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl tozihat
d6 = {'width' : 18  , 'font' : ('courier new' , 10) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl rest
d5 = {'width' : 10  , 'font' : ('courier new' , 10) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl set

frm11=LabelFrame(win3,width=width,height=height,bg='gray12')

lbl11=Label(frm11,d9)
lbl12=Label(frm11,d9)
lbl13=Label(frm11,d9)
lbl14=Label(frm11,d9)
lbl15=Label(frm11,d9)
lbl16=Label(frm11,d9)
lbl17=Label(frm11,d9)
lbl18=Label(frm11,d9)
lbl19=Label(frm11,d9)
lbl110=Label(frm11,d9)
lbl111=Label(frm11,d9)

lblt11=Label(frm11,d8)
lblt12=Label(frm11,d8)
lblt13=Label(frm11,d8)
lblt14=Label(frm11,d8)
lblt15=Label(frm11,d8)
lblt16=Label(frm11,d8)
lblt17=Label(frm11,d8)
lblt18=Label(frm11,d8)
lblt19=Label(frm11,d8)
lblt110=Label(frm11,d8)
lblt111=Label(frm11,d8)

lblse11=Label(frm11,d5)
lblse12=Label(frm11,d5)
lblse13=Label(frm11,d5)
lblse14=Label(frm11,d5)
lblse15=Label(frm11,d5)
lblse16=Label(frm11,d5)
lblse17=Label(frm11,d5)
lblse18=Label(frm11,d5)
lblse19=Label(frm11,d5)
lblse110=Label(frm11,d5)
lblse111=Label(frm11,d5)


lblr11=Label(frm11,d6)
lblr12=Label(frm11,d6)
lblr13=Label(frm11,d6)
lblr14=Label(frm11,d6)
lblr15=Label(frm11,d6)
lblr16=Label(frm11,d6)
lblr17=Label(frm11,d6)
lblr18=Label(frm11,d6)
lblr19=Label(frm11,d6)
lblr110=Label(frm11,d6)
lblr111=Label(frm11,d6)

lblto11=Label(frm11,d7)
lblto12=Label(frm11,d7)
lblto13=Label(frm11,d7)
lblto14=Label(frm11,d7)
lblto15=Label(frm11,d7)
lblto16=Label(frm11,d7)
lblto17=Label(frm11,d7)
lblto18=Label(frm11,d7)
lblto19=Label(frm11,d7)
lblto110=Label(frm11,d7)
lblto111=Label(frm11,d7)


lbltox11=Label(frm11,width=20,font=('courier new',15),bg='gray12',fg='white')
lblonvan11=Label(frm11,width=20,font=('courier new',13),bg='gray12',fg='white')
lbltozi11=Label(frm11,width=20,font=('courier new',12),bg='gray12',fg='white')



btn11=Button(frm11,width=22,text='ذخیره',bd=2,padx=5,pady=5,command=takeScreenshot)
btn12=Button(frm11,width=22,text='بازگشت',bd=2,padx=5,pady=5,command=back)



#combo10 = ttk.Combobox(frm11,values = lst4)
#combo10.set('لطفا انتخاب کنيد')
#combo10.place(x=300,y=500)r

#######################################  harekat ##############################################



win4=Toplevel()
width=win4.winfo_screenwidth()
height=win4.winfo_screenheight()
win4.geometry('%dx%d' % (width,height))
win4.title('harekat')
win4.state('withdrawn')
win4.protocol('WM_DELETE_WINDOW',func1)


frm__1=LabelFrame(win4,width=width,height=height,bg='gray12')
btn__1=Button(frm__1,width=22,text='اضافه',bd=2,padx=5,pady=5,command=new)
btn__2=Button(frm__1,width=22,text=' حذف',bd=2,padx=5,pady=5,command=delete)
btn__3=Button(frm__1,width=22,text=' بازگشت',bd=2,padx=5,pady=5,command=back5)




######################################################  حرکت جدید #####################################################################
win5=Toplevel()
win5.geometry('500x500+150+150')
win5.title('حرکت جدید')
win5.state('withdrawn')
win5.protocol('WM_DELETE_WINDOW',func2)

frm___1=Frame(win5,width=500,height=600,bg='black')
lbl___1=Label(frm___1,width=15,font=('tahoma',12),text='گروه تمرینی',fg='white',bg='black')
lbl___2=Label(frm___1,width=15,font=('tahoma',12),text='عضلات هدف',fg='white',bg='black')
lbl___3=Label(frm___1,width=15,font=('tahoma',12),text='حرکت',fg='white',bg='black')
lbl___4=Label(frm___1,width=15,font=('tahoma',12),text='شناسه',fg='white',bg='black')
#ent___1=Entry(frm___1,width=20,bg='lightgray')
ent___2=Entry(frm___1,width=20,bg='lightgray')
ent___3=Entry(frm___1,width=20,bg='lightgray')
btn___1=Button(frm___1,width=17,text=' ثبت',command=record1)
btn___2=Button(frm___1,width=17,text=' بازگشت',command=back6)


clist0000=['بالا تنه','پایین تنه','میان تنه','عضلات کور','فانکشنال']

    
combo1000 = ttk.Combobox(frm___1,width=17,values = clist0000)
combo1000.set('لطفا انتخاب کنيد')
combo1000.place(x=150,y=100)






#######################################  varzeshkaran ##############################################


win6=Toplevel()
width=win6.winfo_screenwidth()
height=win6.winfo_screenheight()
win6.geometry('%dx%d' % (width,height))
win6.title('varzeshkaran')
win6.state('withdrawn')
win6.protocol('WM_DELETE_WINDOW',func3)


frm____1=LabelFrame(win6,width=width,height=height,bg='black')
btn____1=Button(frm____1,width=22,text='اضافه',bd=2,padx=5,pady=5,command=new2)
btn____2=Button(frm____1,width=22,text=' حذف',bd=2,padx=5,pady=5,command=fish3)
btn____3=Button(frm____1,width=22,text=' بازگشت',bd=2,padx=5,pady=5,command=back3)
btn____4=Button(frm____1,width=22,text=' جستجو',bd=2,padx=5,pady=5,command=serchhh)

#######################################  varzeshkar new ##############################################


win7=Toplevel()

win7.geometry('1000x650+300+100')
win7.title('varzeshkar new')
win7.state('withdrawn')
win7.protocol('WM_DELETE_WINDOW',func4)

frm_____1=LabelFrame(win7,width=1000,height=650,bg='black')
lbl_____1=Label(frm_____1,width=20,font=('calibri',12),text='نام  ',bg='black',fg='white')
lbl_____3=Label(frm_____1,width=20,font=('calibri',12),text='تاریخ تولد ',bg='black',fg='white')
lbl_____4=Label(frm_____1,width=20,font=('calibri',12),text='قد  ',bg='black',fg='white')
lbl_____5=Label(frm_____1,width=20,font=('calibri',12),text='وزن قبلی  ',bg='black',fg='white')
lbl_____6=Label(frm_____1,width=20,font=('calibri',12),text='کدملی  ',bg='black',fg='white')
lbl_____7=Label(frm_____1,width=20,font=('calibri',12),text=' شماره همراه ',bg='black',fg='white')
lbl_____8=Label(frm_____1,width=20,font=('calibri',12),text='وزن فعلی  ',bg='black',fg='white')
lbl_____9=Label(frm_____1,width=20,font=('calibri',12),text='رشته ورزشی  ',bg='black',fg='white')
lbl_____10=Label(frm_____1,width=20,font=('calibri',12),text='گروه خونی  ',bg='black',fg='white')
lbl_____11=Label(frm_____1,width=20,font=('calibri',12),text='تیپ بدنی  ',bg='black',fg='white')
lbl_____12=Label(frm_____1,width=20,font=('calibri',12),text='سابقه آسیب یا جراحی  ',bg='black',fg='white')


ent_____1=Entry(frm_____1,width=30,)

ent_____3=Entry(frm_____1,width=30,)
ent_____4=Entry(frm_____1,width=30,)
ent_____5=Entry(frm_____1,width=30,)
ent_____6=Entry(frm_____1,width=30,)
ent_____7=Entry(frm_____1,width=30,)
ent_____8=Entry(frm_____1,width=30,)
ent_____9=Entry(frm_____1,width=30,)
ent_____10=Entry(frm_____1,width=30,)
ent_____11=Entry(frm_____1,width=30,)
ent_____12=Entry(frm_____1,width=30,)
btn_____1=Button(frm_____1,width=20,text=' ثبت',command=record2)
btn_____2=Button(frm_____1,width=20,text=' بازگشت',command=back4)


#######################################  tahvil_barname ##############################################


win8=Toplevel()
width=win8.winfo_screenwidth()
height=win8.winfo_screenheight()
win8.geometry('%dx%d' % (width,height))
win8.title('tolid_barname')
win8.state('withdrawn')
win8.protocol('WM_DELETE_WINDOW',func5)

frm111=LabelFrame(win8,width=width,height=height,bg='black')
                  
 
lst4 = [ 'بالا تنه','پایین تنه','میان تنه','عضلات کور','فانکشنال' ]
# row = cur.execute('SELECT  gp_tamrini  FROM harekata')
# for i in row :
#         lst4.append(i)
        
combo22 = ttk.Combobox(frm111,width=25,values = lst4)
combo22.set('لطفا انتخاب کنيد')
combo22.place(x=1350,y=80)


ent1101=Entry(frm111,width=20)
ent1102=Entry(frm111,width=20)
ent1103=Entry(frm111,width=25)
ent1104=Entry(frm111,width=20)
ent1105=Entry(frm111,width=20)
ent1106=Entry(frm111,width=20)

lbl1101=Label(frm111,width=20,font=('calibri',11),text='استراحت',bg='black',fg='white')
lbl1102=Label(frm111,width=20,font=('calibri',11),text='تکرار',bg='black',fg='white')
lbl1103=Label(frm111,width=20,font=('calibri',11),text='توضیحات ',bg='black',fg='white')
lbl1104=Label(frm111,width=20,font=('calibri',11),text='ست ',bg='black',fg='white')
lbl1105=Label(frm111,width=20,font=('calibri',11),text='عنوان برنامه ',bg='black',fg='white')
lbl1106=Label(frm111,width=20,font=('calibri',11),text='توضیحات کلی ',bg='black',fg='white')


btn100=Button(frm111,width=15,text='پاک کردن لیست',bd=2,padx=5,pady=5,command=listcleaner)
btn101=Button(frm111,width=15,text='مشاهده لیست',bd=2,padx=5,pady=5,command=listmaker)
btn102=Button(frm111,width=25,text=' اضافه کردن حرکت جدید',bd=2,padx=5,pady=5,command=new)
btn103=Button(frm111,width=25,text='تحویل برنامه',bd=2,padx=5,pady=5,command=emp)
btn112=Button(frm111,width=15,text=' بازگشت',bd=2,padx=5,pady=5,command=back2)
btn113=Button(frm111,width=10,text=' بعدی',bd=2,padx=5,pady=0,command=nextt)
#btn114=Button(frm111,width=10,text=' بعدی',bd=2,padx=5,pady=0,command=nextt2)
#btn115=Button(frm111,width=10,text=' بعدی',bd=2,padx=5,pady=0,command=nextt3)
#############################################################################################################################3

win9=Toplevel()
win9.geometry('400x450+150+150')
win9.title('hazf_hareakat')
win9.state('withdrawn')
win9.protocol('WM_DELETE_WINDOW',func6)

frm1111=LabelFrame(win9,width=400,height=450,bg='black')
ent1111=Entry(frm1111,width=30)
lbl1111=Label(frm1111,width=20,font=('calibri',11),text='شناسه مورد نظر را وارد کنید',bg='black',fg='white')
btn1111=Button(frm1111,width=15,text=' حذف نهایی',command=delete_finally)
##################################################################################################
win10=Toplevel()
win10.geometry('400x450+150+150')
win10.title('serch')
win10.state('withdrawn')

frm11111=LabelFrame(win10,width=400,height=450,bg='black')

ent11111=Entry(frm11111,width=30)
ent11112=Entry(frm11111,width=10)
ent11113=Entry(frm11111,width=30)
lbl11111=Label(frm11111,width=20,font=('calibri',11),text='شماره موبایل مورد نظر را وارد کنید ' ,bg='black',fg='white')

btn11111=Button(frm11111,width=15,text=' جستجو نهایی',command=final_serch)


##################################################################################################
win11=Toplevel()
win11.geometry('1850x800+0+0')
win11.title('profile')
win11.state('withdrawn')
win11.protocol('WM_DELETE_WINDOW',func7)

frm01=LabelFrame(win11,width=1850,height=800,bg='black')

lbl01=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl02=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl03=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl04=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl05=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl06=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl07=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl08=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl09=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl010=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')
lbl011=Label(frm01,width=20,font=('calibri',11),bg='black',fg='white')


lbl001=Label(frm01,width=20,font=('calibri',11),text = 'کد ملی',bg='black',fg='white')
lbl002=Label(frm01,width=20,font=('calibri',11),text = 'نام',bg='black',fg='white')
lbl003=Label(frm01,width=20,font=('calibri',11),text = 'تاریخ تولد',bg='black',fg='white')
lbl004=Label(frm01,width=20,font=('calibri',11),text = 'قد',bg='black',fg='white')
lbl005=Label(frm01,width=20,font=('calibri',11),text = 'وزن قبلی',bg='black',fg='white')
lbl006=Label(frm01,width=20,font=('calibri',11),text = 'وزن فعلی',bg='black',fg='white')
lbl007=Label(frm01,width=20,font=('calibri',11),text = 'شماره همراه',bg='black',fg='white')
lbl008=Label(frm01,width=20,font=('calibri',11),text = 'رشته ورزشی',bg='black',fg='white')
lbl009=Label(frm01,width=20,font=('calibri',11),text = 'تیپ بدنی ',bg='black',fg='white')
lbl0010=Label(frm01,width=20,font=('calibri',11),text = 'گروه خونی',bg='black',fg='white')
lbl0011=Label(frm01,width=20,font=('calibri',11),text = 'سابقه آسیب یا جراحی',bg='black',fg='white')

btn01=Button(frm01,width=15,text=' تولید برنامه',command=create)
btn02=Button(frm01,width=18,text=' مشاهده برنامه های قبلی ',command=old)

#################################################################################################
win12=Toplevel()
win12.geometry('400x450+150+150')
win12.title('hazf_varzeshkar')
win12.state('withdrawn')
win12.protocol('WM_DELETE_WINDOW',func12)

frm01111=LabelFrame(win12,width=400,height=450,bg='black')
ent01111=Entry(frm01111,width=30)
lbl01111=Label(frm01111,width=20,font=('calibri',11),text='کدملی مورد نظر را وارد کنید' ,bg='black',fg='white')
btn01111=Button(frm01111,width=15,text=' حذف نهایی',command=delete_finally_athlee)

######################################################################################################
win13=Toplevel()
width=win13.winfo_screenwidth()
height=win13.winfo_screenheight()
win13.geometry('%dx%d' % (width,height))
win13.title('record_brname')
win13.state('withdrawn')
win13.protocol('WM_DELETE_WINDOW',func11)

# d9 = {'width' : 23  , 'font' : ('courier new' , 13) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl name
# d8 = {'width' : 10  , 'font' : ('courier new' , 10) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl tekrar
# d7 = {'width' : 18  , 'font' : ('courier new' , 10) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl tozihat
# d6 = {'width' : 18  , 'font' : ('courier new' , 10) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl rest
# d5 = {'width' : 10  , 'font' : ('courier new' , 10) , 'bd' : 2 , 'anchor' : 'e' , 'bg' : 'gray12','fg':'azure'}           # Lbl set

frm_11=LabelFrame(win13,width=width,height=height,bg='gray12')

lbl_11=Label(frm_11,d9)
lbl_12=Label(frm_11,d9)
lbl_13=Label(frm_11,d9)
lbl_14=Label(frm_11,d9)
lbl_15=Label(frm_11,d9)
lbl_16=Label(frm_11,d9)
lbl_17=Label(frm_11,d9)
lbl_18=Label(frm_11,d9)
lbl_19=Label(frm_11,d9)
lbl_110=Label(frm_11,d9)
lbl_111=Label(frm_11,d9)

lbl_t11=Label(frm_11,d8)
lbl_t12=Label(frm_11,d8)
lbl_t13=Label(frm_11,d8)
lbl_t14=Label(frm_11,d8)
lbl_t15=Label(frm_11,d8)
lbl_t16=Label(frm_11,d8)
lbl_t17=Label(frm_11,d8)
lbl_t18=Label(frm_11,d8)
lbl_t19=Label(frm_11,d8)
lbl_t110=Label(frm_11,d8)
lbl_t111=Label(frm_11,d8)

lbl_se11=Label(frm_11,d5)
lbl_se12=Label(frm_11,d5)
lbl_se13=Label(frm_11,d5)
lbl_se14=Label(frm_11,d5)
lbl_se15=Label(frm_11,d5)
lbl_se16=Label(frm_11,d5)
lbl_se17=Label(frm_11,d5)
lbl_se18=Label(frm_11,d5)
lbl_se19=Label(frm_11,d5)
lbl_se110=Label(frm_11,d5)
lbl_se111=Label(frm_11,d5)


lbl_r11=Label(frm_11,d6)
lbl_r12=Label(frm_11,d6)
lbl_r13=Label(frm_11,d6)
lbl_r14=Label(frm_11,d6)
lbl_r15=Label(frm_11,d6)
lbl_r16=Label(frm_11,d6)
lbl_r17=Label(frm_11,d6)
lbl_r18=Label(frm_11,d6)
lbl_r19=Label(frm_11,d6)
lbl_r110=Label(frm_11,d6)
lbl_r111=Label(frm_11,d6)

lbl_to11=Label(frm_11,d7)
lbl_to12=Label(frm_11,d7)
lbl_to13=Label(frm_11,d7)
lbl_to14=Label(frm_11,d7)
lbl_to15=Label(frm_11,d7)
lbl_to16=Label(frm_11,d7)
lbl_to17=Label(frm_11,d7)
lbl_to18=Label(frm_11,d7)
lbl_to19=Label(frm_11,d7)
lbl_to110=Label(frm_11,d7)
lbl_to111=Label(frm_11,d7)


lbl_tox11=Label(frm_11,width=20,font=('courier new',15),bg='gray12',fg='white')
lbl_onvan11=Label(frm_11,width=20,font=('courier new',13),bg='gray12',fg='white')
lbl_tozi11=Label(frm_11,width=20,font=('courier new',12),bg='gray12',fg='white')









##################################################################################################
lbl.place(x=0,y=0)
frm.place(x=80,y=150)
lbl1.grid(row=1,column=2)
lbl2.grid(row=2,column=2)
ent1.grid(row=1,column=1)
ent2.grid(row=2,column=1)
btn1.grid(row=3,column=1,columnspan=2)
btn2.grid(row=3,column=2,columnspan=3)

###################################    main      #################################################

#frm_1.place(x=650,y=300)
lbl_1.place(x=620,y=50)
#btn_1.place(x=700,y=600)
btn_2.place(x=500,y=400)
btn_3.place(x=900,y=400)
btn_4.place(x=700,y=750)

#####################################              harekata           #############################################################################
frm__1.place(x=0,y=0)
btn__1.place(x=600,y=730)
btn__2.place(x=800,y=730)
btn__3.place(x=700,y=780)


###########################################              صفحه اضاقه کردن حرکت             ################################################################


frm___1.place(x=0,y=0)
lbl___1.place(x=300,y=100)
lbl___2.place(x=300,y=160)
lbl___3.place(x=300,y=220)
lbl___4.place(x=300,y=280)
#ent___1.place(x=150,y=100)
ent___2.place(x=150,y=160)
ent___3.place(x=150,y=220)
#combo1.place(x=150,y=280)

btn___1.place(x=300,y=340)
btn___2.place(x=120,y=340)




#############################################################   varzeshkaran    ##################################################################################

frm____1.place(x=0,y=0)
btn____1.place(x=400,y=750)
btn____2.place(x=600,y=750)
btn____3.place(x=1000,y=750)
btn____4.place(x=800,y=750)


frm_____1.place(x=0,y=0)
lbl_____1.place(x=800,y=200)

lbl_____3.place(x=800,y=300)
lbl_____4.place(x=800,y=350)
lbl_____5.place(x=800,y=400)
lbl_____6.place(x=800,y=450)
lbl_____7.place(x=400,y=200)
lbl_____8.place(x=400,y=250)
lbl_____9.place(x=400,y=300)
lbl_____10.place(x=400,y=350)
lbl_____11.place(x=400,y=400)
lbl_____12.place(x=400,y=450)

ent_____1.place(x=600,y=200)

ent_____3.place(x=600,y=300)
ent_____4.place(x=600,y=350)
ent_____5.place(x=600,y=400)
ent_____6.place(x=600,y=450)
ent_____7.place(x=200,y=200)
ent_____8.place(x=200,y=250)
ent_____9.place(x=200,y=300)
ent_____10.place(x=200,y=350)
ent_____11.place(x=200,y=400)
ent_____12.place(x=200,y=450)

btn_____1.place(x=500,y=550)
btn_____2.place(x=300,y=550)

#############################################################################################
frm11.place(x=0,y=0)

btn11.place(x=700 ,y =800)
btn12.place(x=400 ,y =800)

lbl11.place(x=1350,y=150)
lbl12.place(x=1350,y=200)
lbl13.place(x=1350,y=250)
lbl14.place(x=1350,y=300)
lbl15.place(x=1350,y=350)
lbl16.place(x=1350,y=400)
lbl17.place(x=1350,y=450)
lbl18.place(x=1350,y=500)
lbl19.place(x=1350,y=550)
lbl110.place(x=1350,y=600)
lbl111.place(x=1350,y=650)

lblt11.place(x=1230,y=150)
lblt12.place(x=1230,y=200)
lblt13.place(x=1230,y=250)
lblt14.place(x=1230,y=300)
lblt15.place(x=1230,y=350)
lblt16.place(x=1230,y=400)
lblt17.place(x=1230,y=450)
lblt18.place(x=1230,y=500)
lblt19.place(x=1230,y=550)
lblt110.place(x=1230,y=600)
lblt111.place(x=1230,y=650)

lblse11.place(x=1130,y=150)
lblse12.place(x=1130,y=200)
lblse13.place(x=1130,y=250)
lblse14.place(x=1130,y=300)
lblse15.place(x=1130,y=350)
lblse16.place(x=1130,y=400)
lblse17.place(x=1130,y=450)
lblse18.place(x=1130,y=500)
lblse19.place(x=1130,y=550)
lblse110.place(x=1130,y=600)
lblse111.place(x=1130,y=650)


lblto11.place(x=970,y=150)
lblto12.place(x=970,y=200)
lblto13.place(x=970,y=250)
lblto14.place(x=970,y=300)
lblto15.place(x=970,y=350)
lblto16.place(x=970,y=400)
lblto17.place(x=970,y=450)
lblto18.place(x=970,y=500)
lblto19.place(x=970,y=550)
lblto110.place(x=970,y=600)
lblto111.place(x=970,y=650)

lblr11.place(x=800,y=150)
lblr12.place(x=800,y=200)
lblr13.place(x=800,y=250)
lblr14.place(x=800,y=300)
lblr15.place(x=800,y=350)
lblr16.place(x=800,y=400)
lblr17.place(x=800,y=450)
lblr18.place(x=800,y=500)
lblr19.place(x=800,y=550)
lblr110.place(x=800,y=600)
lblr111.place(x=800,y=650)




lbltox11.place(x=1350,y=50)
lblonvan11.place(x=650,y=50)
lbltozi11.place(x=50,y=50)
#####################################################################################################
frm111.place(x=0,y=0)

btn100.place(x=1000,y=650)
btn101.place(x=1000,y=700)
btn102.place(x=1350,y=750)
btn103.place(x=610,y=750)
btn112.place(x=1000,y=750)
btn113.place(x=1400,y=130)

lbl1101.place(x=630,y=80)
lbl1102.place(x=1120,y=80)
lbl1103.place(x=810,y=80)
lbl1104.place(x=980,y=80)
lbl1105.place(x=620,y=550)
lbl1106.place(x=620,y=650)


ent1101.place(x=650,y=130)
ent1102.place(x=1150,y=130)
ent1103.place(x=820,y=130)
ent1104.place(x=1000,y=130)
ent1105.place(x=645,y=580)
ent1106.place(x=645,y=680)
#btn114.place(x=950,y=100)
#btn115.place(x=650,y=100)
####################################################
frm1111.place(x=0,y=0)
btn1111.place(x=140,y=200)
lbl1111.place(x=180,y=150)
ent1111.place(x=100,y=150)

###################################################################3

frm11111.place(x=0,y=0)

btn11111.place(x=200,y=290)

lbl11111.place(x=200,y=130)
ent11111.place(x=50,y=130)



###############################################################################


frm01.place(x=0,y=0)

lbl01.place(x=50,y=100)
lbl02.place(x=50,y=150)
lbl03.place(x=50,y=200)
lbl04.place(x=50,y=250)
lbl05.place(x=50,y=300)
lbl06.place(x=50,y=350)
lbl07.place(x=50,y=400)
lbl08.place(x=50,y=450)
lbl09.place(x=50,y=500)
lbl010.place(x=50,y=550)
lbl011.place(x=50,y=600)

lbl001.place(x=300,y=100)
lbl002.place(x=300,y=150)
lbl003.place(x=300,y=200)
lbl004.place(x=300,y=250)
lbl005.place(x=300,y=300)
lbl006.place(x=300,y=350)
lbl007.place(x=300,y=400)
lbl008.place(x=300,y=450)
lbl009.place(x=300,y=500)
lbl0010.place(x=300,y=550)
lbl0011.place(x=300,y=600)

btn01.place(x=300,y=700)
btn02.place(x=100,y=700)


#################################################################################################
frm01111.place(x=0,y=0)
btn01111.place(x=140,y=200)
lbl01111.place(x=180,y=150)
ent01111.place(x=100,y=150)

##################################################################################################
frm_11.place(x=0,y=0)



lbl_11.place(x=1350,y=150)
lbl_12.place(x=1350,y=200)
lbl_13.place(x=1350,y=250)
lbl_14.place(x=1350,y=300)
lbl_15.place(x=1350,y=350)
lbl_16.place(x=1350,y=400)
lbl_17.place(x=1350,y=450)
lbl_18.place(x=1350,y=500)
lbl_19.place(x=1350,y=550)
lbl_110.place(x=1350,y=600)
lbl_111.place(x=1350,y=650)

lbl_t11.place(x=1230,y=150)
lbl_t12.place(x=1230,y=200)
lbl_t13.place(x=1230,y=250)
lbl_t14.place(x=1230,y=300)
lbl_t15.place(x=1230,y=350)
lbl_t16.place(x=1230,y=400)
lbl_t17.place(x=1230,y=450)
lbl_t18.place(x=1230,y=500)
lbl_t19.place(x=1230,y=550)
lbl_t110.place(x=1230,y=600)
lbl_t111.place(x=1230,y=650)

lbl_se11.place(x=1130,y=150)
lbl_se12.place(x=1130,y=200)
lbl_se13.place(x=1130,y=250)
lbl_se14.place(x=1130,y=300)
lbl_se15.place(x=1130,y=350)
lbl_se16.place(x=1130,y=400)
lbl_se17.place(x=1130,y=450)
lbl_se18.place(x=1130,y=500)
lbl_se19.place(x=1130,y=550)
lbl_se110.place(x=1130,y=600)
lbl_se111.place(x=1130,y=650)


lbl_to11.place(x=970,y=150)
lbl_to12.place(x=970,y=200)
lbl_to13.place(x=970,y=250)
lbl_to14.place(x=970,y=300)
lbl_to15.place(x=970,y=350)
lbl_to16.place(x=970,y=400)
lbl_to17.place(x=970,y=450)
lbl_to18.place(x=970,y=500)
lbl_to19.place(x=970,y=550)
lbl_to110.place(x=970,y=600)
lbl_to111.place(x=970,y=650)

lbl_r11.place(x=800,y=150)
lbl_r12.place(x=800,y=200)
lbl_r13.place(x=800,y=250)
lbl_r14.place(x=800,y=300)
lbl_r15.place(x=800,y=350)
lbl_r16.place(x=800,y=400)
lbl_r17.place(x=800,y=450)
lbl_r18.place(x=800,y=500)
lbl_r19.place(x=800,y=550)
lbl_r110.place(x=800,y=600)
lbl_r111.place(x=800,y=650)




lbl_tox11.place(x=1350,y=50)
lbl_onvan11.place(x=650,y=50)
lbl_tozi11.place(x=50,y=50)




win.mainloop()