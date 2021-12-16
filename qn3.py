def encryption(msg, key):
    # key is no of rows
    rows = key
    # column is the length of message
    columns = len(msg)

    e_text = ""
    # matrix creation
    matrix = [[""for k in range(columns)] for l in range(rows)]
    # fillin in thetable
    for i in range(columns):
        row = i % key
        column = i

        # populate the matrix
        matrix[row][column] = msg[i]
    # concatenating the letters
    for p in range(rows):
        for q in range(columns):
          e_text += matrix[p][q]

    return e_text
   
e_msg = encryption("Plain text",2)
print(e_msg)

def decrepyt(e_msg,key):
    rows = key
    # column is the length of message
    columns = len(e_msg)

    d_text = ""
    # matrix creation
    matrix = [[""for k in range(columns)] for l in range(rows)]
    s_it = 0
    c_index = 0
    r_index = 0
    # generating array from decrypted
    while s_it < columns:
        if c_index>= columns:
            c_index = r_index+1
            r_index+=1
            
            
    # fillin in thetable
        # populate the matrix
        matrix[r_index][c_index] = e_msg[s_it]
        s_it +=1
        c_index += key
    print(matrix)
# reading the decyripted
    for i in range(columns):
        c_index = i
        r_index = i % key
        d_text += matrix[r_index][c_index]

    return d_text
    print(d_text)
print(decrepyt(e_msg,2))

        