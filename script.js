var c_code 
var fname
var lname
var mobile


function check()
{
    var select = document.getElementById('get');
    c_code = select.options[select.selectedIndex].value;
     fname=document.getElementById("fname").value.trim();
   lname=document.getElementById("lname").value.trim();
     mobile=document.getElementById("mob").value;
    if(c_code=='' || c_code=='choose')
    {
        document.getElementById("place").innerHTML="Country code cannot be empty";
        document.getElementById("place").style.color="red";  
    }
    else if(fname=="" || fname.trim()=='')
    {
    document.getElementById("place").innerHTML="First name cannot be empty";
    document.getElementById("place").style.color="red";
    }
    else if(lname=="" || lname.trim()=='')
    {
        document.getElementById("place").innerHTML="Last name cannot be empty";
        document.getElementById("place").style.color="red";
    }
    else
    {
    var reg=/^[1-9]\d{9}$/;
    if(reg.test(mobile)==false)
    {
    document.getElementById("place").innerHTML="Invalid mobile number";
    document.getElementById("place").style.color="red";
    }
    else{
      checkotp();
    }
   }
}

function checkotp()
{
    let prompt = document.getElementById('prompt');
    prompt.classList.add('active');
}
function verify()
{
    let prompt = document.getElementById('prompt');
    let otp1 = document.getElementById('otp1');
    let otp2 = document.getElementById('otp2');
let otp3 = document.getElementById('otp3');
let otp4 = document.getElementById('otp4');
let getotp = otp1.value+otp2.value+otp3.value+otp4.value;

let otp = "1234"; 
    if(getotp==otp)
    {
        link=`http://127.0.0.1:5500/signup?countryCode=${c_code}&mobileNum=${mobile}&firstName=${fname}&lastName=${lname}`
        console.log(link)
        var saveData = $.ajax({
    
            type: 'GET',
            url:link,
            success: function(resultData) { 
               if(resultData==1)
               {
                    document.location.href="create account.html";
               }
               else if(resultData==0)
               {
                   alert("User already exists")
               }
               else{
                   alert("Something went wrong")
               }
             }
        

      });






       
    }
else{
    document.getElementById("valid").innerHTML="Invalid OTP";
    document.getElementById("valid").style.color="red";
    setTimeout(() => {
        prompt.classList.remove('active');
        otp1.value='';
        otp2.value='';
        otp3.value='';
        otp4.value='';  
    }, 1000);
    
}

}