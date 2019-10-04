
function getInputs() {

var formData = new FormData();

var i3 = document.getElementById('loanLength');
var loanLength = i3.options[i3.selectedIndex].value;
formData.append('input', loanLength);

var i5 = document.getElementById('loanPurpose');
var loanPurpose = i5.options[i5.selectedIndex].value;
formData.append('input', loanPurpose);

var i6 = document.getElementById('loanSize');
var loanSize = i6.options[i6.selectedIndex].value;
formData.append('input', loanSize);

var i8 = document.getElementById('employmentHistory');
var employmentHistory = i8.options[i8.selectedIndex].value;
formData.append('input', employmentHistory);

var i9 = document.getElementById('cosignerCoborrower');
var cosignerCoborrower = i9.options[i9.selectedIndex].value;
formData.append('input', cosignerCoborrower);

var i10 = document.getElementById('age');
var age = i10.options[i10.selectedIndex].value;
formData.append('input', age);

var i12 = document.getElementById('homeowner');
var homeowner = i12.options[i12.selectedIndex].value;
formData.append('input', homeowner);

var i14 = document.getElementById('telephone');
var telephone = i14.options[i14.selectedIndex].value;
formData.append('input', telephone);

var i15 = document.getElementById('foreignWorker');
var foreignWorker = i15.options[i15.selectedIndex].value;
formData.append('input', foreignWorker);


if(document.getElementById("loanLength").value == "")
{
    document.getElementById("loanLength").focus();
}

if(document.getElementById("loanPurpose").value == "")
{

    document.getElementById("loanPurpose").focus();
}

if(document.getElementById("loanSize").value == "")
{
    alert("Please select a value");
    document.getElementById("loanSize").focus();
}

if(document.getElementById("employmentHistory").value == "")
{
    alert("Please select a value");
    document.getElementById("employmentHistory").focus();
}

if(document.getElementById("cosignerCoborrower").value == "")
{
    alert("Please select a value");
    document.getElementById("cosignerCoborrower").focus();
}

if(document.getElementById("age").value == "")
{
    alert("Please select a value");
    document.getElementById("age").focus();
}

if(document.getElementById("homeowner").value == "")
{
    alert("Please select a value");
    document.getElementById("homeowner").focus();
}

if(document.getElementById("telephone").value == "")
{
    alert("Please select a value");
    document.getElementById("telephone").focus();
}

if(document.getElementById("foreignWorker").value == "")
{
    alert("Please select a value");
    document.getElementById("foreignWorker").focus();
}


return console.log('processed inputs')
}
