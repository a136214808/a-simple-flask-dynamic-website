
    window.onload = function () {
    document.getElementById("password1").onchange = validatePassword;
    document.getElementById("password2").onchange = validatePassword;
    document.getElementById("Name").onchange = validateName;
    document.getElementByName("Email").onchange = validateEmail;

}

    function validatePassword() {
    var pass2 = document.getElementById("password2").value;
    var pass1 = document.getElementById("password1").value;
    if (pass1 !== pass2)
    document.getElementById("password2").setCustomValidity("Passwords Don't Match");
    else
    document.getElementById("password2").setCustomValidity('');
}

    function validateName() {
    var name = document.getElementById("Name").value;
    if (name.length<1)
    document.getElementById("Name").setCustomValidity("Your name is too short");
    else
    document.getElementById("Name").setCustomValidity('');
}

    function validateEmail() {
        var email = document.getElementsByName("Email").value;
        if ('@'.includes(email)) {
            document.getElementById("Name").setCustomValidity("");
        } else {
            document.getElementById("password2").setCustomValidity('please input correct email');
        }
    }




