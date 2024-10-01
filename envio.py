

class Envio:

    def __init__(self, codigo, direccion, tipo, pago):
        self.codigo = codigo
        self.direccion = direccion
        self.tipo = tipo
        self.pago = pago

    def __str__(self):
        cad = ('Código postal: {:<10} | Direccion: {:<20} | Pais: {:<12} '
               '| Tipo de envio: {:<2} | Forma de pago: {:<3} | Importe: {:<10}')
        cad = cad.format(self.codigo, self.direccion, self.country(), self.tipo,
                         self.pago, self.calcular_importe())
        return cad

    def country(self):
        cp = self.codigo
        n = len(cp)
        if n < 4 or n > 9:
            return 'Otro'

        # ¿es Argentina?
        if n == 8:
            if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
                return 'Argentina'
            else:
                return 'Otro'

        # ¿es Brasil?
        if n == 9:
            if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
                return 'Brasil'
            else:
                return 'Otro'

        if cp.isdigit():
            # ¿es Bolivia?
            if n == 4:
                return 'Bolivia'

            # ¿es Chile?
            if n == 7:
                return 'Chile'

            # ¿es Paraguay?
            if n == 6:
                return 'Paraguay'

            # ¿es Uruguay?
            if n == 5:
                return 'Uruguay'

        # ...si nada fue cierto, entonces sea lo que sea, es otro...
        return 'Otro'

    def check_dir(self):
        cl = cd = 0
        td = False
        ant = " "
        for car in self.direccion:
            if car in " .":
                # fin de palabra...
                # un flag si la palabra tenia todos sus caracteres digitos...
                if cl == cd:
                    td = True

                # resetear variables de uso parcial...
                cl = cd = 0
                ant = " "

            else:
                # en la panza de la palabra...
                # contar la cantidad de caracteres de la palabra actual...
                cl += 1

                # si el caracter no es digito ni letra, la direccion no es valida... salir con False...
                if not car.isdigit() and not car.isalpha():
                    return False

                # si hay dos mayusculas seguidas, la direccion no es valida... salir con False...
                if ant.isupper() and car.isupper():
                    return False

                # contar digitos para saber si hay alguna palabra compuesta solo por digitos...
                if car.isdigit():
                    cd += 1

                ant = car

        # si llegamos acá, es porque no había dos mayusculas seguidas y no habia caracteres raros...
        # ... por lo tanto, habria que salir con True a menos que no hubiese una palabra con todos digitos...
        return td

    def calcular_importe(self):
        cp = self.codigo
        pago = self.pago
        tipo = self.tipo
        destino = self.country()

        importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
        monto = importes[tipo]

        if destino == 'Argentina':
            inicial = monto
        else:
            if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
                inicial = int(monto * 1.20)
            elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
                inicial = int(monto * 1.25)
            elif destino == 'Brasil':
                if cp[0] == '8' or cp[0] == '9':
                    inicial = int(monto * 1.20)
                else:
                    if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                        inicial = int(monto * 1.25)
                    else:
                        inicial = int(monto * 1.30)
            else:
                inicial = int(monto * 1.50)

        # 4. Determinación del valor final del ticket a pagar.
        # asumimos que es pago en tarjeta...
        final = inicial

        # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
        if pago == 1:
            final = int(0.9 * inicial)

        return final


if __name__ == "__main__":
    e1 = Envio("98176-453", "Pele 2536.", 4, 2)
    p1 = e1.country()
    print("Pais:", p1)
    print("Direccion valida?:", e1.check_dir())
    print(e1)

    e2 = Envio("76543", "Independencia 374", 2, 1)
    print(e2)
