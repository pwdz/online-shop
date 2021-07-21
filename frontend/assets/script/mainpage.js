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
    console.log("uhuhuhu");
    location.href = '../frontend/userProfile.html';
}

function logoutBtnClick() {
    console.log("hiiiiiiiiiiiiiiii");
    localStorage.clear()
    location.href = '../frontend/index.html';
}



// console.log(profileBtnClick())

