from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray


class SistemasRelas:
    def __init__(self):
        self.reglas = []
        self.hechos = set()
        self.carga_reglas()

    def carga_reglas(self):
        # definicion de reglas
        self.reglas = [
            {
                'condiciones':['fiebre','dolor_cabeza','dolor_muscular'],
                'conclusiones': 'posible_gripe'
            },
            {
                'condiciones': ['fiebre','dolor_garganta','ganglios_inflamados'],
                'conclusiones': 'posible_amigdalitris'
            },
            {
                'condiciones':['tos_seca','dificultad_respiratoria','fiebre'],
                'conclusiones': 'posible_branquitis'
            },
            {
                'condiciones':['dolor_abdominal','nauseas','fiebre'],
                'conclsuines': 'posibles_gastrointeritis'
            },
            {
                'condiciones':['posible_gripe','dificultad_respirar'],
                'conclusiones':'urgencia_medica'
            }
        ]

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)
        print(f"Hecho agregado:{hecho}")

    def encadenamiento_hacia_adelante(self):
        nuevas_conclusiones = True

        while nuevas_conclusiones:
            nuevas_conclusiones = False

            for regla in self.reglas:
                #verificar si todas las condiciones cumplen
                if all(condicion in self.hechos for condicion in regla['condiciones']):
                    conclusion = regla['conclusion']

                    #si la conclusion no esta en los hechos, agregarla
                    if conclusion not in self.hechos:
                        self.hechos.add(conclusion)
                        print(f"Regla aplicada: {regla['condiciones']} -> {conclusion}")
                        nuevas_conclusiones = True
        return self.hechos

    def mostrar_diagnostico(self):
        print("\n" + "="*50)
        print("DIAGNOSTICO FINAL")
        print("="*50)

        #Filtro clave (clasificacion de los hechos)
        enfermedades = [h for h in self.hechos if h.startswitch('posible_')]
        urgencias = [h for h in self.hechos if h.startswitch('urgencia_')]

        if enfermedades:
            print("Condiciones identificadas:")
            for enfermedad in enfermedades:
                print(f"    -{enfermedad.replace('posible_','').replace('_','').title()}")

        if urgencias:
            print("\n ALERTAS")
            for urgencia in urgencias:
               print(f" -{urgencia.replace('urgencia_','').replace('_','').title()}")

        if not enfermedades and not urgencias:
            print("No se identificaron condiciones especificas")

# simulacion
def practica_sistema_reglas():
    print("SISTEMA EXPERTO MEDICO BASICO")
    print("="*40)

    sistema = SistemasRelas()

    sintomas_disponibles = [
        'fiebre', 'dolor_cabeza', 'dolor_muscular', 'dolor_garganta',
        'ganglios_inflamados','tos_seca','dificultad_respiratoria',
        'dolor_abdominal','nauseas'
    ]

    print("\nSelecciona los sintomas presentes (ingresa el numero):")
    for i, sintoma in enumerate(sintomas_disponibles, 1):
        print(f"{i}. {sintoma.replace('_', '').title()}")

    print("0. Finalizar Seleccion")

    while True:
        try:
            opcion = int(input("\nOpcion:"))
            if opcion == 0:
                break
            elif 1 <= opcion <=len(sintomas_disponibles):
                sintoma = sintomas_disponibles[opcion-1]
                sistema.agregar_hecho(sintoma)
            else:
                print("Opcion invalida")
        except ValueError:
            print("Por favor ingresa un numero valido")
    print("\n" + "="*40)
    print("PROCESANDO REGLAS")
    print("="*40)

    sistema.encadenamiento_hacia_adelante()
    sistema.mostrar_diagnostico()

if __name__ == "__main__":
    practica_sistema_reglas()