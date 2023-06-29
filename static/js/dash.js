//POST JOB
var modalPJ = document.getElementById("postjob");
var btnPJ = document.getElementById("btnpj");
var spanPJ = document.getElementsByClassName("closepj")[0];
btnPJ.onclick = function() {
  modalPJ.style.display = "block";
}
spanPJ.onclick = function() {
  modalPJ.style.display = "none";
}