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
async function clickSignUpBtn() {
    const valid = checkFinalUpValidation();
    let text = "";
    let textColor = "black";
    if (!valid) {
        text = "اطلاعات وارد شده معتبر نمی باشد";
    } else {
        const registerData = getRegisterInput()
        let formBody = [];
        for (const property in registerData) {
            const encodedKey = encodeURIComponent(property);
            const encodedValue = encodeURIComponent(registerData[property]);
            formBody.push(encodedKey + "=" + encodedValue);
        }
        formBody = formBody.join("&");

        try {
            const res = await fetch('http://127.0.0.1:5000/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                },
                body: formBody
            })
            const resData = await res.json()
            console.log(resData);
            if (resData.success) {
                text = "ثبت نام موفقیت آمیز است";
                textColor = "green";
                console.log("he;llo");
                const resLoginData = await fetchLogin({ email: registerData.email, password: registerData.password })
                console.log(resLoginData);
                if (resLoginData.success) {
                    console.log(resLoginData);
                    localStorage.setItem('name', resLoginData.data.name)
                    localStorage.setItem('token', resLoginData.data.token)
                }

            }
            else {
                text = "اطلاعات وارد شده معتبر نمی باشد";

            }
        } catch (error) {
            console.log(error);
        }


        // const emailCheck = data.map(v => v.email == email.value);
        // if (emailCheck.includes(true)) {
        //     text = "ایمیل تکراری است";
        // } else {
        //     text = "ثبت نام موفقیت آمیز است";
        //     textColor = "green";
        // }
    }
    modalText.innerText = text;
    modalText.style.color = textColor;
    modalText.style.marginRight = "5%";
    modal.style.display = "block";

}

async function clickSignInBtn() {
    const valid = checkFinalInValidation();
    console.log(valid);
    let text = "";
    let textColor = "black";
    if (!valid) {
        text = "اطلاعات وارد شده معتبر نمی باشد";
    } else {
        // const inputCheck = data.map(v => v.email == email.value && v.pass == fixNumbers(password.value));
        // if (inputCheck.includes(true)) {
        try {
            const loginData = getLoginInput()
            const resData = await fetchLogin(loginData)
            console.log(resData);
            if (resData.success) {
                text = "ورود موفقیت آمیز است";
                textColor = "green";
                localStorage.setItem('name', resData.data.name)
                localStorage.setItem('token', resData.data.token)
            }
            else {
                text = "اطلاعات وارد شده معتبر نمی باشد";

            }
        } catch (error) {
            console.log(error);
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
    modal.style.animationName = "fadeOut_Modal";
    modalContent.style.animationName = "fadeOut_Container";
    modal.style.display = "none";
    modal.style.animationName = "fadeIn_Modal";
    modalContent.style.animationName = "fadeIn_Container";

    if (modalText.style.color == "green") {
        location.href = '../frontend/index.html';
    }

}

window.onclick = function (event) {
    if (event.target == modal) {
        clickSpanBtn();
    }
}

async function fetchLogin(loginData) {
    let formBody = [];
    for (const property in loginData) {
        const encodedKey = encodeURIComponent(property);
        const encodedValue = encodeURIComponent(loginData[property]);
        formBody.push(encodedKey + "=" + encodedValue);
    }
    formBody = formBody.join("&");
    console.log(formBody);
    const res = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        body: formBody
    })
    const resData = await res.json()
    return resData
}