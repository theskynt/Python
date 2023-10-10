import datetime

class Note:
    _id = 1

    def __init__(self, memo, tags) :
        self._id = Note._id
        self._memo = memo
        self._creation_date = datetime.datetime.now().strftime("%d/%m/%y")
        self._tags = tags
        Note._id += 1

    @property #id
    def id(self):
        return self._id

    @property #memo
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, new_memo):
        if isinstance(new_memo, str):
            self._memo = new_memo
        else:
            print("Error")
            exit()

    @property #creation_date
    def creation_date(self):
        return self._creation_date

    @property #tags
    def tags(self):
        return self._tags
    @tags.setter
    def tags(self, new_tags):
        if isinstance(new_tags, list):
            self._tags = new_tags
        else:
            print("Error")
            exit()
    
    def match(self, search_filter):
        if isinstance(search_filter, str):
            if search_filter in self._memo  :
                return True
            for item in self._tags :
                if search_filter in item :
                    return True
                else:
                    return False
        else:
            print("Error")
            exit()

class Notebook :
    notes = []
    
    def search(self, search_filter):
        self.list_id = []
        if isinstance(search_filter, str):
            for notes in self.notes :
                if Note.match(notes, search_filter)  :
                    self.list_id.append(notes)
            return self.list_id
        else:
            print("Error")
            exit()

    def new_note(self, memo, tags):
        if isinstance( memo, str) and isinstance( tags, list):
            self.notes.append(Note(memo, tags))
        else:
            print("Error")
            exit()

    def modify_memo(self, note_id, memo):
        for notes in self.notes :
            if note_id == notes.id :
                notes.memo = memo
                break
            else:
                print("Error")
                exit()
    def modify_tags(self, note_id, tags):
        for notes in self.notes :
            if note_id == notes.id :
                notes.tags = tags
                break
            else:
                print("Error")
                exit()

class Memu :
    def __init__(self,notebook):
        self._notebook = notebook

    def show_gui(self):
        print('''=======Main Manu=======
1. Show note
2. Search note
3. Add note
4. Modify note
5. Modify tags
6. Exit
***********************''')
        input_number = int(input(">> Select menu 1-6 :"))
        match input_number :
            case 1 :
                self.show_note()
            case 2 :
                self.search_note()
            case 3 :
                self.add_note()
            case 4 :
                self.modify_note()
            case 5 :
                self.modify_tags()
            case 6 :
                exit()
            

    def show_note(self):
        print("***********************")
        for note in self._notebook.notes :
            print(f'''
        ID: {note.id}
        Memo: {note.memo}
        Tags: {note.tags}
        Create: {note.creation_date}''')
        input("**Please enter to exit**")

    def search_note(self):
        print("***********************")
        search = input("Search : ")
        search_notes = self._notebook.search(search)
        if len(search_notes) == 0:
            print("No Data in list")
        else :
            for data in search_notes :
                print(f'''
        ID: {data.id}
        Memo: {data.memo}
        Tags: {data.tags}
        Create: {data.creation_date}''')
        input("**Please enter to exit**")
        
    def add_note(self):
        print("***********************")
        memo = input("Memo : ")
        tags = [input("Tags : ")]
        self._notebook.new_note(memo,tags)

    def modify_note(self):
        print("***********************")
        note_id = int(input("ID : "))
        memo = input("New Memo : ")
        self._notebook.modify_memo(note_id,memo)

    def modify_tags(self):
        print("***********************")
        note_id = int(input("ID : "))
        tags = [input("New tags : ")]
        self._notebook.modify_tags(note_id,tags)
    


notebook01 = Notebook()
notebook01.new_note("ไปปลูกป่า",["ต้นไม้","รักโลก"])
notebook01.new_note("ไปว่ายน้ำ",["ว่ายน้ำ","ออกกำลังกาย"])
while True:
    menu01 = Memu(notebook01)
    menu01.show_gui()