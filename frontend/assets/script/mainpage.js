const dropBtnText = document.getElementById("dropBtnText");
const signInBtn = document.getElementById("signin");
const dropBtn = document.getElementById("dropbtn");



if (localStorage.getItem('name')) {
    signInBtn.style.display = 'none';
    dropBtn.style.display = 'block'
    dropBtnText.innerText = localStorage.getItem('name')
} else {
    signInBtn.style.display = 'block';
    dropBtn.style.display = 'none'
}

function profileBtnClick() {
    console.log(localStorage.getItem('name'));
    if (localStorage.getItem('name') == 'ادمین') {
        location.href = '../frontend/profileReceiptAdmin.html';
    } else {
        location.href = '../frontend/userProfile.html';
    }

}

function logoutBtnClick() {
    localStorage.clear()
    location.href = '../frontend/index.html';
}

function mainPageSignBtnClick() {
    location.href = '../frontend/signin.html';
}



// console.log(profileBtnClick())

