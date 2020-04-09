from flask import Flask, render_template,json,request,Markup
import json
from cnx import coneccion

app = Flask(__name__)

@app.route('/')
def main():
    c,con=coneccion()
    try:
        c.execute("SELECT * FROM cargo")
        con.commit()
        lista_objectos=[]
        filas = c.fetchall()
        ncargo=[]
        for fila in filas:
            ncargo.append({'id_cargo': fila[0],'cargo':fila[1]})
    except:
        con.rollback()

    return render_template('index.html',ncargo=ncargo)

    

#Con esta nueva funcion vamos a graficar un pie-chart utilizando plotly..

@app.route('/grafica',methods=['POST'])
def grafica():

    c,con=coneccion()
    _op=request.form['op']
    
    if _op=="mostrar_pie":
        try:
            c.execute("SELECT COUNT(*) AS DIABETICOS FROM base_datos WHERE FLAT_CLAS=1 AND GRUPO=-1")
            fd = c.fetchall()
            c.execute("SELECT COUNT(*) AS NO_DIABETICOS FROM base_datos WHERE FLAT_CLAS=1 AND GRUPO=1")
            fnd = c.fetchall()
        except:
            print ("No se pudo completar la consulta")
        d=fd[0][0]
        nd=fnd[0][0]    
        labels = ['DIABETICS','NON-DIABETICS']
        values = [d,nd]
        trace = Pie(labels=labels, values=values)
        my_plot_div=plot([trace],output_type='div')
        grafica=str(my_plot_div)
        return json.dumps(grafica)

#Con esta nueva funcion vamos procesar los datos..

@app.route('/proceso',methods=['POST'])
def proceso():
    c,con=coneccion()
    _op=request.form['op']
    if _op=="agregar":
        _nombres=request.form['nombres']
        _apellidoP=request.form['apellidoP']
        _apellidoM=request.form['apellidoM']
        _direccion=request.form['direccion']
        _id_cargo=request.form['id_cargo']
        if _nombres:
            try:
                c.execute("INSERT INTO trabajador (nombre,apellidoP,apellidoM,direccion,id_cargo) VALUES (%s,%s,%s,%s,%s)",(_nombres,_apellidoP,_apellidoM,_direccion,_id_cargo))
                con.commit()
                return "Bien echo"
            except:
                con.rollback()
                
    elif _op=="actualizar":
        _id_tra=request.form['id_tra']
        _nombres=request.form['nombres']
        _apellidoP=request.form['apellidoP']
        _apellidoM=request.form['apellidoM']
        _direccion=request.form['direccion']
        _id_cargo=request.form['id_cargo']
        if _nombres:
            try:
                nuevaCons=""" UPDATE trabajador
                SET nombre=%s,apellidoP=%s,apellidoM=%s,direccion=%s,id_cargo=%s
                WHERE id_tra = %s """
                data=(_nombres,_apellidoP,_apellidoM,_direccion,_id_cargo,_id_tra)
                #EJECUTAMOS DE NUEVO LA CLASIFICACION#
                c.execute(nuevaCons,data)
                con.commit()
                return "Bien echo"
            except:
                con.rollback()

    elif _op=="setar":
        try:
            _ID_IND=request.form['ID_IND']   
            lista_objectos=[]
            c.execute("SELECT * FROM trabajador WHERE id_tra="+str(_ID_IND)+"")
            con.commit()
            filas = c.fetchall()
            lista_objectos.append(filas[0])
            j=json.dumps(lista_objectos)
            return j
        except:
            con.rollback()
            print ("Error: No se pudo obtener la data")

    elif _op=="eliminar":
        try:
            _ID_IND=request.form['ID_IND']   
            c.execute("DELETE FROM trabajador WHERE id_tra="+str(_ID_IND)+"")
            con.commit()
            return "Bien echo"
        except:
            con.rollback()
            print ("Error: No se pudo obtener la data")


    else:
        try:
            c.execute("SELECT id_tra,nombre,CONCAT(`apellidoP`,' ',`apellidoM`) as apellidos, direccion, cargo.tipo_cargo FROM trabajador INNER JOIN cargo ON trabajador.id_cargo=cargo.id_cargo")
            con.commit()
            lista_objectos=[]
            filas = c.fetchall()
            for fila in filas:
                boton_setear="<a href='#' class='Boton supercorto' id='SETEAR' onclick=setear("+str(fila[0])+")><i class='icono izquierda fas fa-cog'></i></a>"
                boton_eliminar="<a href='#' class='Boton supercorto' id='ELIMINAR' onclick=eliminar("+str(fila[0])+")><i class='icono izquierda fas fa-trash'></i></a>"
                t=(fila[1],fila[2],fila[3],fila[4],boton_setear+"&nbsp"+boton_eliminar)
                lista_objectos.append(t)
            j=json.dumps(lista_objectos)
            return j
        except:
            print ("Error: No se pudo obtener la data")

    #con.close()



if __name__ == "__main__":
    app.run(debug=True)
