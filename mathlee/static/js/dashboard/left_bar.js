//Lista de menus extendibles
const div_elements = document.getElementsByClassName("menuExtendible");

//Lista de checkbox's
const cb_elements = document.getElementsByClassName("cbInput");

//Iniciacion de atributos
for(var i = 0; i<div_elements.length; i++){
    cb_elements.item(i).setAttribute('toV', 1);
    cb_elements.item(i).setAttribute("number", i);
}

//Añado los listener a los checkbox
for(var i = 0; i<cb_elements.length; i++){
    cb_elements.item(i).addEventListener('change', e => {

        //Elimino el timeout que tenia para añadirle mas
        clearTimeout(e.target.getAttribute('toV'));
        
        //Si esta seleccionado
        if(e.target.checked === true) {

            //Itera y revisa si no es el mismo
            for(var o = 0; o<div_elements.length;o++){
                if(!(cb_elements.item(o) === e.target)){
                    div_elements.item(o).style.transition = 'none';
                    cb_elements.item(o).checked = false;
                    div_elements.item(o).style.visibility = 'hidden';
                    div_elements.item(o).style.transition = 'height .2s';
                }else{
                    //Lo hace visible si es el que esta seleccionado
                    div_elements.item(o).style.visibility = 'visible';
                }

            }
        }

        //Despues de deseleccionar lo oculta, agrega un timeout con una id "h" como referencia
        if(e.target.checked === false) {
            h = setTimeout(() => {
                div_elements.item(e.target.getAttribute("number")).style.visibility = 'hidden';
            }, 300);
            e.target.setAttribute('toV', h);
       }
    });
}