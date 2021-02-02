
function onClick_register(emailAddr, phoneNumber, password, repeatPassword, city) {


  //step 1. check that city is selected
  if( !city.localeCompare("not_selected") ){ //if city == "not_selected"
    alert("도시를 선택해주세요");
    return 0;
  }

  //step 2. check that city is selected
  if(isEmailOverlap == true){
    alert(emailAddr + "은 이미 가입된 이메일주소입니다.");
    return 0;
  }

  //step 3. Check if the password and repeat password are the same
  if(password.localeCompare(repeatPassword)){  //if password != repeatPassword
    alert("비밀번호와 확인 비밀번호가 서로 다릅니다.");
    return 0;
  }

  //step 5. Create signup JSON Object
  var signupInfo        = new Array();
  var emailAddrObj      = new Object();
  var phoneNumberObj    = new Object();
  var passwordObj       = new Object();
  var repeatPasswordObj = new Object();
  var cityObj           = new Object();

  emailAddrObj.emailAddr           = emailAddr;
  phoneNumberObj.phoneNumber       = phoneNumber;
  passwordObj.password             = password;
  repeatPasswordObj.repeatPassword = repeatPassword;
  cityObj.city                    = city;

  signupInfo.push(emailAddrObj);
  signupInfo.push(phoneNumberObj);
  signupInfo.push(passwordObj);
  signupInfo.push(repeatPasswordObj);
  signupInfo.push(cityObj);

  var jsonSignUpInfo = JSON.stringify(signupInfo);
  alert(jsonSignUpInfo);

//step 4. Send signup request to REST API


  return 0;
}


function isEmailOverlap(emailAddr){


  return false;
}
