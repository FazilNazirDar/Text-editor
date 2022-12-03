import tkinter as tk
from tkinter import BOTH, FLAT, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
from turtle import title
main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title("VPAD")
# ******main menu*******
main_menu=tk.Menu()
# File icons
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')

file=tk.Menu(main_menu,tearoff=False)

# Edit Icons
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')

edit=tk.Menu(main_menu,tearoff=False)

# VIEW ICONS
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')

view=tk.Menu(main_menu,tearoff=False)

#COLOR THEMES
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')

color_theme=tk.Menu(main_menu,tearoff=False)
theme_color=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'Little Default':('#000000','#ffffff'),
    'Little Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8d8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}


main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)
#***********END MAIN MENU*********************

#***********TOOL BAR*************************
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
# FONT BOX
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_family_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_family_box['values']=font_tuple
font_family_box.grid(row=0,column=0,padx=5)
font_family_box.current(font_tuple.index('Arial'))
#FONT SIZE BOX
font_size=tk.IntVar()
font_size_box=ttk.Combobox(tool_bar,width=14,textvariable=font_size,state='readonly')
font_size_box['values']=tuple(range(8,80,2))
font_size_box.grid(row=0,column=1,padx=5)
font_size_box.current(2)
#*BOLD BUTTON
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
#ITALIC BUTTON
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
#*UNDERLINE BUTTON
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

#FONT COLOR BUTTON
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

#ALIGN LEFT BUTTON
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

#ALIGN CENTER BUTTON
align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)
#ALIGN RIGHT BUTTON
align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)
#******************TOOL BAR END***********************

#*******************TEXT EDITOR***********************
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)
text_editor.focus_set()
scroll_bar=tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#FONT FAMILY AND FONT SIZE FUNCTIONALITY
current_font_family='Arial'
current_font_size=12

def change_fontFamily(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_fontSize(event=None):
    global current_font_size
    current_font_size=font_size.get()
    text_editor.configure(font=(current_font_family,current_font_size))
font_family_box.bind('<<ComboboxSelected>>', change_fontFamily)   
font_size_box.bind('<<ComboboxSelected>>',change_fontSize)

#BOLD BUTTON FUNCTIONALITY
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold)
#ITALIC BUTTON FUNCTIONALITY
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=change_italic)
#UNDERLINE BUTTON FUNCTIONALITY
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)

#FONT COLOR FUNCTIONALITY
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    # we are selecting hashvalue of color
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)

#*****ALIGNMENT FUNCTIONALITY****
# LEFT ALIGN
def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_btn.configure(command=align_left)
# CENTER ALIGN
def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_btn.configure(command=align_center)
# RIGHT ALIGN
def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
align_right_btn.configure(command=align_right)


text_editor.configure(font=('Arial',12))

#***************END TEXT EDITOR************
# ************STATUS BAR****************
status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_change=False
def changed(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))  #.replace(' ','') is used to remove spaces 
        status_bar.config(text=f'characters: {characters} words: {words}' )
        text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)

# *************MAIN MENU FUNCTIONALITY*****************

# FILE COMMANDS
# new functionality
url = ""
def new_file():
    global url
    url=''
    text_editor.delete(1.0,tk.END)
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
#open functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select file',filetypes=(('Text file','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return  
    main_application.title(os.path.basename(url))       
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

#save functionality
def save_file(event=None):
    global url
    try:
        if url:
            content =text_editor.get(1.0,tk.END)
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:  
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('all files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
#save as functionality
def save_as(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('all files','*.*')))
        url.write(content)
        url.close()
    except:
        return 

file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as)
#Exit Functionality
def exit_file(event = None):
    global url,text_change
    try:
        if text_change:
            mbox=messagebox.askyesnocancel('Warning','Do you want the file?')
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All file','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif  mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 
        
        
            
            

file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_file)

# EDIT COMMANDS
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda : text_editor.event_generate('<Control c>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F')
#VIEW COMMANDS
view.add_checkbutton(label='Tool Bar',image=tool_bar_icon,compound=tk.LEFT)
view.add_checkbutton(label='Status Bar',image=status_bar_icon,compound=tk.LEFT)
#COLOR THEME
count=0 
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_color,compound=tk.LEFT)
    count+=1




main_application.config(menu=main_menu)
main_application.mainloop()