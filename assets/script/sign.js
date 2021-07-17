const persianNumbers = [/۰/g, /۱/g, /۲/g, /۳/g, /۴/g, /۵/g, /۶/g, /۷/g, /۸/g, /۹/g];
const englishNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

let firstname = document.getElementById("name");
let lastname = document.getElementById("lastname");
let password = document.getElementById("pass");
let email = document.getElementById("email");
let address = document.getElementById("address");
const maxChar = 255;
const maxAddr = 1000;
function fixNumbers(str) {
    if (typeof str === 'string') {
        for (var i = 0; i < 10; i++) {
            str = str.replace(persianNumbers[i], i).replace(englishNumbers[i], i);
        }
    }
    return str;
};

function validateNullField(value, err, msg) {
    if (value == "") {
        err.innerText = msg + ' خالی است';
        return false;
    }

    return true;
}

function validate(errID, value, errTopic, maxCharNum, regex) {
    const err = document.getElementById(errID);
    err.innerText = "";
    let isValid = validateNullField(value, err, errTopic);
    if (isValid && value.length >= maxCharNum) {
        err.innerText = "طول کارکترها زیاد است";
        isValid = false;
    }

    if (isValid && regex && !regex.test(value)) {
        isValid = false;
        err.innerText = errTopic + " نامعتبر است";
    }
    return isValid;
}

function validateEmail() {
    const reg = new RegExp("[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$");
    const valid = validate("emailerror", email.value.trim(), "ایمیل", maxChar, reg);
    email.style.borderColor = valid ? 'green' : 'red';
    return valid;
}

function validatePassword() {
    const reg = new RegExp("^(?=.*[0-9]+.*)(?=.*[a-zA-Z]+.*)[0-9a-zA-Z]{8,255}$");
    const valid = validate("passworderror", fixNumbers(password.value), "رمز عبور", maxChar, reg);
    password.style.borderColor = valid ? 'green' : 'red';
    return valid;
}

function validateInPassword() {
    const valid = validate("passworderror", fixNumbers(password.value), "رمز عبور", maxChar);
    password.style.borderColor = valid ? 'green' : 'red';
    return valid;
}

function validateName() {
    const valid = validate("nameerror", firstname.value.trim(), "نام", maxChar);
    firstname.style.borderColor = valid ? 'green' : 'red';
    return valid;
}

function validateLastName() {
    const valid = validate("lastnameerror", lastname.value.trim(), "نام خانوادگی", maxChar);
    lastname.style.borderColor = valid ? 'green' : 'red';
    return valid;
}

function validateAddr() {
    const valid = validate("addresserror", address.value, "آدرس", maxAddr);
    address.style.borderColor = valid ? 'green' : 'red';
    return valid;
}

function checkFinalUpValidation() {
    const addrValid = validateAddr();
    const nameValid = validateName();
    const lastnameValid = validateLastName();
    const passwordValid = validatePassword();
    const emailValid = validateEmail();
    return addrValid & nameValid & lastnameValid & passwordValid & emailValid;
}

function checkFinalInValidation() {
    const passwordValid = validateInPassword();
    const emailValid = validateEmail();
    return passwordValid & emailValid;
}

