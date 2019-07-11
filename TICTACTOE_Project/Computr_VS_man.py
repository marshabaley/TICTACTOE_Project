import random

#GAME LISTS
Matriza = [["_","_","_"],["_","_","_"],["_","_","_"]]

ListRound = [1]
ListRange = [1]

#MATRIZA PRITING
for RowGroup in Matriza:
    print(RowGroup)

#START THE GAME
for RowGroup in ListRange:

    if 3 in ListRound:
        break

    try:
        #XO FUNCTION
        def XO(ROW_,COLUMN_,VALUE_):

            for RowGroup in Matriza:

                for Row in RowGroup:

                    #IN PUT DATA - ROW(1,2,3, OR 4) COLMN(1,2,3, OR 4) VALUE(x OR o)
                    row = ROW_
                    column = COLUMN_
                    value = VALUE_

                    #CHEEK IF VALUES ARE CORRECT
                    #if row in (1,2,3,4) and column in ((1,2,3,4)) and value in ("x","o"):
                    if row in (1, 2, 3) and column in (1, 2, 3) and value in ("x","o"):

                        Select_row = Matriza[row - 1]
                        Type_data = Select_row[column-1]

                        #UPDATE MATRIZA (x OR o)
                        if Type_data =="_":
                            Select_row[column - 1] = value


                        if Type_data =="x" or Type_data =="o" :
                            row = ROW_
                            column = COLUMN_
                            value = VALUE_

                        #ROW LISTS
                        ROW_A = Matriza[0]
                        ROW_B = Matriza[1]
                        ROW_C = Matriza[2]

                        #A COMBINATION OF WINS
                        Count_valuw_1 = [ROW_A[0], ROW_B[1], ROW_C[2]].count(value)
                        Count_valuw_2 = [ROW_C[2], ROW_A[1], ROW_B[0]].count(value)

                        Count_valuw_3 = [ROW_A[0], ROW_B[0], ROW_C[0]].count(value)
                        Count_valuw_4 = [ROW_A[1], ROW_B[1], ROW_C[1]].count(value)
                        Count_valuw_5 = [ROW_A[2], ROW_B[2], ROW_C[2]].count(value)

                        Count_valuw_6 = [ROW_A[0], ROW_A[1], ROW_A[2]].count(value)
                        Count_valuw_7 = [ROW_B[0], ROW_B[1], ROW_B[2]].count(value)
                        Count_valuw_8 = [ROW_C[0], ROW_C[1], ROW_C[2]].count(value)

            #CHEEK IF THERE IS WINNER IN MATRIZA
            if 3 in (Count_valuw_1, Count_valuw_2, Count_valuw_3, Count_valuw_4,
                     Count_valuw_5, Count_valuw_6, Count_valuw_7, Count_valuw_8):

                ListRound.append(3)
                print("PLAYER", value, "WIN")

            else:
                ListRound.append(1)
                ListRange.append(1)

        XO(int(input("Enter row:")), int(input("Enter culmun:")), input("Enter value:"))
        XO(random.choice([1, 2, 3]), random.choice([1, 2, 3]), random.choice(["x"]))

        # MATRIZA PRITING
        for RowGroup in Matriza:
            print(RowGroup)


    except:
        #ERROR DESCRIPTION
        print("YOU HAVE AN ERROR TYPING, TRY AGAIN")

    #CHEEK IF MATRIZA IS FULL
    if "_" not in (Matriza[0]) and "_" not in (Matriza[1]) and "_" not in (Matriza[2])and \
            3 not in ListRound:

        print(" ")
        print("THERE IS NO WINNER, START THE GAME AGAIN")
        break

print(" ")
print("----------------GAME OVER----------------")


