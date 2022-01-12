// form errors //
const mailInput = document.querySelector(".left .user-info .input.mail input");
const mailError = document.querySelector(
    ".left .user-info .input.mail .error-msg"
);

const pwdInput = document.querySelector(".left .user-info .input.pwd input");

const logInButton = document.querySelector(".left .user-info .submit-box .log");

const formErrors = {
    mail: false,
    pwd: false,
};

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
    formErrors.pwd = e.target.value == "" ? false : true;
});
//  //

// active submit //
setInterval(() => {
    if (formErrors.mail == true && formErrors.pwd == true) {
        logInButton.classList.add("active");
    } else {
        logInButton.classList.remove("active");
    }
}, 500);
//  //

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
//  //

// Content writer //
let content =
    "if you want anything for sheep prices, or treading products with other peoples, this platform will help you to reach them . . .";

const contentContainer = document.querySelector(".log-in .right > .content");

let writingDelay = 100;
let endWritingDelay = 17000;
let lettersPointer = 0;

function writeLetter() {
    contentContainer.innerHTML += content[lettersPointer];
    lettersPointer++;

    if (lettersPointer == content.length) {
        setTimeout(() => {
            contentContainer.innerHTML = "";
            lettersPointer = 0;

            writeLetter();
        }, endWritingDelay);
    } else {
        let delay =
            content[lettersPointer] == " " ? writingDelay * 4 : writingDelay;

        setTimeout(() => {
            writeLetter();
        }, delay);
    }
}
writeLetter();
//  //
