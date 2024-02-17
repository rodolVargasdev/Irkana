from config.wsgi import *
from core.erp.models import Types

#Listar

#select * from Tabla

query = Types.objects.all()
print(query)

# insercion

t = Types

# edicicion

try:
    t = Types.objects.get(pk=1)
    t.name = 'accionista'
    t.save()
except Exception as e:
    print(e)    

# Eliminacion
t = Types.objects.get(pk=1)
t.delete()
