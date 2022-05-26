class Tarefa:
    # def __init__(self, path):
    #     import os
    #     print(os.getcwd())
    #     if path == 1:
    #         import os
    #         import sqlite3
    #         path = os.getcwd().replace("Saiat", "usertaskbase.db")
    #         # print(path)
    #         self.conn = sqlite3.connect(path)
    #
    #     else:
    import sqlite3
    conn = sqlite3.connect("usertaskbase.db")

    def inserir(self, nome, importancia, inicio, fim, duracao, data, subtarefa):
        C = self.conn.cursor()
        C.execute("INSERT INTO tarefa(nome, importancia, inicio, fim, duracao, data, subtarefa) "
                  "values(\'{}\',{},\'{}\',\'{}\',{},\'{}\',"
                  "\'{}\')".format(nome, importancia, inicio, fim, duracao, data, subtarefa))
        self.conn.commit()
        C.close()

    def abrir(self):
        C = self.conn.cursor()
        C.execute("SELECT * FROM tarefa")
        lista = []

        for i in C.fetchall():
            lista.append(i)
        C.close()

        return lista
