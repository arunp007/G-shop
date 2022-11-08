function validation(){
    var status = 1
    var name = document.getElementById('name')
    var email = document.getElementById('email')
    var phone = document.getElementById('phone')
    var address = document.getElementById('address')
    var pass = document.getElementById('password')

    if(name.value == ""){
        document.getElementById('name').style.borderColor="red"
        document.getElementById('name_error').innerHTML="** Please Enter Your Name **"
        document.getElementById('name_error').style.color="red"
        document.getElementById('name_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('name').style.color="black"
        document.getElementById('name_error').style.display="none"
        var status = 1
    }

    if(email.value == ""){
        document.getElementById('email').style.borderColor="red"
        document.getElementById('email_error').innerHTML="** Please Enter Your Email Id **"
        document.getElementById('email_error').style.color="red"
        document.getElementById('email_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('email').style.color="black"
        document.getElementById('email_error').style.display="none"
        var status = 1
    }

    if(phone.value == ""){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter Your Phone Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('phone').style.borderColor="black"
        document.getElementById('email_error').style.display="none"
        var status = 1
    }

    if(address.value == ""){
        document.getElementById('address').style.borderColor="red"
        document.getElementById('address_error').innerHTML="** Please Enter Your Permanent Address **"
        document.getElementById('address_error').style.color="red"
        document.getElementById('address_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('address').style.borderColor="black"
        document.getElementById('address_error').style.display="none"
        var status = 1
    }

    if(pass.value == ""){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Please Enter Your Password **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('password').style.borderColor="black"
        document.getElementById('password_error').style.display="none"
        var status = 1
    }

    if(status == 0){
        return false;
    }

    if(status == 1){
        return true;
    }

}

function valid_name(){
    var name = document.getElementById('name').value

    if(isNaN(name)){
        document.getElementById('name').style.borderColor="black"
        document.getElementById('name_error').style.display="none"
    }

    else{
        document.getElementById('name').style.borderColor="red"
        document.getElementById('name_error').innerHTML="** Enter A Valid Name **"
        document.getElementById('name_error').style.color="red"
        document.getElementById('name_error').style.display="block"
    }
}

function valid_email(){
    var email = document.getElementById('email').value

    if(isNaN(email)){
        document.getElementById('email').style.borderColor="black"
        document.getElementById('email_error').style.display="none"
    }

    else{
        document.getElementById('email').style.borderColor="red"
        document.getElementById('email_error').innerHTML="** Enter A Valid Email Id **"
        document.getElementById('email_error').style.color="red"
        document.getElementById('email_error').style.display="block"
    }

    if(email.length == 5){
        document.getElementById('email').style.borderColor="red"
        document.getElementById('email_error').innerHTML="** Email Id Must End With @gmail.com **"
        document.getElementById('email_error').style.color="red"
        document.getElementById('email_error').style.display="block"
    }
}

function valid_phone(){
    var phone = document.getElementById('phone').value

    if(isNaN(phone)){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter A Valid Phone Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    else{
        document.getElementById('phone').style.borderColor="black"
        document.getElementById('phone_error').style.display="none"
    }

    if(phone.length == 5){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Phone Number Must Have 10 digits **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length == 10){
        document.getElementById('phone').style.borderColor="green"
        document.getElementById('phone_error').innerHTML="** Perfect Phone Number **"
        document.getElementById('phone_error').style.color="green"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length > 10){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter A Valid Phone Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }
}

function valid_address(){
    var address = document.getElementById('address').value

    if(isNaN(address)){
        document.getElementById('address').style.borderColor="black"
        document.getElementById('address_error').style.display="none"
    }

    else{
        document.getElementById('address').style.borderColor="red"
        document.getElementById('address_error').innerHTML="** Please Enter A Valid Address **"
        document.getElementById('address_error').style.color="red"
        document.getElementById('address_error').style.display="block"
    }
}

function valid_password(){
    var pass = document.getElementById('password').value

    if(pass.length < 8){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Password Must Have 8 Characters **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block"
    }

    if(pass.length == 8){
        document.getElementById('password').style.borderColor="green"
        document.getElementById('password_error').innerHTML="** Perfect Password **"
        document.getElementById('password_error').style.color="green"
        document.getElementById('password_error').style.display="block"
    }

    if(pass.length > 8){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Please Enter A Valid Password **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block"
    }
}