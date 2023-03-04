const div_elements = document.getElementsByClassName("options");
const cnt_elements = document.getElementsByClassName("dLCnt");
const optit_elements = document.getElementsByClassName("optTit");
const cb_elements = document.getElementsByClassName("cbTopic");
const contOpen = document.getElementById("cntOpen");

for(var i = 0; i<div_elements.length; i++){
    div_elements.item(i).style.visibility = 'hidden';
}

console.log(cnt_elements.length);

for(var i = 0; i<cnt_elements.length; i++){
    if(i === (cnt_elements.length - 1)){
        console.log("entro");
        cnt_elements.item(i).style.border = 'none';
    }
}

contOpen.addEventListener('change', e => {
    if(e.target.checked === true){

    }
});

for(var i = 0; i<cb_elements.length; i++){
    cb_elements.item(i).setAttribute("number", i);
    cb_elements.item(i).addEventListener('change', e => {
        if(e.target.checked === true) {
            console.clear();
            for(var o = 0; o<div_elements.length;o++){
                if(!(cb_elements.item(o) === e.target)){
                    div_elements.item(o).style.transition = 'none';
                    cb_elements.item(o).checked = false;
                    div_elements.item(o).style.visibility = 'hidden';
                    div_elements.item(o).style.transition = 'height .2s, background-color .2s';

                    optit_elements.item(o).style.paddingTop = '9%';
                    optit_elements.item(o).style.paddingBottom = '-9%';
                    optit_elements.item(o + 1).style.paddingTop = '9%';
                    optit_elements.item(o + 1).style.paddingBottom = '-9%';
                    cnt_elements.item(o).style.height = '15%';
                    cnt_elements.item(o + 1).style.height = '15%';
                    cnt_elements.item(o).style.transform = 'translatey(130%)';
                    console.log("cambiado");
                    console.log(cnt_elements.item(o));
                }else{
                    console.log("principal");
                    console.log(cnt_elements.item(o));
                    contOpen.checked = true;
                    cnt_elements.item(o).style.height = '19.87%';
                    cnt_elements.item(o).style.transform = 'none';
                    optit_elements.item(o).style.paddingTop = '12%';
                    optit_elements.item(o).style.paddingBottom = '-12%';
                    if(!(o === 0)){
                        for(var s = 0; s<o; s++){
                            cnt_elements.item(s).style.height = '15%';
                            cnt_elements.item(s).style.transform = 'none';
                        }
                    }
                }
            }
            div_elements.item(e.target.getAttribute("number")).style.visibility = 'visible';
        }
        if(e.target.checked === false) {
            setTimeout(() => {
                div_elements.item(e.target.getAttribute("number")).style.visibility = 'hidden';
                div_elements.item(e.target.getAttribute("number")).style.opacity = '0';
            }, 200);
       }
    });
}