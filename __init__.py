
class grizzlies:

  #  def __init__(self):

   #     self.fichero = None

    def leer_csv(self, doc):

            with open (doc, "r") as f:
                #csv = []
                #for linea in f:
                #    instancia = lineasplit(",")
                #results.append((instancia[0], instancia[1:]))

                csv = f.read()

            f.close()

            print("Csv leido")

            self.fichero = csv

            return

    def leer_json(self, doc):

        with open (doc, "r") as f:

            json = f.read()

        f.close()

        print("Json leido")

        self.fichero = json

        return



    def leer(self, doc):

        self.tipofich = doc[-1]

        if self.tipofich != "v" and self.tipofich != "n":

            raise ValueError("Tipo de fichero invalido")

        if self.tipofich == "v":

            return self.leer_csv(doc)

        return self.leer_json(doc)



   # def convertir_a_json(self):


   # def convertir_a_csv(self):








    def convertir(self):

        if self.tipofich == "v":

            return self.convertir_a_json()

        return self.convertir_a_csv()



    #def guardar(self):







if __name__ == "__main__":

    gz = grizzlies()

    #gz.leer("neo.csv")

    gz.leer("climate.json")

    gz.convertir()
