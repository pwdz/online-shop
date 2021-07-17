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

// When the user clicks on <span> (x), close the modal
function clickSpanBtn() {
    modal.style.animationName = "fadeOut_Modal";
    modalContent.style.animationName = "fadeOut_Container";
    modal.addEventListener('animationend', animationEndCallback);
    // modal.style.display = "none";

}

animationEndCallback = (e) => {
    modal.style.display = "none";
}