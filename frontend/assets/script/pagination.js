const pageCapacity = 15
var pageNumber = 0

var productInfos;
var productCell = document.getElementsByClassName("product")[0]
var productCells = []

var nextPageBtn, prevPageBtn, numBtns;
get();
async function get(){
    try {

        let formBody = [];
        // for (const property in loginData) {
        //     const encodedKey = encodeURIComponent(property);
        //     const encodedValue = encodeURIComponent(loginData[property]);
        //     formBody.push(encodedKey + "=" + encodedValue);
        // }
        formBody = formBody.join("&");

        const res = await fetch('http://127.0.0.1:5000/products/list', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            }
            // body: formBody
        })
        const resData = await res.json()
        console.log(resData);
        if (resData.success) {
            console.log(resData.data)
            productInfos = resData.data

            initProductCells();
            setupPageButtons();
            disableBtn(prevPageBtn)
        }
        else {

        }
    } catch (error) {
        console.log(error);
    }
}
// productCell.inn
function initProductCells(){
    clearPage() 

    index = 0
    for(let i= pageNumber * pageCapacity; i<productInfos.length && i < (pageNumber + 1) * pageCapacity; i++){
        productCells[index] = productCell.cloneNode(true)
        setProductCellValues(productCells[index], productInfos[i])        
        productCell.parentNode.appendChild(productCells[index])
        index++
    }
} 
function updateProductCells(){
    clearPage()
    index = 0
    for(let i= pageNumber * pageCapacity; i<productInfos.length && i < (pageNumber + 1) * pageCapacity; i++){
        setProductCellValues(productCells[index], productInfos[i])        
        index++
    }
    console.log(productInfos.length, (pageNumber+1)*pageCapacity)
    if(pageNumber == 0){
        disableBtn(prevPageBtn)
    }else
        enableBtn(prevPageBtn)
    
    if(productInfos.length <= (pageNumber + 1) * pageCapacity ){
        disableBtn(nextPageBtn)
    }else
        enableBtn(nextPageBtn)
}
function disableBtn(btn){
    btn.disabled = true
}
function enableBtn(btn){
    btn.disabled = false
}
function setProductCellValues(productCell, productValues){
    productCell.getElementsByClassName("productName")[0].innerHTML = productValues['name']
    productCell.getElementsByClassName("productCat")[0].innerHTML = productValues['category']
    productCell.getElementsByClassName("priceNumber")[0].innerHTML = productValues['price']
    productCell.style.display = "flex";

    // productCell.getElementsByClassName("productImage")[0].innerHTML = productValues['image']
}

function setupPageButtons(){
    let paginationDivCell = document.getElementsByClassName("pagination")[0]
    paginationDiv = paginationDivCell.cloneNode(true)
    paginationDiv.style.display = "flex"
    paginationDivCell.parentNode.appendChild(paginationDiv)

    numBtns = paginationDiv.getElementsByClassName("paginationNumber")
    nextPageBtn = paginationDiv.getElementsByClassName("paginationR")[0]
    prevPageBtn = paginationDiv.getElementsByClassName("paginationL")[0]

    nextPageBtn.onclick = function(){
        console.log("SDSDS")
        nextPage()
    }

    console.log("wewewee", nextPageBtn)
    prevPageBtn.onclick = prevPage
    for(let i=0; i<numBtns.length; i++){
        numBtns[i].onclick = function(){
            loadPage(numBtns[i].innerHTML)
            turnBtnOff()
            selectBtn(numBtns[i])
            // numBtns[i].style.boxShadow = "0px 10px 10px rgba(0, 157, 255, 0.616)";
        }
    }
    selectBtn(numBtns[0])
    // numBtns[0].style.boxShadow = "0px 10px 10px rgba(0, 157, 255, 0.616)";
}

function selectBtn(btn){
    btn.style.backgroundColor = "rgb(0, 157, 255)"
}
function turnBtnOff(){
    for(let i=0; i<numBtns.length;i++){
        // numBtns[i].style.boxShadow = "0px 2px 2px rgba(0, 157, 255, 0.616)";
        numBtns[i].style.backgroundColor = "white";
    }
}
function clearPage(){
    for(let i=0; i<productCells.length; i++)
        productCells[i].style.display = ("none");
}
function nextPage(){
    if(productInfos.length > (pageNumber+1) * pageCapacity )
        pageNumber++
    updateProductCells()

    turnBtnOff()
    selectBtn(numBtns[pageNumber])
    // numBtns[pageNumber].style.boxShadow = "0px 10px 10px rgba(0, 157, 255, 0.616)";
}
function prevPage(){
    if(pageNumber > 0)
        pageNumber--
    updateProductCells()

    turnBtnOff()
    selectBtn(numBtns[pageNumber])
    // numBtns[pageNumber].style.boxShadow = "0px 10px 10px rgba(0, 157, 255, 0.616)";
}
function loadPage(n){
    pageNumber = n - 1
    updateProductCells()
}
