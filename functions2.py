#function object as a reference

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def define_row():
    print '+ - - - -',

def define_column():
        print '|        ',

def grid_row():
    define_row()
    print '+'

def grid_column():
    define_column()
    print '|'


def single_grid():
    grid_row()
    do_four(grid_column)
    grid_row()


def multiRow_grid(row):
    #print "Number of ROWS of grid are", row
    # if (row == 1):
    #        single_grid()
    # else:
    #     for x in range(row):
    #        single_grid()
    y = (row % 2)
    if (y == 0):
        for x in range (row / 2):
            do_twice(single_grid)
    else:
        for x in range(row):
            single_grid()

#multiRow_grid(2)

def multiColumn_grid(column):
    # print "Number of COLUMNS of grid are", column
    if (column==1):
        single_grid()

    else:
        for x in range(column):
            single_grid()



#multiColumn_grid(2)

# def multiRowAndColumn_grid(rows, columns):
#     print " Number of ROWS and COLUMNS in a grid are" , rows, " and ", columns
#     if (rows == columns):
#         for x in range (rows):
#             single_grid(),
#
#     else:
#         #print "Number of ROWS and COLUMNS are unequal"
#         #multiRow_grid(rows), multiColumn_grid(columns)
#         do_four(single_grid)
#
# multiRowAndColumn_grid(2, 1)


def drawLineA(width):

    print width * "+ - - - - " + "+"


def drawLineB(width):
    print width * "|         " + "|"

# def grid(width):
#     drawLineA(width)
#     drawLineB(width)
#     drawLineB(width)
#     drawLineB(width)
#     drawLineB(width)
#     drawLineA(width)


def grid(width, height):
    for x in range(width):
        drawLineA(height)
        drawLineB(height)
        drawLineB(height)
        drawLineB(height)
        drawLineB(height)
    drawLineA(height)

grid(1,7)