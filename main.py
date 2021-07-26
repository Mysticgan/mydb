import json
import pathlib

class Table:

    def __init__(self):
        self.table = {}
        self.rows = []
        self.columns = []

    def add_row(self,id):
        if id in self.rows:
            raise Exception("Row Id already exists")
        self.table[id] = dict((key,"") for key in self.columns)
        self.rows.append(id)

    def add_columns(self,id):
        if id in self.columns:
            raise Exception("Column Id already exists")
        for i in self.rows:
            self.table[i][id] = ""
        self.columns.append(id)

    def get_value(self,row_id,column_id):
        return self.table[row_id][column_id]

    def set_value(self,row_id,column_id,value):
        self.table[row_id][column_id]=value

    def remove_row(self,id):
        self.table.pop(id)
        self.rows.remove(id)

    def remove_column(self,id):
        for i in self.table:
            self.table[i].pop(id)
        self.columns.remove(id)

    def rename_row(self,old_id,new_id):
        if new_id in self.rows:
            raise Exception("Row Id already exists")
        self.table[new_id] = self.table.pop(old_id)
        self.rows.remove(old_id)
        self.rows.append(new_id)
    
    def rename_column(self,old_id,new_id):
        if new_id in self.columns:
            raise Exception("Column Id already exists")
        for i in self.table:
            self.table[i][new_id] = self.table[i].pop(old_id)
        self.columns.remove(old_id)
        self.columns.append(new_id)
        pass

    def display_table(self,width=10):
        tabledata=[[self.table[i][j] for j in self.table[i]]for i in self.table]
        output=[]
        for col in self.columns:
            if len(col)<=width:
                output.append(col.ljust(width))
            else:
                output.append(str(col[:width-3]+"...").ljust(width))
        
        decor,heading="",""
        for i in output:
            heading += i+"|"
            decor += "-"*(len(i))+"+"
        decor = "+"+decor
        heading="|"+heading
        print(decor,heading,decor,sep="\n")

        for num,row in enumerate(tabledata):
            output=[]
            for col in row:
                if len(col)<=width:
                    output.append(col.ljust(width))
                else:
                    output.append(str(col[:width-3]+"...").ljust(width))
                
            disp=""
            for i in output:
                disp += i+"|"
            print("|"+disp)
        print(decor)


    def read_json(self,file_location,silent_confirm=False):
        file_path = pathlib.Path(file_location)
        if not file_path.is_file():
            raise Exception("NO FILE FOUND")
        if file_path.suffix != ".json":
            raise Exception("Please use JSON Format")
        if not silent_confirm:
            if str(input("Reading from the json file overwrites the current table\nDO YOU WANT TO PROCEED(YES/NO) > ")).lower() != 'yes':
                return
        read_file = open(file_path,'r')
        self.table = json.load(read_file)
        read_file.close()
        del read_file

        self.rows = [i for i in self.table]
        self.columns = [i for i in self.table[self.rows[0]]]

    def write_json(self,file_location,silent_confirm=False):
        file_path = pathlib.Path(file_location)
        if not file_path.is_file():
            if not silent_confirm:
                if str(input("The file you specified doesnt exist\ndo you want to create a new file(yes\no) > ")).lower() != 'yes':
                    return
            write_file = open(file_path,'w')
            json.dump({},write_file)
            write_file.close()
            del write_file
        if not silent_confirm:
            if str(input("Writing the json file overwrites contents of the file\nDO YOU WANT TO PROCEED(YES/NO) > ")).lower() != 'yes':
                return
        write_file = open(file_path,'w')
        json.dump(self.table,write_file)
        write_file.close()
        del write_file

if __name__ == '__main__':
    pass

# this part is to test the code it can be removed

    test = Table()
    test.add_columns("before col 1")
    test.add_columns("before col 2")

    test.add_row("before row 1")
    test.add_row("before row 2")

    test.set_value("before row 1","before col 1","1")
    test.set_value("before row 1","before col 2","2")
    test.set_value("before row 2","before col 1","3")
    test.set_value("before row 2","before col 2","4")

    test.display_table(20)
    print("\n\n")

    test.rename_row("before row 1","after row 1")

    test.display_table(20)
    print("\n\n")

    test.rename_column("before col 1","after col 1")

    test.display_table(20)
    print("\n\n")
