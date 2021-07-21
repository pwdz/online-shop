const pageCapacity = 15
var productInfos;
var productCell = document.getElementsByClassName("product")[0]
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

            createProductCells();
        }
        else {

        }
    } catch (error) {
        console.log(error);
    }
}
// productCell.inn
function createProductCells(){
    let productCells = []
    productCells.push(productCell)
    setProductCellValues(productCells[0], productInfos[0])
    for(let i=1; i<productInfos.length; i++){
        productCells[i] = productCell.cloneNode(true)
        setProductCellValues(productCells[i], productInfos[i])        
        productCell.parentNode.appendChild(productCells[i])
    }

    setupPageButtons();
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
}