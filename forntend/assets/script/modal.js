const data = [
    {
        email: "rozhin@email.com",
        pass: "test12345"
    },
    {
        email: "rozhin1@email.com",
        pass: "test23456"
    },
    {
        email: "rozhin2@email.com",
        pass: "test34567"
    }
];


// Get the modal
const modal = document.getElementById("myModal");
const modalText = document.getElementById("contentText");
const modalContent = document.getElementById("modal-content");

// When the user clicks on the button, open the modal
function clickSignUpBtn() {
    const valid = checkFinalUpValidation();
    let text = "";
    let textColor = "black";
    if (!valid) {
        text = "اطلاعات وارد شده معتبر نمی باشد";
    } else {
        const emailCheck = data.map(v => v.email == email.value);
        if (emailCheck.includes(true)) {
            text = "ایمیل تکراری است";
        } else {
            text = "ثبت نام موفقیت آمیز است";
            textColor = "green";
        }
    }
    modalText.innerText = text;
    modalText.style.color = textColor;
    modalText.style.marginRight = "5%";
    modal.style.display = "block";

}

function clickSignInBtn() {
    const valid = checkFinalInValidation();
    let text = "";
    let textColor = "black";
    if (!valid) {
        text = "اطلاعات وارد شده معتبر نمی باشد";
    } else {
        const inputCheck = data.map(v => v.email == email.value && v.pass == fixNumbers(password.value));
        if (inputCheck.includes(true)) {
            text = "ورود موفقیت آمیز است";
            textColor = "green";
        } else {
            text = "اطلاعات وارد شده معتبر نمی باشد";

        }
    }
    modalText.innerText = text;
    modalText.style.color = textColor;
    modalText.style.marginRight = "5%";
    modal.style.display = "block";
}

function clickEditBtn() {
    const valid = checkFinalEditValidation();
    let text = "";
    let textColor = "black";
    if (!valid) {
        text = "اطلاعات وارد شده معتبر نمی باشد";
    } else {
        text = "ویرایش موفقیت آمیز است";
        textColor = "green";
    }
    modalText.innerText = text;
    modalText.style.color = textColor;
    modalText.style.marginRight = "5%";
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function clickSpanBtn() {
    console.log("hellooooo1");
    modal.style.animationName = "fadeOut_Modal";
    modalContent.style.animationName = "fadeOut_Container";
    modal.style.display = "none";
    modal.style.animationName = "fadeIn_Modal";
    modalContent.style.animationName = "fadeIn_Container";
    // console.log("hellooooo2");
    // new Promise((resolve, reject) => {
    //     modal.addEventListener('animationend', animationEndCallback, true);
    //     console.log("hollllllllllllllllllllla");
    //     resolve();
    // }).then(() => {
    //     console.log("kokokokokokokokooooooo");
    //     // modal.removeEventListener('animationend', animationEndCallback, true);
    //     // modal.style.display = "none";
    // })
    // console.log("hellooooo3");

}

// function animationEndCallback(e) {
//     console.log("hellooooo4");
//     // modal.style.display = "none";
//     modal.removeEventListener('animationend', undefined);
//     modal.style.animationName = "fadeIn_Modal";
//     modalContent.style.animationName = "fadeIn_Container";
//     modal.style.display = "none";
//     console.log("hellooooo5");
// }

window.onclick = function (event) {
    if (event.target == modal) {
        clickSpanBtn();
    }
}