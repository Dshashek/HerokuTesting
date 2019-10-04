function validate() {
    var valid = 1

    if(document.getElementById("loanLength").value == "")
    valid = 0
{
    document.getElementById("loanLength").focus();
    valid = 0
}

if(document.getElementById("loanPurpose").value == "")
{
    document.getElementById("loanPurpose").focus();
    valid = 0
}

if(document.getElementById("loanSize").value == "")
{
    document.getElementById("loanSize").focus();
    valid = 0
}

if(document.getElementById("employmentHistory").value == "")
{
    document.getElementById("employmentHistory").focus();
    valid = 0
}

if(document.getElementById("cosignerCoborrower").value == "")
{
   document.getElementById("cosignerCoborrower").focus();
   valid = 0
}

if(document.getElementById("age").value == "")
{
    document.getElementById("age").focus();
    valid = 0
}

if(document.getElementById("homeowner").value == "")
{
    document.getElementById("homeowner").focus();
    valid = 0
}

if(document.getElementById("telephone").value == "")
{
    document.getElementById("telephone").focus();
    valid = 0
}

if(document.getElementById("foreignWorker").value == "")
{
    document.getElementById("foreignWorker").focus();
    valid = 0
}

if(valid=1) {
    getInputs();
}}


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

return console.log('processed inputs')
}
