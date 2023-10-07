from tkinter import * 

root = Tk()
root.title('Sales App')
root.geometry('700x700')
root.configure(background = 'snow')

MONTHS = ('January', 'Febuary', 'March', 'April', 
    'May', 'June', 'July', 'August', 
    'September', 'October', 'November', 'December')
PROFITS = (1000, 2000, 3000, 4000, 3000, 5000, 4000,
    7000, 5000, 3000, 2000, 6000, 1000, 2000
)

lblMonths = Label(root, text = str(MONTHS), background = 'light blue')
lblMonths.place(relx = 0.5, rely = 0.3, anchor = CENTER)
lblProfits = Label(root, text = str(PROFITS), background = 'light blue')
lblProfits.place(relx = 0.5, rely = 0.4, anchor = CENTER)

lblStats = Label(root, text = '', background = 'light blue')
lblStats.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def showStats():
    lblStats['text'] = 'Maximum profits made was $' + str(max(PROFITS)) + ' in ' + str(MONTHS[PROFITS.index(max(PROFITS))]) + '.\n'
    lblStats['text'] += 'Minimum profits made was $' + str(min(PROFITS)) + ' in ' + str(MONTHS[PROFITS.index(min(PROFITS))]) + '.'

btnStats = Button(root, text = 'Show Profit Statistics', command = lambda: showStats())
btnStats.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()