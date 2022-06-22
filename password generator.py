import tkinter as tk     


############################################################################
# Initialize global values (i, j, and words)
############################################################################
i = 0
j = 0
words = []

############################################################################
# Define functions
############################################################################
def add_wd(first_word):
    #
    '''
        This function creates a list of two words entered by user and also to
        turns the buttons gray to show they have been pressed.
    '''
    #
    global i, words
     
    if i == 2:             # This conditional allows you to create more
        i = 0              # than one password.
        words *= 0
    i += 1
    words.append(first_word)
    if i==1:
        word1_btn.config(highlightbackground='gray')
    elif i==2:
        word2_btn.config(highlightbackground='gray')
    return 


def create_file(hint_file_name):
    '''
        This function is use to create a hint file in a specific location.
    '''
    global filname
    filname = hint_file_name
    
    file_btn.config(highlightbackground='gray')
    return

def write_hint(hint):
    '''
        This function will print out hints for the input password for user.
    '''
    
    global j
    j += 1
    if j==1:
        hint1_btn.config(highlightbackground='gray')
    elif i==2:
        hint2_btn.config(highlightbackground='gray')
    pw_hint = open(filname, 'a')
    print(pw_hint, file=pw_hint)
    pw_hint.close() 
    return

def gen_pw():
    global text
    passwd = words[1].lower() + words[0].lower()
    passwd = passwd.replace('e', '3')
    passwd = passwd.replace('i', '!')
    passwd = passwd.replace('o', 'F')
    passwd = passwd.replace('s', 'X')
    passwd = passwd.replace('a', 's')
    passwd = passwd.replace('u', '_')
    passwd = passwd.replace('r', '*')
    passwd = passwd.replace('p', 'r')
    passwd = passwd.replace('t', 'P')
    passwd = passwd.replace('m', 'W')
    passwd = passwd.replace('g', '9')
    passwd = passwd.replace('d', 'E')
    passwd = passwd.replace('b', 'd')
    passwd = passwd.replace('c', 'o')
    passwd = passwd.replace('n', 'u')
    passwd = passwd.replace('h', '4')
    passwd = passwd.replace('y', 'R')
    passwd = passwd.replace('j', 'L')
    passwd = passwd.replace(' ', '$')
    passwd = passwd.replace('1', 'a')
    passwd = passwd.replace('2', 'B')
    passwd = passwd.replace('5', '2')
    passwd = passwd.replace('6', 'D')
    passwd = passwd.replace('7', '&') 
    passwd = passwd.replace('8', '-')
    
    print(passwd)          # Print password to check GUI output
    text.set(passwd)       # Display password in GUI
    return

###########################################################################
# Set up window.
############################################################################

hgt = 800                 # Set height and width of canvas
wdth = 1000
win = tk.Tk()              # Define window
win.title('Password Generator UWU')  # Assign title to window

#create canvas object
canvas = tk.Canvas(win, height=hgt, width=wdth)  # Create canvas
canvas.pack()                                    # Display canvas



bg_image = tk.PhotoImage(file='C:\\Users\\draxl\\Desktop\\Password Generator (python)\\passGen\\sunset.png')  # Get background image
bg_label = tk.Label(win, image=bg_image)         # Create label for image
bg_label.place(relwidth=1, relheight=1)          # Display label

lbl=tk.Label(win, text="By Waddhanabot Yi", fg = "grey", bg = "#FAF0D7", font=('Kiona', 14))
lbl.pack(pady = 7)



############################################################################
# Set up word entry area.
############################################################################
#***********First frame box (first and last name)***********

word_frame = tk.Frame(win, bg='#eaac8b', bd=10)  # Create frame
                                                 # Display frame
word_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.2, anchor='n')


                                                 # Create entry widget
                                                 # Display entry widget
word1_entry = tk.Entry(word_frame, font=('Kiona', 16))
word1_entry.place(relx=0, rely=0, relwidth=0.5, relheight=0.4)

word1_btn = tk.Button(word_frame, text='Press to enter first word', font=('Kiona', 14), anchor='w', command=lambda: add_wd(word1_entry.get()))
word1_btn.place(relx=0.53, rely=0, relwidth=0.47, relheight=0.4)

                                                 # Create entry widget
                                                 # Display entry widget
word2_entry = tk.Entry(word_frame, font=('Kiona', 16))
word2_entry.place(relx=0, rely=0.525, relwidth=0.5, relheight=0.4)


                                                 # Create button widget
                                                 # Display button widget
word2_btn = tk.Button(word_frame, text='Press to enter second word', font=('Kiona', 14), anchor='w', command=lambda: add_wd(word2_entry.get()))
word2_btn.place(relx=0.53, rely=0.525, relwidth= 0.47, relheight = 0.4)

############################################################################
# Set up hint entry area.
############################################################################
#***********Second Frame Box***********

hint_frame = tk.Frame(win, bg='#eaac8b', bd=10)
hint_frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.275, anchor='n')
                                                 # Create entry widget
                                                 # Display entry widget
file_entry = tk.Entry(hint_frame, font=('Kiona', 16))
file_entry.place(relx=0, rely=0, relwidth=0.5, relheight=0.26)

                                                 # Create button widget
                                                 # Display button widget
file_btn = tk.Button(hint_frame, text='Press to enter file name', font=('Kiona', 14), anchor='w', command=lambda: create_file(file_entry.get()))
file_btn.place(relx=0.53, rely=0.0, relwidth=0.47, relheight=0.26)

                                                 # Create entry widget
                                                 # Display entry widget
hint1_entry = tk.Entry(hint_frame, font=('Kiona', 16))
hint1_entry.place(relx=0, rely=0.375, relwidth=0.5, relheight=0.26)

                                                 # Create button widget
                                                 # Display button widget
hint1_btn = tk.Button(hint_frame, text='Press to enter first hint', font=('Kiona', 14), anchor='w', command=lambda: write_hint(hint1_entry.get()))
hint1_btn.place(relx=0.53, rely=0.375, relwidth=0.47, relheight=0.26)

                                                 # Create entry widget
                                                 # Display entry widget
hint2_entry = tk.Entry(hint_frame, font=('Kiona', 16))
hint2_entry.place(relx=0, rely=0.75, relwidth=0.5, relheight=0.26)

                                                 # Create button widget
                                                 # Display button widget
hint2_btn = tk.Button(hint_frame, text='Press to enter second hint', font=('Kiona', 14), anchor='w', command=lambda: write_hint(hint2_entry.get()))
hint2_btn.place(relx=0.53, rely=0.75, relwidth=0.47, relheight=0.26)

############################################################################
# Set up password area and window closure.
############################################################################
# Finally, add frame for printing the password.

pw_frame = tk.Frame(win, bg='#eaac8b', bd=10)
pw_frame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.1, anchor='n')

text = tk.StringVar()                            # Initialize text
                                                 # Create label widget
                                                 # Display label widget
pw_label= tk.Label(pw_frame, font=('Kiona', 16), textvariable=text)
pw_label.place(relx=0, rely=0, relwidth=0.5, relheight=1)

                                                 # Create button widget
                                                 # Display button widget
pw_btn = tk.Button(pw_frame, text='Press for password', font=('Kiona', 14), command=gen_pw)
pw_btn.place(relx=0.53, rely=0, relwidth=0.47, relheight=1)

#Frame for Done
close_frame = tk.Frame(win, bg='#eaac8b', bd=10)
close_frame.place(relx=0.5, rely=0.9, relwidth=0.12, relheight=0.057, anchor='n')
                                                 # Create button widget
                                                 # Display button widget
close_btn=tk.Button(win, font=('Kiona', 14), text='Done', command=win.destroy)
close_btn.place(relx=0.5, rely=.9, relwidth=0.1, relheight=0.05, anchor='n')

win.mainloop()
############################################################################
