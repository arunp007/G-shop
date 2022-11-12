function validation(){
    var status = 1
    var image = document.getElementById('image')
    var name = document.getElementById('name')
    var description = document.getElementById('description')
    var price = document.getElementById('price')

    if(image.value == ""){
        document.getElementById('image').style.borderColor="red"
        document.getElementById('image_error').innerHTML="** Upload Image **"
        document.getElementById('image_error').style.color="red"
        document.getElementById('image_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('image').style.borderColor="black"
        document.getElementById('image_error').style.display="none"
        var status = 1
    }

    if(name.value == ""){
        document.getElementById('name').style.borderColor="red"
        document.getElementById('name_error').innerHTML="** Enter Your Name **"
        document.getElementById('name_error').style.color="red"
        document.getElementById('name_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('name').style.borderColor="black"
        document.getElementById('name_error').style.display="none"
        var status = 1
    }

    if(description.value == ""){
        document.getElementById('description').style.borderColor="red"
        document.getElementById('description_error').innerHTML="** Enter Your Description **"
        document.getElementById('description_error').style.color="red"
        document.getElementById('description_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('description').style.borderColor="black"
        document.getElementById('description_error').style.display="none"
        var status = 1
    }

    if(price.value == ""){
        document.getElementById('price').style.borderColor="red"
        document.getElementById('price_error').innerHTML="** Enter Your Description **"
        document.getElementById('price_error').style.color="red"
        document.getElementById('price_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('price').style.borderColor="black"
        document.getElementById('price_error').style.display="none"
        var status = 1
    }

    if(status == 0){
        return false;
    }

    if(status == 1){
        return true;
    }
}