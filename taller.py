from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave):
        pass

  class ReglaValidacionGanimedes(ReglaValidacion):
      def contiene_caracter_especial(self, clave):
          especiales = '@_#$%'
          return any(c in especiales for c in clave)

      def es_valida(self, clave):
          if not self._validar_longitud(clave):
              raise ExcepcionLongitudInvalida()
          if not self._contiene_mayuscula(clave):
              raise ExcepcionMayusculaFaltante()
          if not self._contiene_minuscula(clave):
              raise ExcepcionMinusculaFaltante()
          if not self._contiene_numero(clave):
              raise ExcepcionNumeroFaltante()
          if not self.contiene_caracter_especial(clave):
              raise ExcepcionCaracterEspecialFaltante()
          return True

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        palabra = 'calisto'
        count = sum(1 for c in palabra if c in clave)
        if count >= 2 and not palabra.isupper():
            return True
        return False

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise ExcepcionLongitudInvalida()
        if not self._contiene_numero(clave):
            raise ExcepcionNumeroFaltante()
        if not self.contiene_calisto(clave):
            raise ExcepcionCalistoInvalida()
        return True


class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)


class ExcepcionLongitudInvalida(Exception):
    pass

class ExcepcionMayusculaFaltante(Exception):
    pass

class ExcepcionMinusculaFaltante(Exception):
    pass

class ExcepcionNumeroFaltante(Exception):
    pass

class ExcepcionCaracterEspecialFaltante(Exception):
    pass

class ExcepcionCalistoInvalida(Exception):
    pass
