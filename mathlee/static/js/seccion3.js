const div_elements = document.getElementsByClassName("temas");
const cb_elements = document.getElementsByClassName("cbTopic");

for(var i = 0; i<div_elements.length; i++){
    div_elements.item(i).style.visibility = 'hidden';
}

for(var i = 0; i<cb_elements.length; i++){
    cb_elements.item(i).setAttribute("number", i);
    cb_elements.item(i).addEventListener('change', e => {
        if(e.target.checked === true) {
            for(var o = 0; o<div_elements.length;o++){
                if(!(cb_elements.item(o) === e.target)){
                    div_elements.item(o).style.transition = 'none';
                    cb_elements.item(o).checked = false;
                    div_elements.item(o).style.visibility = 'hidden';
                    div_elements.item(o).style.transition = 'height .2s, background-color .2s';
                }
            }
            div_elements.item(e.target.getAttribute("number")).style.visibility = 'visible';
        }
        if(e.target.checked === false) {
            setTimeout(() => {
                div_elements.item(e.target.getAttribute("number")).style.visibility = 'hidden';
            }, 200);
       }
    });
}

AOS.init();