import json, csv

class grizzlies:


    def __init__(self):

        self.fichero = None

    def leer_csv(self, doc, delimitador = ","):

            lista_dicc = []


            with open(doc, encoding='utf-8') as csv_leer:

                csv_leido = csv.DictReader(csv_leer, delimiter = delimitador)


                for instancia in csv_leido:

                    lista_dicc.append(instancia)

                csv_leer.close()


            self.fichero = lista_dicc

            return

    def leer_json(self, doc):

        with open(doc, "r") as json_leer:


            filedata = json_leer.read()


        filedata = filedata.replace('[', '???')

        filedata = filedata.replace('{', '[')

        filedata = filedata.replace('???', '{')

        filedata = filedata.replace(']', '???')

        filedata = filedata.replace('}', ']')

        filedata = filedata.replace('???', '}')

        print(filedata)



        json_leido = json.load(filedata)





        self.fichero = json_leido

        print(self.fichero.items())

        return



    def leer(self, doc):

        self.tipofich = doc[-1]

        if self.tipofich != "v" and self.tipofich != "n":

            raise ValueError("Tipo de fichero invalido")

        if self.tipofich == "v":

            return self.leer_csv(doc)

        return self.leer_json(doc)



    def convertir_a_json(self):


        self.fichero = json.dumps(self.fichero, indent=4)



    def normalize_json(self, data: dict) -> dict:

        new_data = dict()
        for key, value in data.items():
            if not isinstance(value, dict):
                new_data[key] = value
            else:
                for k, v in value.items():
                    new_data[key + "_" + k] = v


        return new_data


    def convertir_a_csv(self):


        self.fichero = self.normalize_json(self.fichero)


        csv_columns = self.fichero.keys()


        csv_data = ",".join(csv_columns) + "\n"


        new_row = list()
        for col in csv_columns:
            new_row.append(str(self.fichero [col]))


        csv_data += ",".join(new_row) + "\n"


        self.fichero = csv_data

        print(self.fichero)

        return




    def convertir(self):

        if self.tipofich == "v":

            return self.convertir_a_json()

        return self.convertir_a_csv()



    def guardar_json(self, nombre_json):

        with open(nombre_json, 'w', encoding='utf-8') as json_obj:

            json_obj.write(self.fichero)

            print("Archivo guardado!")

            return


    def guardar_csv(self, nombre_csv):

        with open(nombre_csv, "w+", encoding = "utf-8") as f:
            f.write(str(self.fichero))

            print("Archivo guardado!")

        return



    def guardar(self, nombre_archivo):

        if self.tipofich == "v":

            return self.guardar_json(nombre_archivo)

        return self.guardar_csv(nombre_archivo)








if __name__ == "__main__":

    gz = grizzlies()


#    gz.leer("neo.csv")

 #   gz.convertir()

  #  gz.guardar("prueba.json")


    gz.leer("climate.json")

    gz.convertir()

    gz.guardar("prueba.csv")
