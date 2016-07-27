#  VALORES DE INGRESO

valorPlaca = input("Ingrese su placa: ") 
fecha1 = input("Ingrese la fecha: ")
hora1 = input("Ingrese la hora: 'HH:mm:ss' ")

# CLASE PARA OBTENER EL ULTIMO DIGITO PLACA

class DigitoPlaca:
	def inicializar(self,placas):
		ud=placas[-1:]
		return(ud)

# CLASE PARA OBTENER EL DIA

class ObternerFecha:
	def fechas(self,fecha):
		import datetime, locale
		locale.setlocale(locale.LC_ALL, "")
		str(fecha)
		dia = datetime.datetime.strptime(fecha, '%d-%m-%Y').strftime('El dia es: %A')
		return(dia)


#		CLASE PARA VALIDAR HORA

class ObtenerHora:
	def horas(self,hora):
		horas = hora[:2]
		minutos = hora[3:5]
		a = int(horas)
		b = int (minutos)
		c = a*60
		minutosumados = c + b
		if minutosumados >= 420 and minutosumados <=570:
			respuesta = "No puede salir";
			return(respuesta)
		elif minutosumados >= 960 and minutosumados >= 1170:
			respuesta = "No puede salir";
			return(respuesta)
		else:
			respuesta = "Si puede salir";
			return(respuesta)

	
# MAIN


placa= DigitoPlaca()
a=placa.inicializar(valorPlaca)


fecha2= ObternerFecha()
b=fecha2.fechas(fecha1)


hora2 = ObtenerHora()
rs=hora2.horas(hora1)


if (a == '2' or a == '1') and (b == 'lunes'):
	hora2 = ObtenerHora()
	rs=hora2.horas(hora1)
	print (rs)
elif (a == '3' or a == '4') and (b == 'martes'):
	hora2 = ObtenerHora()
	rs=hora2.horas(hora1)
	print (rs)
elif (a == '5' or a == '6') and (b == 'miercoles'):
	hora2 = ObtenerHora()
	rs=hora2.horas(hora1)
	print (rs)
elif (a == '7' or a == '8') and (b == 'jueves'):
	hora2 = ObtenerHora()
	rs=hora2.horas(hora1)
	print (rs)
elif (a == '9' or a == '0') and (b == 'viernes'):
	hora2 = ObtenerHora()
	rs=hora2.horas(hora1)
	print (rs)	
else:
	print ('Si Puede Salir')
	
	