var leftTabBtn = document.getElementsByClassName("leftTab")[0];
var middleTabBtn = document.getElementsByClassName("middleTab")[0];
var rightTabBtn = document.getElementsByClassName("rightTab")[0];

const rightTabDiv = document.getElementsByClassName("tabRec")[0];
const middleTabDiv = document.getElementsByClassName("tabCat")[0];
const leftTabDiv = document.getElementsByClassName("tabProd")[0];

var currTab = rightTabDiv
var currBtn = rightTabBtn
console.log(":|", leftTabBtn, middleTabBtn, rightTabBtn)
leftTabBtn.onclick = function(){
    if(currTab != leftTabDiv){
        switchTab(currTab, leftTabDiv, currBtn, leftTabBtn);
        currTab = leftTabDiv;
        currBtn = leftTabBtn
    }
}
middleTabBtn.onclick = function(){
    if(currTab != middleTabDiv){
        switchTab(currTab, middleTabDiv, currBtn, middleTabBtn);
        currTab = middleTabDiv
        currBtn = middleTabBtn
    }
}
rightTabBtn.onclick = function(){
    console.log("lol", currTab, rightTabDiv)
    if(currTab != rightTabDiv){
        switchTab(currTab, rightTabDiv, currBtn, rightTabBtn);
        currTab = rightTabDiv
        currBtn = rightTabBtn
    }
}

function switchTab(currTab, newTab, pressedBtn, releasedBtn){

    currTab.style.display = "none";
    newTab.style.display = "flex";

    releasedBtn.style.backgroundColor = "rgb(238, 238, 238)";
    releasedBtn.style.color = "rgb(54, 54, 54)";

    pressedBtn.style.backgroundColor = "rgb(247, 247, 247)";
    pressedBtn.style.color = "rgb(159, 163, 167)";
}
