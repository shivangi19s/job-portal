//ABOUT US
var modalAB = document.getElementById("aboutus");
var btnAB = document.getElementById("btnab");
var spanAB = document.getElementsByClassName("closeab")[0];
btnAB.onclick = function() {
  modalAB.style.display = "block";
}
spanAB.onclick = function() {
  modalAB.style.display = "none";
}

//REGISTER
var modalReg = document.getElementById("register");
var btnReg = document.getElementById("btnreg");
var spanReg = document.getElementsByClassName("closereg")[0];
btnReg.onclick = function() {
  modalReg.style.display = "block";
}
spanReg.onclick = function() {
  modalReg.style.display = "none";
}

//APPLICANT LOGIN
var modalApp = document.getElementById("applicant");
var btnApp = document.getElementById("btnapp");
var spanApp = document.getElementsByClassName("closeapp")[0];
btnApp.onclick = function() {
  modalApp.style.display = "block";
}
spanApp.onclick = function() {
  modalApp.style.display = "none";
}

//RECRUITER LOGIN
var modalRec = document.getElementById("recruiter");
var btnRec = document.getElementById("btnrec");
var spanRec = document.getElementsByClassName("closerec")[0];
btnRec.onclick = function() {
  modalRec.style.display = "block";
}
spanRec.onclick = function() {
  modalRec.style.display = "none";
}