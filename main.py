import json
import pathlib

class Table:

    def __init__(self):
        self.table = {}
        self.rows = []
        self.columns = []
        self.max_display_length=10

    def add_row(self,id):
        for i in self.rows:
            if id == i:
                raise Exception("Row Id already exists")
        self.table[id] = dict((key,"") for key in self.columns)
        self.rows.append(id)
        # if len(id)>self.maxlen:
        #     self.maxlen=len(id)+1

    def add_columns(self,id):
        for i in self.columns:
            if id == i:
                raise Exception("Column Id already exists")
        for i in self.rows:
            self.table[i][id] = ""
        self.columns.append(id)
        # if len(id)>self.maxlen:
        #     self.maxlen=len(id)+1

    def get_value(self,row_id,column_id):
        return self.table[row_id][column_id]

    def set_value(self,row_id,column_id,value):
        self.table[row_id][column_id]=value
        # if len(value)>self.maxlen:
        #     self.maxlen=len(value)+1

    def remove_row(self,id):
        self.table.pop(id)
        self.rows.remove(id)

    def remove_column(self,id):
        for i in self.table:
            self.table[i].pop(id)
        self.columns.remove(id)

    def display_table(self):
        tableData = [[self.table[i][j] for j in self.table[i]] for i in self.table]
        output=[]
        for col in self.columns:
            if len(col)<=self.max_display_length:
                output.append(col.ljust(self.max_display_length))
            else:
                dispstr = col[:self.max_display_length-3]+"..."
                output.append(dispstr.ljust(self.max_display_length))
        heading = "| "+" | ".join(output)+" |"
        print("_"*(len(heading)),heading,"_"*(len(heading)),sep="\n")
        
        for row in tableData:
            output = []
            for col in row:
                if len(col)<=self.max_display_length:
                    output.append(col.ljust(self.max_display_length))
                else:
                    dispstr = col[:self.max_display_length-3]+"..."
                    output.append(dispstr.ljust(self.max_display_length))
            rowdisp = "| "+" | ".join(output)+" |"
            print(rowdisp,"_"*(len(rowdisp)),sep="\n")

        del tableData,row,col,output,heading,rowdisp

    def read_json(self,file_location,silent_confirm=False):
        if not silent_confirm:
            if str(input("Reading from the json file overwrites the current table\nDO YOU WANT TO PROCEED(YES/NO) > ")).lower() != 'yes':
                return
        pass

    def write_json(self,file_location,silent_confirm=False):
        if not silent_confirm:
            if str(input("Writing the json file overwrites contents of the file\nDO YOU WANT TO PROCEED(YES/NO) > ")).lower() != 'yes':
                return
        pass


if __name__ == '__main__':
    
    pass

