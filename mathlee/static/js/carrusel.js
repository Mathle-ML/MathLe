const cont_elements = document.getElementsByClassName("cont");
const left = document.getElementById("left");
const right = document.getElementById("right");
const left_label = document.getElementById("lft-lbl");
const right_label = document.getElementById("rgt-lbl");
const rpd = document.getElementById("rpd");

for(var i = 0; i<cont_elements.length; i++){
    if(i<(cont_elements.length - 1)){
        cont_elements.item(i).setAttribute("nxtCnt", cont_elements.item(i + 1).getAttribute("id"))
    }

    if(!(i === 0)){
        cont_elements.item(i).setAttribute("antCnt", cont_elements.item(i - 1).getAttribute("id"))
    }
}
for(var i = 0; i<cont_elements.length; i++){
    cont_elements.item(i).setAttribute("nmb", i);
    if(!(i === 0)){
        cont_elements.item(i).style.display = 'none';
    }else{
        var cnt = cont_elements.item(i);
        rpd.setAttribute("cntAct", cnt.getAttribute("id"));
    }
}

right_label.addEventListener('click', e =>{
    right_label.style.animation = 'boom .2s';
});

right.addEventListener('change', e =>{
    if(e.target.checked === true){
        e.target.checked = false;
        cnt = rpd.getAttribute("cntAct");
        const cntAct = document.getElementById(cnt);
        nxtCnt = document.getElementById(cntAct.getAttribute("nxtCnt"));
        if(!(nxtCnt === null)){
            cntAct.style.animation = 'anim-left-end .5s';
            setTimeout(() => {
                cntAct.style.display = 'none';
                nxtCnt.style.display = 'block';
                nxtCnt.style.animation = 'anim-left-start .5s';
                nxtCnt.style.opacity = '1';
            }, 400);
            rpd.setAttribute("cntAct", nxtCnt.getAttribute("id"));
        }else{
            nxtCnt = cont_elements.item(0);
            cntAct.style.animation = 'anim-left-end .5s';
            setTimeout(() => {
                cntAct.style.display = 'none';
                nxtCnt.style.display = 'block';
                nxtCnt.style.animation = 'anim-left-start .5s';
                nxtCnt.style.opacity = '1';
            }, 400);
            rpd.setAttribute("cntAct", "cont-1");
        }
    }
});

left.addEventListener('change', e =>{
    if(e.target.checked === true){
        e.target.checked = false;
        cnt = rpd.getAttribute("cntAct");
        const cntAct = document.getElementById(cnt);
        var antCnt = document.getElementById(cntAct.getAttribute("antCnt"));
        if(!(antCnt === null)){
            cntAct.style.animation = 'anim-right-end .5s';
            setTimeout(() => {
                cntAct.style.display = 'none';
                antCnt.style.display = 'block';
                antCnt.style.animation = 'anim-right-start .5s';
                antCnt.style.opacity = '1';
            }, 400);
            rpd.setAttribute("cntAct", antCnt.getAttribute("id"));
        }else{
            antCnt = cont_elements.item(cont_elements.length - 1);
            cntAct.style.animation = 'anim-right-end .5s';
            setTimeout(() => {
                cntAct.style.display = 'none';
                antCnt.style.display = 'block';
                antCnt.style.animation = 'anim-right-start .5s';
                antCnt.style.opacity = '1';
                rpd.setAttribute("cntAct", "cont-" + cont_elements.length);
            }, 400);
        }
    }
});