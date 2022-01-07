// form errors //
const firstInput = document.querySelector(
    ".left .input-form .input.first input"
);
const firstError = document.querySelector(
    ".left .input-form .input.first .error-msg"
);

const lastInput = document.querySelector(".left .input-form .input.last input");
const lastError = document.querySelector(
    ".left .input-form .input.last .error-msg"
);

const phoneInput = document.querySelector(
    ".left .input-form .input.phone input"
);
const phoneError = document.querySelector(
    ".left .input-form .input.phone .error-msg"
);

const mailInput = document.querySelector(".left .input-form .input.mail input");
const mailError = document.querySelector(
    ".left .input-form .input.mail .error-msg"
);

const pwdInput = document.querySelector(".left .input-form .input.pwd input");
const pwdError = document.querySelector(
    ".left .input-form .input.pwd .error-msg"
);

const pwdConfInput = document.querySelector(
    ".left .input-form .input.pwd-conf input"
);
const pwdConfError = document.querySelector(
    ".left .input-form .input.pwd-conf .error-msg"
);

const submitBtn = document.querySelector(".left .submit");

let formErrors = {
    first: false,
    last: false,
    phone: true,
    mail: false,
    pwd: false,
    pwdConf: false,
};

// first name //
firstInput.addEventListener("input", (e) => {
    let test = validName(e.target.value);

    if (test == true) {
        formErrors.first = true; // set first error //
        firstError.innerHTML = ""; // remove error msg //
    } else {
        formErrors.first = false; // set first error //

        if (test == "too long") {
            firstError.innerHTML = "First name too long"; // set the error msg //

            firstInput.value = firstInput.value.slice(0, 20);
        } else if (test == "invalid letter") {
            firstError.innerHTML =
                "First name must contain only letters and numbers"; // set the error msg //
        }
    }
});
//  //

// last name //
lastInput.addEventListener("input", (e) => {
    let test = validName(e.target.value);

    if (test == true) {
        formErrors.last = true; // set last error //
        lastError.innerHTML = ""; // remove error msg //
    } else {
        formErrors.last = false; // set last error //

        if (test == "too long") {
            lastError.innerHTML = "Last name too long"; // set the error msg //

            lastInput.value = lastInput.value.slice(0, 20);
        } else if (test == "invalid letter") {
            lastError.innerHTML =
                "Last name must contain only letters and numbers"; // set the error msg //
        }
    }
});
//  //

// mail //
mailInput.addEventListener("input", (e) => {
    let test = validMail(e.target.value);

    if (test == true) {
        formErrors.mail = true; // set mail error //
        mailError.innerHTML = ""; // remove error msg //
    } else {
        formErrors.mail = false; // set mail error //
        mailError.innerHTML = "Invalid Email address"; // set error msg //
    }
});
//  //

// pwd //
pwdInput.addEventListener("input", (e) => {
    pwdConfError.innerHTML = "";

    let test = validPwd(e.target.value);

    if (test == true) {
        formErrors.pwd = true; // set pwd error //
        pwdError.innerHTML = ""; // remove error msg //
    } else {
        formErrors.pwd = false; // set pwd error //

        if (test == "too short") {
            pwdError.innerHTML = "Password must contain at list 8 characters"; // set error msg //
        } else if (test == "need lower") {
            pwdError.innerHTML =
                "Password must have at list one Lowercase letter"; // set error msg //
        } else if (test == "need upper") {
            pwdError.innerHTML =
                "Password must have at list one Uppercase letter"; // set error msg //
        } else if (test == "need num") {
            pwdError.innerHTML = "Password must have at list one Number"; // set error msg //
        }
    }
});
//  //

// pwd confirm //
pwdConfInput.addEventListener("input", (e) => {
    if (e.target.value == pwdInput.value) {
        formErrors.pwdConf = true; // set pwdConf error //
        pwdConfError.innerHTML = ""; // remove error msg //
    } else {
        formErrors.pwdConf = false; // set pwdConf error //
        pwdConfError.innerHTML = "Password confirm not mach"; // set error msg //
    }
});
//  //

// submit button //
setInterval(() => {
    if (
        formErrors.first == true &&
        formErrors.last == true &&
        formErrors.phone == true &&
        formErrors.mail == true &&
        formErrors.pwd == true &&
        formErrors.pwdConf == true
    ) {
        submitBtn.classList.add("enable"); // enable the submit button //
    } else {
        submitBtn.classList.remove("enable"); // disable the submit button //
    }
}, 1000);
//  //

// validation functions //
function validName(name, nameLength = 20) {
    if (name.length > nameLength) {
        return "too long";
    }

    let test = true;
    for (let i = 0; i < name.length; i++) {
        let letterCode = name.charCodeAt(i);

        if (
            !(
                (
                    (letterCode >= 48 && letterCode <= 57) || // number //
                    (letterCode >= 65 && letterCode <= 90) || // uppercase letter //
                    (letterCode >= 97 && letterCode <= 122) || // lowercase letter //
                    letterCode == 32
                ) // spaces //
            )
        ) {
            test = "invalid letter";
            break;
        }
    }
    return test;
}

function validMail(mail) {
    let test = true;

    if (mail.includes("@")) {
        if (mail.includes(".")) {
            if (mail.indexOf("@") < mail.indexOf(".")) {
                let partOne = mail.split("@")[0];
                let partTow = mail.split("@")[1].split(".")[0];
                let partThree = mail.split("@")[1].split(".")[1];

                if (partOne != "" && !partOne.includes(" ")) {
                    if (partTow == "gmail") {
                        if (partThree == "com") {
                        } else {
                            test = false;
                        }
                    } else {
                        test = false;
                    }
                } else {
                    test = false;
                }
            } else {
                test = false;
            }
        } else {
            test = false;
        }
    } else {
        test = false;
    }

    return test;
}

function validPwd(pwd, minimumLength = 8) {
    if (pwd.length < minimumLength) {
        return "too short";
    }

    let haveLower = false;
    let haveUpper = false;
    let haveNum = false;

    for (let i = 0; i < pwd.length; i++) {
        let letterCode = pwd.charCodeAt(i);

        if (letterCode >= 97 && letterCode <= 122) {
            haveLower = true; // lower letter //
        }
        if (letterCode >= 65 && letterCode <= 90) {
            haveUpper = true; // uppercase letter //
        }
        if (letterCode >= 48 && letterCode <= 57) {
            haveNum = true; // number //
        }
    }

    if (!haveLower) {
        return "need lower";
    }
    if (!haveUpper) {
        return "need upper";
    }
    if (!haveNum) {
        return "need num";
    }

    return true;
}
//  //
//  //
