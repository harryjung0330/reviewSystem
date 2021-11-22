
let a, b;

function loginFetch(event) {
    event.preventDefault();
    const loginButton = document.querySelector("#loginButton");
    const userId = document.querySelector("#userLogInId");
    const psw = document.querySelector("#psw");

    //https://x0hwwevlc3.execute-api.us-east-2.amazonaws.com/dev/logIn
    fetch("https://x0hwwevlc3.execute-api.us-east-2.amazonaws.com/dev/logIn", {
        method: "POST",
        headers: {
            'content-type': 'application/x-www-form-urlencoded',
        },
        body: `userLogInId=${userId.value}&psw=${psw.value}`,
    })
    .then((response) => {
        a = response.json()
        a.then((res) => {
            b = res
            //console.log(b);
            if (b.resFlag === 1) {      // 로그인 실패
                alert(b.respondMsg);
            }
            else {  //로그인 성공
                alert(b.respondMsg);
                //loginButton.off(event);
                window.location.href = "#";     //홈 화면으로 리다이렉트 https://x0hwwevlc3.execute-api.us-east-2.amazonaws.com/dev
            }
        });
    })
    .catch(err => console.error(err));
}


function newUserFetch(event) {
    event.preventDefault();
    const name = document.querySelector("#name");
    const phoneNumb = document.querySelector("#phoneNumb");
    const socialSec = document.querySelector("#socialSec");
    const logInId = document.querySelector("#logInId");
    const psw = document.querySelector("#psw");
    const country = document.querySelector("#country");
    const city = document.querySelector("#city");
    const streetAddr = document.querySelector("#streetAddr");
    const detailAddr = document.querySelector("#detailAddr");
    const emailAddr = document.querySelector("#emailAddr");

    // action="https://x0hwwevlc3.execute-api.us-east-2.amazonaws.com/dev/user" method="POST"
    fetch("https://x0hwwevlc3.execute-api.us-east-2.amazonaws.com/dev/user", {
        method: "POST",
        headers: {
            'content-type': 'application/x-www-form-urlencoded',
        },
        body: `name=${name.value}&phoneNumb=${phoneNumb.value}&socialSec=${socialSec.value}&logInId=${logInId.value}&psw=${psw.value}&country=${country.value}&city=${city.value}&streetAddr=${streetAddr.value}&detailAddr=${detailAddr.value}&emailAddr=${emailAddr.value}`,
    })
    .then((response) => {
        a = response.json()
        a.then((res) => {
            b = res
            //console.log(b);
            if (b.resFlag === 1) {      // 회원가입 실패
                alert(b.respondMsg);
            }
            else {  //회원가입 성공
                alert(b.respondMsg);
                window.location.href = "https://x0hwwevlc3.execute-api.us-east-2.amazonaws.com/dev/logIn"; //login.html    //로그인 화면으로 리다이렉트
            }
        });
    })
    .catch(err => console.error(err));
}