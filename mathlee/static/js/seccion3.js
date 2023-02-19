/*const cb_1 = document.getElementById("cb-lvl1");
const cont_1 = document.getElementById("temas-1");

const cb_2 = document.getElementById("cb-lvl2");
const cont_2 = document.getElementById("temas-2");

const cb_3 = document.getElementById("cb-lvl3");
const cont_3 = document.getElementById("temas-3");

const cb_4 = document.getElementById("cb-lvl4");
const cont_4 = document.getElementById("temas-4");*/

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
                    console.log(cb_elements.item(o).checked);
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


/*cb_1.addEventListener('change', e => {
    if(e.target.checked === true) {
        if(cb_2.target.checked || cb_3.target.checked || cb_4.target.checked){
            cont_2.style.visibility = 'hidden';
            cont_3.style.visibility = 'hidden';
            cont_4.style.visibility = 'hidden';
        }
        cont_1.style.visibility = 'visible';
    }
    if(e.target.checked === false) {
        setTimeout(() => {
            cont_1.style.visibility = 'hidden';
        }, 200);
   }
});

cb_2.addEventListener('change', e => {
    if(e.target.checked === true) {
        cont_2.style.visibility = 'visible';
    }
    if(e.target.checked === false) {
        setTimeout(() => {
            cont_2.style.visibility = 'hidden';
        }, 200);
   }
});

cb_3.addEventListener('change', e => {
    if(e.target.checked === true) {
        cont_3.style.visibility = 'visible';
    }
    if(e.target.checked === false) {
        setTimeout(() => {
            cont_3.style.visibility = 'hidden';
        }, 200);
   }
});

cb_4.addEventListener('change', e => {
    if(e.target.checked === true) {
        cont_4.style.visibility = 'visible';
    }
    if(e.target.checked === false) {
        setTimeout(() => {
            cont_4.style.visibility = 'hidden';
        }, 200);
   }
});*/
