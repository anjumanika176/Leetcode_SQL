class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        #Three simple dictionaries, one value per table name
        self.col_count = {}  #how many columns each table has 
        self.next_id = {}     #the id the next new role will get
        self.rows = {}        #the rows of each table 

        for i in range(len(names)):
            name = names[i]
            self.col_count[name] = columns[i]
            self.next_id[name] = 1
            self.rows[name] = [] 

    def ins(self, name, row):
            # 1.Does this table exists?
            if name not in self.rows:
                return False

            # 2.Does the row have the right number of columns?
            if len(row) != self.col_count[name]:
                return False

            # 3.Save the row together with its id
            new_id = self.next_id[name]
            self.rows[name].append([new_id, row])

            # 4.Next row gets a bigger id (this never goes back down)
            self.next_id[name] = new_id + 1
            return True

    def rmv(self, name, rowId):
            if name in self.rows:
                self.rows[name] = [r for r in self.rows[name] if r[0] != rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
            if name not in self.rows:
                return "<null>"


        #Column must be between i and the number of columns
            if columnId < 1 or columnId > self.col_count[name]:
                return "<null>"

        
            for item in self.rows[name]:
                if item[0] == rowId:
                    return item[1][columnId - 1]    
            return "<null>"

    def exp(self, name):
        result = []
        if name not in self.rows:
            return result
        for item in self.rows[name]:
            line = str(item[0])
            for v in item[1]:
                line = line + "," + v
            result.append(line)
        return result   
