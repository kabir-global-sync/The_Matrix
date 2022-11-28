from tkinter import *

import determinant_calculator as det

root = Tk()
root.title('Matrix Application')
root.configure(bg='#363636')
global_font = ('Consolas', 12)
###########################################################################################
frm1 = LabelFrame(root, text='Determiant', padx=10, bg='#363636', fg='white')
frm1.grid(row=0, column=0, pady=10)

frm2 = LabelFrame(root, text='Matrix', padx=20, bg='#363636', fg='white')
frm2.grid(row=1, column=0, pady=10)

frmVector = LabelFrame(root, text='Vector', padx=20, bg='#363636', fg='white')
frmVector.grid(row=2, column=0, pady=10)


def buttonHover(button, onEnter, onLeave):
    button.bind('<Leave>', func=lambda w: button.config(background=onEnter))
    button.bind('<Enter>', func=lambda w: button.config(background=onLeave))


###########################################################################################
# For determinants part
def row_col_number():
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    order1 = StringVar()
    menu_label = Label(frm1, text='Select Order', bg='#363636', fg='white', font=('Roboto', 12))
    menu_label.grid(row=1, column=0, columnspan=2)
    menu = OptionMenu(frm1, order1, *numbers)
    menu.config(bg='#363636', fg='white', font=('Consolas', 10))
    menu.grid(row=1, column=2, pady=(0, 5))
    mat_set = Button(frm1, text='Set Matrix', pady=5, command=lambda: set_matrix_determinant(order1.get()),
                     bg='#007979', fg='white', font=('Consolas', 10))
    mat_set.grid(row=2, column=1, ipadx=114, columnspan=2, pady=(0, 5))
    buttonHover(mat_set, '#007979', '#008879')


main_mat = []
a = []


def set_matrix_determinant(x):
    global root2
    root2 = Tk()
    root2.title('Matrix Value Input')
    global lbl, main_mat
    main_mat = []
    lbl = Label(root2, text="", font=('Roboto', 15))
    lbl.grid(row=int(x) + 2, column=1, columnspan=int(x))
    global e, a
    for j in range(int(x)):
        for i in range(int(x)):
            Label(root2, text=f'R{i + 1}').grid(row=i + 1, column=0)
            Label(root2, text=f'C{j + 1}').grid(row=0, column=j + 1)
            e = Entry(root2, width=6, font=global_font)
            e.grid(row=j + 1, column=i + 1, padx=3, pady=2)
            a.append(e)
        main_mat.append(a)
        a = []

    calc_button = Button(root2, text='Calculate', command=lambda: determinant(x))
    calc_button.grid(row=int(x) + 1, column=1, columnspan=2, pady=5)


def determinant(x):
    global main_mat

    final_matrix = [[int(main_mat[subnum][num].get()) for num in range(len(main_mat[0]))] for subnum in
                    range(len(main_mat))]
    final_determinant = det.det_calc(final_matrix)
    lbl.config(text=f'\u0394={final_determinant}')

# Setting the value in matrix

dtr_button = Button(frm1, text='Determinant', command=row_col_number, font=('Lucida Fax', 15), bg='#e7540e', fg='white',
                    border=2)
dtr_button.grid(row=0, column=1, pady=5, ipadx=70, columnspan=3)
buttonHover(dtr_button, '#e7540e', '#e7680e')

###########################################################################################
p = []
q = []

matrix1 = []
matrix2 = []

def closer():
    global matrix1, matrix2, p, q
    matrix1 = []
    matrix2 = []
    p = q = []
    root4.destroy()


# For matrix addition
def matrixOperation(type):
    global root4
    root4 = Tk()
    root4.title('Matrix Value Input')
    frm_add = Frame(root4)
    frm_add.pack()
    row = Label(frm_add, text='Enter number of rows   :')
    row.grid(row=0, column=0, pady=(5, 5))
    row_num = Entry(frm_add, width=10)
    row_num.grid(row=0, column=1, padx=(0, 5), columnspan=5)
    col = Label(frm_add, text='Enter number of columns:')
    col.grid(row=1, column=0, pady=(0, 5))
    col_num = Entry(frm_add, width=10)
    col_num.grid(row=1, column=1, padx=(0, 5), columnspan=5)

    def matrixSetter(r, c):
        set_btn.destroy()
        frm_add_2 = Frame(root4)
        frm_add_2.pack()
        global p, q
        p = []
        q = []
        table1 = LabelFrame(frm_add_2, text='Matrix-1', font=('Roboto', 10))
        table1.grid(row=3, column=0, pady=(0, 5))
        table2 = LabelFrame(frm_add_2, text='Matrix-2', font=('Roboto', 10))
        table2.grid(row=4, column=0, pady=(0, 0))
        for j in range(int(r)):
            for i in range(int(c)):
                Label(table1, text=f"C{i + 1}").grid(row=0, column=i + 1)
                e1 = Entry(table1, width=6)
                e1.grid(row=j + 1, column=i + 1, padx=1, pady=1)
                p.append(e1)
            Label(table1, text=f"R{j + 1}").grid(row=j + 1, column=0)
            matrix1.append(p)
            p = []
        for j in range(int(r)):
            for i in range(int(c)):
                Label(table2, text=f"C{i + 1}").grid(row=0, column=i + 1)
                e1 = Entry(table2, width=6)
                e1.grid(row=j + 1, column=i + 1, padx=1, pady=1)
                q.append(e1)
            Label(table2, text=f"R{j + 1}").grid(row=j + 1, column=0)
            matrix2.append(q)
            q = []
        global calc_button
        calc_button = Button(frm_add_2, text='Calculate', command=lambda: matrixmanipulation(r, c), bg='black',
                             fg='white')
        calc_button.grid(row=5, column=0, ipadx=100, pady=5)

        def matrixmanipulation(r, c):
            mat = []
            if type == 'add':

                mat = [[int(matrix1[n][m].get()) + int(matrix2[n][m].get()) for m in range(len(matrix1[0]))] for n in
                       range(len(matrix2))]
                result_frm = LabelFrame(frm_add_2, text='Added Matrix')
                result_frm.grid(row=6, column=0)
            elif type == 'sub':

                mat = [[int(matrix1[n][m].get()) - int(matrix2[n][m].get()) for m in range(len(matrix1[0]))] for n
                       in
                       range(len(matrix2))]
                result_frm = LabelFrame(frm_add_2, text='Added Matrix')
                result_frm.grid(row=6, column=0)
            for j in range(int(r)):
                for i in range(int(c)):
                    Label(result_frm, text=f"C{i + 1}").grid(row=0, column=i + 1)
                    e1 = Entry(result_frm, width=6)
                    e1.grid(row=j + 1, column=i + 1, padx=1, pady=1)
                    e1.insert(END, mat[j][i])

                Label(result_frm, text=f"R{j + 1}").grid(row=j + 1, column=0)
            calc_button['state'] = DISABLED
            Button(root4, text='Close', font=global_font, bg='black', fg='white', command=closer).pack()

    set_btn = Button(frm_add, text='Set Matrix', font=('Consolas', 12),
                     command=lambda: matrixSetter(row_num.get(), col_num.get()))
    set_btn.grid(row=2, column=1, ipadx=10, columnspan=1)


def matrix_multiplication():
    global root4
    root4 = Tk()
    root4.title('Matrix Multiplication Input')
    frm_add = Frame(root4)
    frm_add.pack()
    matrix1_frm = LabelFrame(frm_add, text='MATRIX1')
    matrix1_frm.pack()
    row1 = Label(matrix1_frm, text='Enter number of rows   :')
    row1.grid(row=0, column=0, pady=5)
    row_num1 = Entry(matrix1_frm, width=10)
    row_num1.grid(row=0, column=1, padx=(0, 5), columnspan=5)
    col1 = Label(matrix1_frm, text='Enter number of columns:')
    col1.grid(row=1, column=0, pady=(0, 5))
    col_num1 = Entry(matrix1_frm, width=10)
    col_num1.grid(row=1, column=1, padx=(0, 5), columnspan=5)
    # For second matrix
    matrix2_frm = LabelFrame(frm_add, text='MATRIX2')
    matrix2_frm.pack(pady=(10))
    row2 = Label(matrix2_frm, text='Enter number of rows   :')
    row2.grid(row=0, column=0, pady=5)
    row_num2 = Entry(matrix2_frm, width=10)
    row_num2.grid(row=0, column=1, padx=(0, 5), columnspan=5)
    col2 = Label(matrix2_frm, text='Enter number of columns:')
    col2.grid(row=1, column=0, pady=(0, 5))
    col_num2 = Entry(matrix2_frm, width=10)
    col_num2.grid(row=1, column=1, padx=(0, 5), columnspan=5)

    def set_multiply_matrix(r1, c1, r2, c2):
        set_btn.destroy()
        global p, q
        p = []
        q = []
        frm_add_2 = Frame(root4)
        frm_add_2.pack()
        table1 = LabelFrame(frm_add_2, text='Matrix-1', font=('Roboto', 10))
        table1.grid(row=3, column=0, pady=(0, 5))
        table2 = LabelFrame(frm_add_2, text='Matrix-2', font=('Roboto', 10))
        table2.grid(row=4, column=0, pady=0)

        for j in range(int(r1)):
            for i in range(int(c1)):
                Label(table1, text=f"C{i + 1}").grid(row=0, column=i + 1)
                e1 = Entry(table1, width=6)
                e1.grid(row=j + 1, column=i + 1, padx=1, pady=1)
                p.append(e1)

            Label(table1, text=f"R{j + 1}").grid(row=j + 1, column=0)

            matrix1.append(p)
            p = []
        for j in range(int(r2)):
            for i in range(int(c2)):
                Label(table2, text=f"C{i + 1}").grid(row=0, column=i + 1)
                e1 = Entry(table2, width=6)
                e1.grid(row=j + 1, column=i + 1, padx=1, pady=1)
                q.append(e1)
            Label(table2, text=f"R{j + 1}").grid(row=j + 1, column=0)
            matrix2.append(q)
            q = []
            global calc_button

        def matrix_result(r, c):

            result = [[0 for _ in range(c)] for _ in range(r)]

            for m in range(len(matrix1)):
                for n in range(len(matrix2[0])):
                    for o in range(len(matrix2)):
                        result[m][n] += int(matrix1[m][o].get()) * int(matrix2[o][n].get())
            result_frm = LabelFrame(frm_add_2, text='Multiplied Matrix')
            result_frm.grid(row=6, column=0)

            for j in range(int(r)):

                for i in range(int(c)):
                    Label(result_frm, text=f"C{i + 1}").grid(row=0, column=i + 1)
                    e1 = Entry(result_frm, width=6)
                    e1.grid(row=j + 1, column=i + 1, padx=1, pady=1)
                    e1.insert(END, result[j][i])
                Label(result_frm, text=f"R{j + 1}").grid(row=j + 1, column=0)

            calc_button['state'] = DISABLED
            Button(root4, text='Close', font=global_font, bg='black', fg='white', command=closer).pack()

        calc_button = Button(frm_add_2, text='Calculate', command=lambda: matrix_result(int(r1), int(c2)))
        calc_button.grid(row=5, column=0, pady=5)

    set_btn = Button(frm_add, text='Set Matrix', font=('Consolas', 12),
                     command=lambda: set_multiply_matrix(row_num1.get(), col_num1.get(), row_num2.get(),
                                                         col_num2.get()))
    set_btn.pack(pady=10)


def matrix_transpose():
    global matrix1, root4
    matrix1 = []
    root4 = Tk()
    root4.title('Matrix Transpose Input')
    frm_add = Frame(root4)
    frm_add.pack()
    row = Label(frm_add, text='Enter number of rows   :')
    row.grid(row=0, column=0, pady=5)
    row_num = Entry(frm_add, width=10)
    row_num.grid(row=0, column=1, padx=(0, 5), columnspan=5)
    col = Label(frm_add, text='Enter number of columns:')
    col.grid(row=1, column=0, pady=(0, 5))
    col_num = Entry(frm_add, width=10)
    col_num.grid(row=1, column=1, padx=(0, 5), columnspan=5)

    def transpose_matrix_set(r, c):

        set_btn.destroy()
        global p
        p = []
        frm_add_2 = Frame(root4)
        frm_add_2.pack()
        table1 = LabelFrame(frm_add_2, text='Matrix-1', font=('Roboto', 10))
        table1.grid(row=3, column=0, pady=(0, 5))
        for j in range(int(r)):
            for i in range(int(c)):
                Label(table1, text=f"C{i + 1}").grid(row=0, column=i + 1)
                e1 = Entry(table1, width=6)
                e1.grid(row=j + 1, column=i + 1, padx=1, pady=1)
                p.append(e1)

            Label(table1, text=f"R{j + 1}").grid(row=j + 1, column=0)
            matrix1.append(p)
            p = []
            global calc_button
        calc_button = Button(frm_add_2, text='Calculate', command=lambda: matrix_result(int(r), int(c)))
        calc_button.grid(row=5, column=0, pady=(5, 5))

        def matrix_result(r, c):
            calc_button.destroy()
            result = [[matrix1[i][j].get() for i in range(r)] for j in range(c)]
            result_frm = LabelFrame(frm_add_2, text='Transpose Matrix')
            result_frm.grid(row=6, column=0)

            for j in range(int(c)):
                for i in range(int(r)):
                    Label(result_frm, text=f"C{i + 1}").grid(row=0, column=i + 1)
                    e1 = Entry(result_frm, width=6)
                    e1.grid(row=j + 1, column=i + 1, padx=1, pady=1)
                    e1.insert(END, result[j][i])
                Label(result_frm, text=f"R{j + 1}").grid(row=j + 1, column=0)
            Button(root4, text='Close', font=global_font, bg='black', fg='white', command=closer).pack()

    set_btn = Button(frm_add, text='Set Matrix', font=('Consolas', 12),
                     command=lambda: transpose_matrix_set(row_num.get(), col_num.get()))
    set_btn.grid(row=2, column=1, ipadx=10, columnspan=1)


def matrix_operation():
    frm3 = LabelFrame(frm2, text='Matrix Operation', bg='#363636', fg='white')
    frm3.grid(row=1, column=1)
    mat_add_btn = Button(frm3, text='Addition', font=('Consolas', 10), command=lambda: matrixOperation('add'),
                         bg='#007979',
                         fg='white')

    mat_add_btn.pack(pady=(5, 0), ipadx=61, padx=5)
    mat_sub_btn = Button(frm3, text='Substraction', font=('Consolas', 10), command=lambda: matrixOperation('sub'),
                         bg='#007979', fg='white')
    mat_sub_btn.pack(pady=5, ipadx=47)
    mat_mul_btn = Button(frm3, text='Multiplication', font=('Consolas', 10), bg='#007979', fg='white',
                         command=matrix_multiplication)
    mat_mul_btn.pack(pady=(0, 5), ipadx=40)
    mat_trans_btn = Button(frm3, text='Transpose  ', font=('Consolas', 10), bg='#007979', fg='white',
                           command=matrix_transpose)
    mat_trans_btn.pack(pady=(0, 5), ipadx=50)
    
    buttonHover(mat_add_btn, '#007979', '#008879')
    buttonHover(mat_sub_btn, '#007979', '#008879')
    buttonHover(mat_mul_btn, '#007979', '#008879')
    buttonHover(mat_trans_btn, '#007979', '#008879')


mat_button = Button(frm2, text='Matrix', bg='#e7540e', fg='white', font=('Lucida Fax', 15), command=matrix_operation,
                    border=2)
mat_button.grid(row=0, column=0, pady=5, ipadx=90, columnspan=3)
buttonHover(mat_button, '#e7540e', '#e7640e')
direction = ['i', 'j', 'k']


def VectorProduct(type):
    root5 = Tk()
    root5.title('Vector Entry')

    def CrossProductResult():
        vectorResultFrm = LabelFrame(root5, text='Result')
        vectorResultFrm.pack(pady=10, padx=10)
        vijk = [int(ventry[0][1].get()) * int(ventry[1][2].get()) - int(ventry[1][1].get()) * int(ventry[0][2].get()),
                int(ventry[1][0].get()) * int(ventry[0][2].get()) - int(ventry[0][0].get()) * int(ventry[1][2].get()),
                int(ventry[0][0].get()) * int(ventry[1][1].get()) - int(ventry[0][1].get()) * int(ventry[1][0].get())]
        resultVectorlbl = Label(vectorResultFrm, text='Resultant Vector')
        resultVectorlbl.grid(row=0, column=0, padx=5, pady=10)
        for c in range(3):
            e = Entry(vectorResultFrm, width=5, justify=CENTER, font=('Lato', 10))
            e.grid(row=0, column=2 * c + 1, padx=2)
            e.insert(0, str(vijk[c]))
            Label(vectorResultFrm, text=direction[c]).grid(row=0, column=2 * c + 2)

    def DotProductResult():
        vijk = int(ventry[0][0].get()) * int(ventry[1][0].get()) + int(ventry[0][1].get()) * int(
            ventry[1][1].get()) + int(ventry[0][2].get()) \
               * int(ventry[1][2].get())
        vectorResultFrm = LabelFrame(root5, text='Result')
        vectorResultFrm.pack(pady=10, padx=10)
        ansLabel = Label(vectorResultFrm, text=f'Dot Product = {vijk}', font=('Roboto', 13))
        ansLabel.grid(row=0, column=0, padx=5, pady=10)

    ventry = []
    vector_subentries = []
    vectorEntryFrame = LabelFrame(root5, text='Value Input')
    vectorEntryFrame.pack(pady=10, padx=10)
    vector1Label = Label(vectorEntryFrame, text='Vector1:', font=global_font)
    vector1Label.grid(row=0, column=0)
    vector2Label = Label(vectorEntryFrame, text='Vector2:', font=global_font)
    vector2Label.grid(row=1, column=0)

    for i in range(2):
        for j in range(3):
            e = Entry(vectorEntryFrame, width=5, justify=CENTER, font=('Lato', 10))
            e.grid(row=i, column=2 * j + 1, padx=2)
            vector_subentries.append(e)
            Label(vectorEntryFrame, text=direction[j]).grid(row=i, column=2 * j + 2)
        ventry.append(vector_subentries)
        vector_subentries = []
    if type == 'crx':
        calc_button = Button(vectorEntryFrame, text='Calculate', command=CrossProductResult)
        calc_button.grid(row=2, column=1, columnspan=4, pady=10)
    else:
        calc_button = Button(vectorEntryFrame, text='Calculate', command=DotProductResult)
        calc_button.grid(row=2, column=1, columnspan=4, pady=10)


VectorButton = Button(frmVector, text='Crx-Product', bg='#e7540e', fg='white', font=('Lucida Fax', 15),
                      command=lambda: VectorProduct('crx'))
VectorButton.grid(row=0, column=0, pady=5, ipadx=60, columnspan=3)
buttonHover(VectorButton, '#e7540e', '#e7640e')

DotProdButton = Button(frmVector, text='Dot-Product', bg='#e7540e', fg='white', font=('Lucida Fax', 15),
                       command=lambda: VectorProduct('dot'))
DotProdButton.grid(row=1, column=0, pady=5, ipadx=60, columnspan=3)
buttonHover(DotProdButton, '#e7540e', '#e7640e')
close = Button(root, text='Close', bg='black', fg='white', font=('Fixedsys', 15), command=root.destroy, border=0)
close.grid(row=3, column=0, columnspan=2, ipadx=30, pady=5)
buttonHover(close, 'black', '#212121')
mainloop()
