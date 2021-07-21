const dropBtnText = document.getElementById("dropBtnText");
const signInBtn = document.getElementById("signin");
const dropBtn = document.getElementById("dropbtn");
const profileBtn = document.getElementById("profileBtn");


if (localStorage.getItem('name')) {
    signInBtn.style.display = 'none';
    dropBtn.style.display = 'block'
    dropBtnText.innerText = localStorage.getItem('name')
} else {
    signInBtn.style.display = 'block';
    dropBtn.style.display = 'none'
}
console.log('here');

function profileBtnClick() {
    console.log('heloooooooooooooo');
    location.href = '../frontend/userProfile.html';
}

// console.log(profileBtnClick())

