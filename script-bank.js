
function validate()
{
    var select = document.getElementById('get');
    var mobile=document.getElementById("mob").value;;
    var c_code = select.options[select.selectedIndex].value;
    var fname=document.getElementById("fname").value.trim();
    var lname=document.getElementById("lname").value.trim();
    var dob=document.getElementById("dob").value.trim();
    var fatherName=document.getElementById("fatherName").value.trim();
    var paddress=document.getElementById("paddress").value.trim();
    var caddress=document.getElementById("caddress").value.trim();


    if(mobile=='' && fname=='' && lname==''&&fatherName==''&&paddress==''&&caddress=='')
    {
        alert("All fields are required")
    }
    else{
        link=`http://127.0.0.1:5500/createAccount?countryCode=${c_code}&mobileNum=${mobile}&firstName=${fname}&lastName=${lname}&fatherName=${fatherName}&dob=${dob}&permanentAddress=${paddress}&currentAddress=${caddress}`
        console.log(link)
        var saveData = $.ajax({
    
            type: 'GET',
            url:link,
            success: function(resultData) { 
                alert(resultData)

                document.location.href="index.html";
        
             }
        

      });
    }



}


