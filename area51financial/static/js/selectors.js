
function getInputs() {

var inputResults = [];

var i1 = document.getElementById('dependents');
var dependents = i1.options[i1.selectedIndex].value;
inputResults.push({'input':dependents});

var i2 = document.getElementById('checkingAcctBalance');
var checkingAcctBalance = i2.options[i2.selectedIndex].value;
inputResults.push({'input':checkingAcctBalance});

var i3 = document.getElementById('loanLength');
var loanLength = i3.options[i3.selectedIndex].value;
inputResults.push({'input':loanLength});

var i4 = document.getElementById('creditHistory');
var creditHistory = i4.options[i4.selectedIndex].value;
inputResults.push({'input':creditHistory});

var i5 = document.getElementById('loanPurpose');
var loanPurpose = i5.options[i5.selectedIndex].value;
inputResults.push({'input':loanPurpose});

var i6 = document.getElementById('loanSize');
var loanSize = i6.options[i6.selectedIndex].value;
inputResults.push({'input':loanSize});

var i7 = document.getElementById('savingsAcctBalance');
var savingsAcctBalance = i7.options[i7.selectedIndex].value;
inputResults.push({'input':savingsAcctBalance});

var i8 = document.getElementById('employmentHistory');
var employmentHistory = i8.options[i8.selectedIndex].value;
inputResults.push({'input':employmentHistory});

var i9 = document.getElementById('cosignerCoborrower');
var cosignerCoborrower = i9.options[i9.selectedIndex].value;
inputResults.push({'input':cosignerCoborrower});

var i10 = document.getElementById('age');
var age = i10.options[i10.selectedIndex].value;
inputResults.push({'input':age});

var i11 = document.getElementById('otherLoans');
var otherLoans = i11.options[i11.selectedIndex].value;
inputResults.push({'input':otherLoans});

var i12 = document.getElementById('homeowner');
var homeowner = i12.options[i12.selectedIndex].value;
inputResults.push({'input':homeowner});

var i13 = document.getElementById('employmentType');
var employmentType = i13.options[i13.selectedIndex].value;
inputResults.push({'input':employmentType});

var i14 = document.getElementById('telephone');
var telephone = i14.options[i14.selectedIndex].value;
inputResults.push({'input':telephone});

var i15 = document.getElementById('foreignWorker');
var foreignWorker = i15.options[i15.selectedIndex].value;
inputResults.push({'input':foreignWorker});

document.getElementById('inputTarget').textContent = inputResults

return data = inputResults
}

function doWork() {
	// ajax the JSON to the server
	$.post("receiver", data, function(){

	});}
