var leftTabBtns = document.getElementsByClassName("leftTab");
var rightTabBtns = document.getElementsByClassName("rightTab");

const firstTabDiv = document.getElementById("tab0");
const secondTabDiv = document.getElementById("tab1");

var currTab = firstTabDiv
for (let i=0; i < leftTabBtns.length; i++) {
    leftTabBtns[i].onclick = function(){
        if(currTab== firstTabDiv){
            // console.log("d" + currTabBtn + fir);
            switchTab(currTab, secondTabDiv, leftTabBtns, rightTabBtns);
            currTab = secondTabDiv;
        }
    }
    rightTabBtns[i].onclick = function(){
        if(currTab== secondTabDiv){
            switchTab(currTab, firstTabDiv, rightTabBtns, leftTabBtns);
            currTab = firstTabDiv;
        }
    }
    console.log("big big");
};

function switchTab(currTab, newTab, pressedBtns, releasedBtns){
    currTab.style.display = "none";
    newTab.style.display = "flex";
    for(let i=0; i<pressedBtns.length; i++){
        pressedBtns[i].style.backgroundColor = "rgb(238, 238, 238)";
        pressedBtns[i].style.color = "rgb(54, 54, 54)";

        releasedBtns[i].style.backgroundColor = "rgb(247, 247, 247)";
        releasedBtns[i].style.color = "rgb(238, 238, 238)";

    }
}